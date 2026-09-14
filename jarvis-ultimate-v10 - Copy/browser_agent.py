from playwright.sync_api import sync_playwright

class BrowserAgent:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start_browser(self):
        if not self.playwright:
            self.playwright = sync_playwright().start()
            # headless=False so you can watch JARVIS control the browser
            self.browser = self.playwright.chromium.launch(headless=False)
            self.page = self.browser.new_page()
            return "Browser launched successfully."
        return "Browser is already active."

    def navigate_to(self, url):
        if not self.page:
            self.start_browser()
        
        if not url.startswith("http"):
            url = f"https://{url}"
            
        try:
            self.page.goto(url, timeout=15000)
            return f"Successfully navigated to {self.page.title()}"
        except Exception as e:
            return f"Failed to load page: {str(e)}"

    def extract_page_text(self, char_limit=3000):
        if not self.page:
            return "Error: No browser window is open."
        
        try:
            # Grabs the visible text on the page and limits the length so it doesn't overload Gemini's context window
            text = self.page.evaluate("document.body.innerText")
            return text[:char_limit]
        except Exception as e:
            return f"Failed to extract text: {str(e)}"

    def close_browser(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
            self.playwright = None
        return "Browser closed."