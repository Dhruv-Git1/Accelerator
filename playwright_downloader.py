import sys
sys.stdout.reconfigure(encoding='utf-8')
import asyncio
import json
import os
import re
import random
import urllib.parse
import urllib.request
import html as html_module
from playwright.async_api import async_playwright

async def extract_transcript(page, title, raw_path):
    query = f"Vipin Kizheppatt {title}"
    search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
    print(f"  -> Searching: {query}")
    await page.goto(search_url, wait_until="domcontentloaded")
    
    try:
        await page.wait_for_selector("ytd-video-renderer", timeout=10000)
        video_link = page.locator("ytd-video-renderer a#video-title").first
        
        href = await video_link.get_attribute("href")
        full_url = "https://www.youtube.com" + href
        print(f"  -> Found video URL. Loading full page: {full_url}")
        await page.goto(full_url, wait_until="domcontentloaded")
        
        # Click transcript button
        try:
            await page.wait_for_selector("tp-yt-paper-button#expand", timeout=10000)
            more_btn = page.locator("tp-yt-paper-button#expand")
            if await more_btn.count() > 0:
                await more_btn.first.click()
                await page.wait_for_timeout(1000)
        except Exception as e:
            print(f"  -> Expand button not found or click failed: {e}")
            
        try:
            await page.wait_for_selector("button[aria-label='Show transcript']", timeout=10000)
            transcript_btn = page.locator("button[aria-label='Show transcript']")
            await transcript_btn.first.click()
        except Exception as e:
            print(f"  -> Could not find or click 'Show transcript' button: {e}")
            return False
            
        try:
            await page.wait_for_selector("ytd-transcript-segment-renderer", timeout=15000)
        except Exception as e:
            print("  -> Transcript segments did not load in DOM")
            try:
                await page.screenshot(path=r"D:\Desktop\Accelerator\screenshot.png")
                page_html = await page.content()
                with open(r"D:\Desktop\Accelerator\page_dump.html", "w", encoding="utf-8") as f:
                    f.write(page_html)
                print("  -> Saved screenshot and page dump for debugging.")
            except Exception as se:
                print(f"  -> Debug dump failed: {se}")
            return False
            
        # Extract everything via JS
        transcript_text = await page.evaluate("""() => {
            const segments = document.querySelectorAll('ytd-transcript-segment-renderer');
            let result = '';
            for (const seg of segments) {
                const timeEl = seg.querySelector('.segment-timestamp');
                const textEl = seg.querySelector('.segment-text');
                if (timeEl && textEl) {
                    const time = timeEl.innerText.trim();
                    const text = textEl.innerText.trim().replace(/\\n/g, ' ');
                    result += '[' + time + '] ' + text + '\\n';
                }
            }
            return result;
        }""")
        
        if not transcript_text.strip():
            print("  -> Transcript text was empty")
            return False
            
        with open(raw_path, "w", encoding="utf-8") as f:
            f.write(transcript_text)
            
        print("  -> Downloaded successfully.")
        return True
    except Exception as e:
        print(f"  -> Failed to extract: {e}")
        return False

async def main():
    os.makedirs(r"D:\Desktop\Accelerator\raw", exist_ok=True)
    
    lines = open(r"C:\Users\nisha\.gemini\antigravity\brain\ba32c169-5d5c-44d2-803b-f957e04d61d6\raw_user_input.txt", "r", encoding="utf-8").read().split('\n')
    titles = []
    for i, l in enumerate(lines):
        l = l.strip()
        if 'views' in l:
            for j in range(i-1, -1, -1):
                t = lines[j].strip()
                if t and t != '•' and not (':' in t and len(t) <= 5 and t.replace(':','').isdigit()):
                    titles.append(t)
                    break
                
    final_titles = []
    for t in titles:
        if t and t not in final_titles and t != '<USER_REQUEST>':
            final_titles.append(t)
            
    print(f"Found {len(final_titles)} videos.")
    
    async with async_playwright() as p:
        try:
            browser = await p.chromium.connect_over_cdp("http://localhost:9222")
            print("  -> Connected to Chrome over CDP")
        except Exception as e:
            print(f"  -> Failed to connect to Chrome over CDP: {e}")
            return
            
        context = browser.contexts[0]
        page = await context.new_page()
        
        for i, title in enumerate(final_titles):
            try:
                print(f"[{i+1}/{len(final_titles)}] Processing: {title}")
            except UnicodeEncodeError:
                print(f"[{i+1}/{len(final_titles)}] Processing: {title.encode('ascii', 'ignore').decode()}")
                
            safe_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
            raw_path = rf"D:\Desktop\Accelerator\raw\{safe_title}.txt"
            
            if os.path.exists(raw_path) and os.path.getsize(raw_path) > 10:
                print("  -> Already exists. Skipping download.")
                continue
                
            await extract_transcript(page, title, raw_path)
            await asyncio.sleep(random.uniform(3, 7))
            
        await page.close()

if __name__ == "__main__":
    asyncio.run(main())
