import pytest

from journey.LoginJourney import LoginJourney


@pytest.fixture
def login_credentials() -> dict:
    return {
        "user": "student",
        "password": "Password123"
    }


@pytest.fixture
def login_journey(login_page):
    return LoginJourney(login_page)


def test_basic_login_journey_positive(login_journey: LoginJourney, login_credentials: dict):
    login_journey.login_with_valid_credentials(*login_credentials.values())
    login_journey.check_login_successful()


def test_basic_login_journey_invalid_username_negative(login_journey: LoginJourney, login_credentials: dict):
    login_journey.login_with_invalid_username(login_credentials.get('password'))
    login_journey.check_login_invalid_user_name()


def test_basic_login_journey_invalid_password_negative(login_journey: LoginJourney, login_credentials: dict):
    login_journey.login_with_invalid_password(login_credentials.get('user'))
    login_journey.check_login_invalid_password()
