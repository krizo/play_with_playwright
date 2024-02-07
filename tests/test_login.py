import pytest
from pages.login_page import LoginPage


@pytest.fixture
def search_string():
    return 'Tyrese Haliburton'


@pytest.fixture
def login_credentials() -> tuple:
    return "student", "Password123"


def test_basic_login_positive(login_page: LoginPage, login_credentials: tuple):
    login_page.visit()
    login_page.login(*login_credentials)
