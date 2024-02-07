from playwright.sync_api import Browser, Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://practicetestautomation.com/practice-test-login/'

    def __init__(self, page: Page):
        super().__init__(page)
        self.user_name = self.page.locator('#username')
        self.password = self.page.locator("#password")
        self.submit = self.page.locator("#submit")

    def login(self, user_name: str, password: str) -> None:
        self.user_name.fill(user_name)
        self.password.fill(password)
        self.submit.click()
