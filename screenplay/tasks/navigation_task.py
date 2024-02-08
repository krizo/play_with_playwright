from screenplay.tasks.base_task import BaseTask


class NavigateToLoginPage(BaseTask):
    def perform(self, actor):
        login_page = actor.abilities['browse_the_web']
        login_page.visit()
