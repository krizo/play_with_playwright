from playwright.sync_api import Page


class JourneyBase:
    def __init__(self, page: Page):
        self.page = page

    