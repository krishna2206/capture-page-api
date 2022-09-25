from playwright.sync_api import sync_playwright


def test_webpage(page_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(page_url)
        content = page.content()
        browser.close()
        return content
