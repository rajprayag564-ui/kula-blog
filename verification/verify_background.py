from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the index.html file
        page.goto(f"file://{os.getcwd()}/index.html")

        # Wait for the page to render (though static, good practice)
        page.wait_for_selector(".book-container")

        # Take a screenshot
        screenshot_path = "verification/background_check.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()
