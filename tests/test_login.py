import pytest
from pages.login_page import LoginPage


@pytest.fixture
def search_string():
    return 'Tyrese Haliburton'


@pytest.fixture
def login_credentials() -> tuple:
    return "student", "Password123"


@pytest.fixture
def invalid_user_name() -> tuple:
    return "invalid_user", "Password123"


@pytest.fixture
def invalid_password() -> tuple:
    return "student", "invalid_password"


def test_basic_login_positive(login_page: LoginPage, login_credentials: tuple):
    login_page.visit()
    login_page.login(*login_credentials)
    login_page.check_login_successful()


def test_basic_login_invalid_username_negative(login_page: LoginPage, invalid_user_name: tuple):
    login_page.visit()
    login_page.login(*invalid_user_name)
    login_page.check_login_invalid_user_name()


def test_basic_login_invalid_password_negative(login_page: LoginPage, invalid_password: tuple):
    login_page.visit()
    login_page.login(*invalid_password)
    login_page.check_login_invalid_password()
