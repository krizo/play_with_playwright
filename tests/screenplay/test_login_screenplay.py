import pytest

from screenplay import Actor
from screenplay.tasks.login_task import LoginTask, LoginWithInvalidPassword, LoginWithInvalidUsername
from screenplay.tasks.navigation_task import NavigateToLoginPage


@pytest.fixture
def login_credentials() -> tuple:
    return "student", "Password123"


@pytest.fixture
def test_user(login_page):
    return Actor("TestUser", {"browse_the_web": login_page})


@pytest.fixture
def go_to_login_page() -> NavigateToLoginPage:
    return NavigateToLoginPage()


@pytest.fixture
def login_with_valid_credentials(login_credentials) -> LoginTask:
    return LoginTask(*login_credentials)


@pytest.fixture
def login_with_invalid_username(login_credentials) -> LoginTask:
    return LoginWithInvalidUsername(username="invalid_username", password=login_credentials[1])


@pytest.fixture
def login_with_invalid_password(login_credentials) -> LoginTask:
    return LoginWithInvalidPassword(username=login_credentials[0], password="invalid_password")


def test_login_screenplay_with_valid_credentials(test_user, go_to_login_page, login_with_valid_credentials):
    test_user.perform(go_to_login_page)
    test_user.perform(login_with_valid_credentials)


def test_login_screenplay_with_invalid_user_name(test_user, go_to_login_page, login_with_invalid_username):
    test_user.perform(go_to_login_page)
    test_user.perform(login_with_invalid_username)


def test_login_screenplay_with_invalid_password(test_user, go_to_login_page, login_with_invalid_password):
    test_user.perform(go_to_login_page)
    test_user.perform(login_with_invalid_password)
