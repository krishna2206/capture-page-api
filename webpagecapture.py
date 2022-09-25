import uuid
from playwright.async_api import async_playwright


async def generate_webpage_screenshot(page_url):
    async with async_playwright() as playwright:
        try:
            device = playwright.devices["Pixel 4"]
            browser = await playwright.chromium.launch(headless=True)
            context = await browser.new_context(**device)

            page = await browser.new_page()
            await page.goto(page_url)

            filename = f"{str(uuid.uuid4())}.png"
            await page.screenshot(path=f"screenshots/{filename}", full_page=True)
        except Exception as error:
            return False, f"{type(error).__name__}: {error}"
        else:
            return True, filename
        finally:
            await browser.close()
