import uuid

from playwright.async_api import async_playwright


async def generate_webpage_screenshot(page_url, param_device=None):
    async with async_playwright() as playwright:
        try:
            if param_device is not None:
                device = playwright.devices[param_device]
                if device["defaultBrowserType"] == "firefox":
                    browser = await playwright.firefox.launch(headless=True)
                elif device["defaultBrowserType"] == "webkit":
                    browser = await playwright.webkit.launch(headless=True)
                else:
                    browser = await playwright.chromium.launch(headless=True)
                browser_context = await browser.new_context(**device)
            else:
                browser = await playwright.chromium.launch(headless=True)

            if param_device is not None:
                page = await browser_context.new_page()
            else:
                page = await browser.new_page()
            await page.goto(page_url)

            filename = f"{str(uuid.uuid4())}.png"
            await page.screenshot(path=f"screenshots/{filename}", full_page=True)
        except Exception as error:
            print(f"{type(error).__name__}: {error}")
            return False, f"{type(error).__name__}: {error}"
        else:
            return True, filename
        finally:
            await browser.close()
