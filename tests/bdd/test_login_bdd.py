import pytest
from pytest_bdd import scenario, given, when, then, parsers
from page_objects.login_page import LoginPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@scenario('login.feature', 'Logging in with valid credentials')
def test_login_positive():
    pass


@scenario('login.feature', 'Logging in with invalid credentials')
def test_login_negative():
    pass


@scenario('login.feature', 'Logging in with invalid credentials')
def test_login_negative():
    pass


@given("I am on the login page")
def i_am_on_the_login_page(login_page):
    login_page.visit()


@when(parsers.parse('I log in with {username} and {password}'))
def log_in_with_credentials(login_page, username, password):
    login_page.login(username, password)


@then(parsers.parse('I should {expected_result}'))
def check_result(login_page, expected_result):
    if expected_result == "see successful login":
        login_page.check_login_successful()
    elif expected_result == "see invalid username":
        login_page.check_login_invalid_user_name()
    elif expected_result == "see invalid password":
        login_page.check_login_invalid_password()
