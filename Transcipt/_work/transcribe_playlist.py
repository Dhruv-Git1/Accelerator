#!/usr/bin/env python3
"""Slow, resumable YouTube-audio transcription for the Zynq course playlist."""

from __future__ import annotations

import argparse
import contextlib
import csv
import hashlib
import html
import json
import msvcrt
import os
import random
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from faster_whisper import WhisperModel


ROOT = Path(r"D:\Desktop\Accelerator")
TARGET_DIR = ROOT / "Transcipt"
WORK_DIR = TARGET_DIR / "_work"
PLAYLIST_JSON = WORK_DIR / "agent_ytdlp" / "playlist_flat.json"
AUDIO_DIR = WORK_DIR / "audio"
SEGMENTS_DIR = WORK_DIR / "segments"
COMPLETION_DIR = WORK_DIR / "completed"
PROGRESS_FILE = WORK_DIR / "progress.json"
EVENT_LOG = WORK_DIR / "events.jsonl"
LOCK_FILE = WORK_DIR / "pipeline.lock"
INDEX_FILE = TARGET_DIR / "index.csv"
COOKIES_FILE = ROOT / "cookies.txt"
SESSION_COOKIES_FILE = WORK_DIR / "cookies.session.txt"
NODE_RUNTIME = Path(r"C:\Program Files\nodejs\node.exe")

PLAYLIST_ID = "PLXHMvqUANAFOviU0J8HSp0E91lLJInzX1"
MODEL_NAME = "small.en"

TECHNICAL_TERMS = (
    "Vipin Kizheppatt, Xilinx, Zynq, ZedBoard, FPGA, SoC, Vivado, Vitis, "
    "Verilog HDL, AXI, AXI4-Lite, AXI4-Stream, SDK, IP core, OLED, SPI, DMA, "
    "VDMA, UART, ILA, GPIO, FIFO, PCAP, ICAP, Sobel, HDMI, XSCT, SD card, "
    "ESP8266, TensorFlow, neural network, Network-on-Chip, NoC"
)

NOISE_ONLY = re.compile(
    r"^\s*(?:\[(?:music|applause|laughter|silence)\]|\((?:music|applause|laughter|silence)\))\s*[.!]?\s*$",
    re.IGNORECASE,
)
INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
WHITESPACE = re.compile(r"\s+")
VIDEO_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{11}$")
FINAL_AUDIO_SUFFIXES = {
    ".aac",
    ".flac",
    ".m4a",
    ".mp3",
    ".mp4",
    ".ogg",
    ".opus",
    ".wav",
    ".webm",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temp.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temp, path)


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(
        path,
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
    )


def append_event(event: str, **details: Any) -> None:
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    record = {"at": now_iso(), "event": event, **details}
    with EVENT_LOG.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


@contextlib.contextmanager
def single_run_lock():
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    handle = LOCK_FILE.open("a+b")
    if handle.seek(0, os.SEEK_END) == 0:
        handle.write(b"0")
        handle.flush()
    handle.seek(0)
    try:
        msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
    except OSError as exc:
        handle.close()
        raise RuntimeError(
            "Another transcript pipeline process already holds the run lock"
        ) from exc
    try:
        handle.seek(1)
        handle.truncate()
        handle.write(str(os.getpid()).encode("ascii"))
        handle.flush()
        yield
    finally:
        handle.seek(0)
        try:
            msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        finally:
            handle.close()


def safe_title(title: str, limit: int = 170) -> str:
    title = html.unescape(title)
    title = INVALID_FILENAME_CHARS.sub(" - ", title)
    title = WHITESPACE.sub(" ", title).strip(" .-")
    if len(title) > limit:
        title = title[:limit].rstrip(" .-")
    return title or "Untitled"


def transcript_filename(position: int, title: str) -> str:
    return f"{position:03d} - {safe_title(title)}.txt"


def load_manifest() -> list[dict[str, Any]]:
    raw = PLAYLIST_JSON.read_bytes()
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        playlist_text = raw.decode("utf-16")
    else:
        playlist_text = raw.decode("utf-8-sig")
    data = json.loads(playlist_text)
    entries = data.get("entries") or []
    manifest: list[dict[str, Any]] = []
    for position, entry in enumerate(entries, start=1):
        video_id = str(entry.get("id") or "").strip()
        title = str(entry.get("title") or "").strip()
        if not video_id or not title:
            raise ValueError(f"Playlist entry {position} is missing an id or title")
        if not VIDEO_ID_PATTERN.fullmatch(video_id):
            raise ValueError(
                f"Playlist entry {position} has an invalid video id: {video_id!r}"
            )
        manifest.append(
            {
                "position": position,
                "id": video_id,
                "title": title,
                "duration": int(entry.get("duration") or 0),
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "file": transcript_filename(position, title),
            }
        )
    ids = [item["id"] for item in manifest]
    if len(manifest) != 85 or len(set(ids)) != 85:
        raise ValueError(
            f"Expected 85 unique playlist videos, got {len(manifest)} entries "
            f"and {len(set(ids))} unique ids"
        )
    return manifest


def audio_candidates(video_id: str) -> list[Path]:
    return sorted(AUDIO_DIR.glob(f"{video_id}.*"))


def audio_is_decodable(path: Path) -> bool:
    if path.suffix.lower() not in FINAL_AUDIO_SUFFIXES:
        return False
    try:
        result = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-select_streams",
                "a:0",
                "-show_entries",
                "stream=codec_type",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                str(path),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    return result.returncode == 0 and "audio" in result.stdout.lower()


def find_audio(video_id: str) -> Path | None:
    for candidate in audio_candidates(video_id):
        if not candidate.is_file() or candidate.stat().st_size <= 100_000:
            continue
        if audio_is_decodable(candidate):
            return candidate
        if candidate.suffix.lower() in FINAL_AUDIO_SUFFIXES:
            quarantine = candidate.with_name(
                f"{candidate.name}.invalid-{int(time.time())}"
            )
            candidate.replace(quarantine)
            append_event(
                "invalid_audio_quarantined",
                video_id=video_id,
                source=str(candidate),
                quarantine=str(quarantine),
            )
    return None


def download_audio(
    item: dict[str, Any],
    session_cookies: Path | None,
) -> Path:
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    output_template = str(AUDIO_DIR / f"{item['id']}.%(ext)s")
    command = [
        "yt-dlp",
        "--ignore-config",
        "--no-playlist",
        "--js-runtimes",
        f"node:{NODE_RUNTIME}",
        "--socket-timeout",
        "30",
        "--retries",
        "5",
        "--fragment-retries",
        "5",
        "--no-progress",
        "--newline",
        "-f",
        "139/bestaudio[language^=en]/bestaudio",
        "-o",
        output_template,
    ]
    if session_cookies is not None:
        command.extend(["--cookies", str(session_cookies)])
    command.append(item["url"])

    append_event(
        "download_started",
        position=item["position"],
        video_id=item["id"],
        title=item["title"],
    )
    result = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=20 * 60,
        check=False,
    )
    audio = find_audio(item["id"])
    if result.returncode != 0 or audio is None:
        error_tail = (result.stderr or result.stdout or "")[-2500:]
        append_event(
            "download_failed",
            position=item["position"],
            video_id=item["id"],
            returncode=result.returncode,
            error=error_tail,
        )
        raise RuntimeError(
            f"Audio download failed for #{item['position']} {item['id']} "
            f"(exit {result.returncode})"
        )
    append_event(
        "download_completed",
        position=item["position"],
        video_id=item["id"],
        bytes=audio.stat().st_size,
    )
    return audio


def clean_segment_text(text: str) -> str:
    text = html.unescape(text)
    text = WHITESPACE.sub(" ", text).strip()
    if not text or NOISE_ONLY.fullmatch(text):
        return ""
    return text


def pack_paragraphs(texts: list[str], target_chars: int = 750) -> str:
    paragraphs: list[str] = []
    current: list[str] = []
    current_chars = 0
    for text in texts:
        if not text:
            continue
        if current and current_chars + 1 + len(text) > target_chars:
            paragraphs.append(" ".join(current))
            current = []
            current_chars = 0
        current.append(text)
        current_chars += len(text) + (1 if current_chars else 0)
        if current_chars >= 520 and text.endswith((".", "?", "!")):
            paragraphs.append(" ".join(current))
            current = []
            current_chars = 0
    if current:
        paragraphs.append(" ".join(current))
    return "\n\n".join(paragraphs).strip() + "\n"


def transcribe_audio(
    model: WhisperModel,
    item: dict[str, Any],
    audio: Path,
) -> tuple[str, dict[str, Any]]:
    prompt = (
        f"Technical lecture titled “{item['title']}” by Vipin Kizheppatt. "
        f"Vocabulary: {TECHNICAL_TERMS}."
    )
    append_event(
        "transcription_started",
        position=item["position"],
        video_id=item["id"],
        audio=str(audio),
        model=MODEL_NAME,
    )
    started = time.monotonic()
    segment_iter, info = model.transcribe(
        str(audio),
        language="en",
        task="transcribe",
        beam_size=1,
        best_of=1,
        temperature=0.0,
        vad_filter=True,
        vad_parameters={"min_silence_duration_ms": 500},
        condition_on_previous_text=True,
        initial_prompt=prompt,
        hotwords=TECHNICAL_TERMS,
        word_timestamps=False,
    )

    raw_segments: list[dict[str, Any]] = []
    spoken_texts: list[str] = []
    for segment in segment_iter:
        text = clean_segment_text(segment.text)
        if not text:
            continue
        spoken_texts.append(text)
        raw_segments.append(
            {
                "start": round(float(segment.start), 3),
                "end": round(float(segment.end), 3),
                "text": text,
            }
        )

    transcript = pack_paragraphs(spoken_texts)
    if len(transcript) < 100 or len(raw_segments) < 2:
        raise RuntimeError(
            f"Transcript for #{item['position']} {item['id']} is unexpectedly short"
        )

    elapsed = round(time.monotonic() - started, 2)
    metadata = {
        "playlist_id": PLAYLIST_ID,
        "position": item["position"],
        "video_id": item["id"],
        "title": item["title"],
        "url": item["url"],
        "video_duration_seconds": item["duration"],
        "detected_language": info.language,
        "detected_language_probability": round(
            float(info.language_probability), 6
        ),
        "model": MODEL_NAME,
        "transcription_elapsed_seconds": elapsed,
        "created_at": now_iso(),
        "segments": raw_segments,
    }
    append_event(
        "transcription_completed",
        position=item["position"],
        video_id=item["id"],
        elapsed_seconds=elapsed,
        segments=len(raw_segments),
        characters=len(transcript),
    )
    return transcript, metadata


def segment_file(item: dict[str, Any]) -> Path:
    return SEGMENTS_DIR / f"{item['position']:03d}_{item['id']}.json"


def completion_file(item: dict[str, Any]) -> Path:
    return COMPLETION_DIR / f"{item['position']:03d}_{item['id']}.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_completion_marker(item: dict[str, Any]) -> None:
    transcript_path = TARGET_DIR / item["file"]
    segments_path = segment_file(item)
    if not transcript_path.is_file() or not segments_path.is_file():
        raise RuntimeError(
            f"Cannot mark #{item['position']} complete without both output files"
        )
    marker = {
        "playlist_id": PLAYLIST_ID,
        "position": item["position"],
        "video_id": item["id"],
        "model": MODEL_NAME,
        "transcript_file": item["file"],
        "transcript_bytes": transcript_path.stat().st_size,
        "transcript_sha256": sha256_file(transcript_path),
        "segments_file": segments_path.name,
        "segments_bytes": segments_path.stat().st_size,
        "segments_sha256": sha256_file(segments_path),
        "completed_at": now_iso(),
    }
    atomic_write_json(completion_file(item), marker)


def transcript_is_complete(item: dict[str, Any]) -> bool:
    transcript_path = TARGET_DIR / item["file"]
    segments_path = segment_file(item)
    marker_path = completion_file(item)
    if not (
        transcript_path.is_file()
        and transcript_path.stat().st_size > 100
        and segments_path.is_file()
        and segments_path.stat().st_size > 100
        and marker_path.is_file()
    ):
        return False
    try:
        marker = json.loads(marker_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return False
    return bool(
        marker.get("playlist_id") == PLAYLIST_ID
        and marker.get("position") == item["position"]
        and marker.get("video_id") == item["id"]
        and marker.get("model") == MODEL_NAME
        and marker.get("transcript_file") == item["file"]
        and marker.get("segments_file") == segments_path.name
        and marker.get("transcript_bytes") == transcript_path.stat().st_size
        and marker.get("segments_bytes") == segments_path.stat().st_size
        and marker.get("transcript_sha256") == sha256_file(transcript_path)
        and marker.get("segments_sha256") == sha256_file(segments_path)
    )


def prepare_session_cookies() -> Path | None:
    if not COOKIES_FILE.is_file():
        return None
    shutil.copyfile(COOKIES_FILE, SESSION_COOKIES_FILE)
    try:
        SESSION_COOKIES_FILE.chmod(0o600)
    except OSError:
        pass
    return SESSION_COOKIES_FILE


def remove_session_cookies() -> None:
    try:
        SESSION_COOKIES_FILE.unlink(missing_ok=True)
    except OSError as exc:
        append_event("session_cookie_cleanup_failed", error=str(exc))


def write_index(manifest: list[dict[str, Any]]) -> None:
    rows: list[dict[str, Any]] = []
    for item in manifest:
        transcript_path = TARGET_DIR / item["file"]
        complete = transcript_is_complete(item)
        words = 0
        if complete:
            words = len(transcript_path.read_text(encoding="utf-8").split())
        rows.append(
            {
                "position": item["position"],
                "video_id": item["id"],
                "title": item["title"],
                "duration_seconds": item["duration"],
                "transcript_file": item["file"],
                "status": "complete" if complete else "pending",
                "word_count": words,
                "youtube_url": item["url"],
            }
        )

    temp = INDEX_FILE.with_name(f".{INDEX_FILE.name}.{os.getpid()}.tmp")
    temp.parent.mkdir(parents=True, exist_ok=True)
    with temp.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temp, INDEX_FILE)


def write_progress(
    manifest: list[dict[str, Any]],
    status: str,
    current: dict[str, Any] | None = None,
    message: str | None = None,
) -> None:
    completed = sum(transcript_is_complete(item) for item in manifest)
    value: dict[str, Any] = {
        "status": status,
        "pid": os.getpid(),
        "model": MODEL_NAME,
        "playlist_count": len(manifest),
        "completed": completed,
        "remaining": len(manifest) - completed,
        "updated_at": now_iso(),
    }
    if current:
        value["current_position"] = current["position"]
        value["current_video_id"] = current["id"]
        value["current_title"] = current["title"]
    if message:
        value["message"] = message
    atomic_write_json(PROGRESS_FILE, value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=85)
    parser.add_argument("--threads", type=int, default=8)
    parser.add_argument("--sleep-min", type=float, default=45.0)
    parser.add_argument("--sleep-max", type=float, default=90.0)
    parser.add_argument("--keep-audio", action="store_true")
    return parser.parse_args()


def run_pipeline(args: argparse.Namespace) -> int:
    if not 1 <= args.start <= args.end <= 85:
        raise ValueError("--start and --end must satisfy 1 <= start <= end <= 85")
    if args.sleep_min < 0 or args.sleep_max < args.sleep_min:
        raise ValueError("Invalid sleep range")

    for directory in (
        TARGET_DIR,
        WORK_DIR,
        AUDIO_DIR,
        SEGMENTS_DIR,
        COMPLETION_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest()
    write_index(manifest)
    write_progress(manifest, "starting")
    append_event(
        "run_started",
        pid=os.getpid(),
        start=args.start,
        end=args.end,
        threads=args.threads,
        model=MODEL_NAME,
    )

    failures: list[int] = []
    selected = [
        item
        for item in manifest
        if args.start <= item["position"] <= args.end
    ]
    pending = [item for item in selected if not transcript_is_complete(item)]
    model: WhisperModel | None = None
    if pending:
        write_progress(
            manifest,
            "starting",
            pending[0],
            "Validating local speech model",
        )
        model = WhisperModel(
            MODEL_NAME,
            device="cpu",
            compute_type="int8",
            cpu_threads=args.threads,
            num_workers=1,
            local_files_only=True,
        )

    session_cookies = prepare_session_cookies()

    try:
        for selected_index, item in enumerate(selected):
            if transcript_is_complete(item):
                append_event(
                    "video_skipped_complete",
                    position=item["position"],
                    video_id=item["id"],
                )
                continue

            write_progress(manifest, "working", item, "Preparing audio")
            try:
                audio = find_audio(item["id"]) or download_audio(
                    item,
                    session_cookies,
                )
                if model is None:
                    raise RuntimeError("Local speech model was not initialized")

                write_progress(
                    manifest,
                    "working",
                    item,
                    "Transcribing locally",
                )
                transcript, metadata = transcribe_audio(model, item, audio)
                atomic_write_json(
                    segment_file(item),
                    metadata,
                )
                atomic_write_text(TARGET_DIR / item["file"], transcript)
                write_completion_marker(item)
                write_index(manifest)
                write_progress(
                    manifest,
                    "working",
                    item,
                    "Transcript saved",
                )

                if not args.keep_audio:
                    try:
                        audio.unlink(missing_ok=True)
                        append_event(
                            "temporary_audio_removed",
                            position=item["position"],
                            video_id=item["id"],
                        )
                    except OSError as exc:
                        append_event(
                            "temporary_audio_remove_failed",
                            position=item["position"],
                            video_id=item["id"],
                            error=str(exc),
                        )
            except Exception as exc:
                failures.append(item["position"])
                append_event(
                    "video_failed",
                    position=item["position"],
                    video_id=item["id"],
                    error=f"{type(exc).__name__}: {exc}",
                )
                write_progress(
                    manifest,
                    "working",
                    item,
                    f"Failed: {type(exc).__name__}: {exc}",
                )

            if selected_index < len(selected) - 1:
                delay = random.uniform(args.sleep_min, args.sleep_max)
                append_event(
                    "pacing_delay",
                    seconds=round(delay, 2),
                    after_position=item["position"],
                )
                time.sleep(delay)
    except KeyboardInterrupt:
        append_event("run_interrupted", pid=os.getpid())
        write_progress(manifest, "interrupted", message="Interrupted")
        return 130
    finally:
        remove_session_cookies()

    write_index(manifest)
    if failures:
        message = "Failed playlist positions: " + ", ".join(map(str, failures))
        append_event("run_completed_with_failures", failures=failures)
        write_progress(manifest, "completed_with_failures", message=message)
        print(message, flush=True)
        return 1

    missing = [
        item["position"]
        for item in manifest
        if not transcript_is_complete(item)
    ]
    if missing:
        message = (
            f"Selected range {args.start}-{args.end} completed; "
            f"{len(missing)} of 85 playlist transcripts remain"
        )
        append_event(
            "range_completed",
            start=args.start,
            end=args.end,
            missing_count=len(missing),
        )
        write_progress(manifest, "range_completed", message=message)
        print(message, flush=True)
        if args.start == 1 and args.end == 85:
            return 1
        return 0

    append_event("run_completed", pid=os.getpid(), verified=85)
    write_progress(manifest, "completed", message="All 85 transcripts verified")
    return 0


def main() -> int:
    args = parse_args()
    with single_run_lock():
        return run_pipeline(args)


if __name__ == "__main__":
    sys.exit(main())
