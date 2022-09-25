import uuid
import math
from io import BytesIO

from PIL import Image
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

            full_page_image_buffer = await page.screenshot(full_page=True)
            string_io = BytesIO(full_page_image_buffer)
            full_page_image = Image.open(string_io)
            parts = math.ceil(full_page_image.height / 720)
            height_per_part = full_page_image.height / parts
            part_page_image_buffers = []
            for part in range(parts):
                part_page_image_buffer = await page.screenshot(
                    clip={
                        "x": 0,
                        "y": height_per_part * part,
                        "width": full_page_image.width,
                        "height": height_per_part,
                    })
                part_page_image_buffers.append(part_page_image_buffer)
            final_image = Image.new("RGB", (full_page_image.width, full_page_image.height))
            for part, part_page_image_buffer in enumerate(part_page_image_buffers):
                string_io = BytesIO(part_page_image_buffer)
                part_page_image = Image.open(string_io)
                final_image.paste(part_page_image, (0, height_per_part * part))
            final_image.save(f"screenshots/{filename}")
        except Exception as error:
            print(f"{type(error).__name__}: {error}")
            return False, f"{type(error).__name__}: {error}"
        else:
            return True, filename
        finally:
            await browser.close()
