import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        await page.goto("https://www.youtube.com/watch?v=GILjTGScbfc", wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)
        
        accept_btn = page.locator("button:has-text('Accept all')")
        if await accept_btn.count() > 0:
            await accept_btn.first.click()
            await page.wait_for_timeout(1000)
            
        more_btn = page.locator("tp-yt-paper-button#expand")
        if await more_btn.count() > 0:
            await more_btn.first.click()
            await page.wait_for_timeout(1000)
            
        transcript_btn = page.locator("button:has-text('Show transcript')")
        if await transcript_btn.count() > 0:
            await transcript_btn.first.click()
            await page.wait_for_timeout(3000)
        
        html = await page.content()
        with open(r"D:\Desktop\Accelerator\page_dump.html", "w", encoding="utf-8") as f:
            f.write(html)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
