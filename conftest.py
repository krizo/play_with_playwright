import pytest
from playwright.sync_api import Page

from page_objects.login_page import LoginPage


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)
