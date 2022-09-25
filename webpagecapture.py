from playwright.async_api import async_playwright


async def test_webpage(page_url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(page_url)
        content = await page.content()
        await browser.close()
        return content
