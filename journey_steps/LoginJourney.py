from playwright.sync_api import Page, expect

from journey_steps.journey_base import JourneyBase
from pages.login_page import LoginPage


class LoginJourney(JourneyBase):
    def __init__(self, login_page: LoginPage):
        super().__init__(login_page.page)
        self.page = login_page

    def login_with_valid_credentials(self, user_name: str, password: str):
        self.page.visit()
        self.page.login(user_name=user_name, password=password)
        self.page.check_login_successful()

    def login_with_invalid_username(self, password: str):
        self.page.visit()
        self.page.login(user_name="invalid_username", password=password)
        self.page.check_login_invalid_user_name()

    def login_with_invalid_password(self, user_name: str):
        self.page.visit()
        self.page.login(user_name=user_name, password='invalid_password')
        self.page.check_login_invalid_password()

    def check_login_successful(self):
        self.page.check_login_successful()

    def check_login_invalid_user_name(self):
        self.page.check_login_invalid_user_name()

    def check_login_invalid_password(self):
        self.page.check_login_invalid_password()
