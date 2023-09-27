from playwright.sync_api import Page
from pages.base_page import BasePage

class OrderCompletion(BasePage):

    _completion_header = '.complete-header'

    def __init__(self, page: Page) -> None:
        super().__init__(page)


    def  get_order_confirmation(self):
        return self.get_inner_text(self._completion_header)