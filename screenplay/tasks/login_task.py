from screenplay.actor import Actor
from screenplay.tasks.base_task import BaseTask
from pages.login_page import LoginPage


class LoginTask(BaseTask):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def perform(self, actor: Actor):
        login_page: LoginPage = actor.abilities['browse_the_web']
        login_page.visit()
        login_page.login(self.username, self.password)
        login_page.check_login_successful()


class LoginWithInvalidUsername(LoginTask):
    def perform(self, actor: Actor):
        login_page: LoginPage = actor.abilities['browse_the_web']
        login_page.visit()
        login_page.login(self.username, self.password)
        login_page.check_login_invalid_user_name()


class LoginWithInvalidPassword(LoginTask):
    def perform(self, actor: Actor):
        login_page: LoginPage = actor.abilities['browse_the_web']
        login_page.visit()
        login_page.login(self.username, self.password)
        login_page.check_login_invalid_password()
