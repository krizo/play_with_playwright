from playwright.sync_api import Page, expect

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://practicetestautomation.com/practice-test-login/'
    INVALID_USERNAME_ERROR = "Your username is invalid!"
    INVALID_PASSWORD_ERROR = "Your password is invalid!"

    def __init__(self, page: Page):
        super().__init__(page)
        self.user_name = self.page.locator('#username')
        self.password = self.page.locator("#password")
        self.submit = self.page.locator("#submit")
        self.successful_login = self.page.locator(".post-title")
        self.login_failed = self.page.locator("#error")

    def login(self, user_name: str, password: str) -> None:
        self.user_name.fill(user_name)
        self.password.fill(password)
        self.submit.click()

    def check_login_successful(self):
        expect(self.successful_login).to_have_text("Logged In Successfully")

    def check_login_invalid_user_name(self):
        expect(self.login_failed).to_have_text(self.INVALID_USERNAME_ERROR)

    def check_login_invalid_password(self):
        expect(self.login_failed).to_have_text(self.INVALID_PASSWORD_ERROR)
