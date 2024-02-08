from playwright.sync_api import Page


class BasePage:
    URL: str = None

    def __init__(self, page: Page) -> None:
        self.page = page
        if self.URL is None:
            raise ValueError(f"Page {self.__class__.__name__} needs to have URL property defined")

    def visit(self):
        self.page.goto(self.URL)


