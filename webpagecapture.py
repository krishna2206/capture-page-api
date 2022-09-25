from playwright.async_api import async_playwright


async def test_webpage(page_url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(page_url)
        screenshot_url = await page.screenshot(path="files/screenshot.png")
        # content = await page.content()
        await browser.close()
        return screenshot_url
