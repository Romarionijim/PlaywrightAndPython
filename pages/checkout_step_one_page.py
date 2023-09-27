from playwright.sync_api import Page
from pages.base_page import BasePage

class CheckoutStepOnePage(BasePage):

    _first_name_field = '#first-name'
    _last_name_field = '#last-name'
    _zip_field = '#postal-code'
    _continue_button = '#continue'
    _cancel_button = '#cancel'

    def __init__(self, page: Page) -> None:
        super().__init__(page)


    def fill_checkout_details(self, firstname, lastname, zip):
        self.fill_text(self._first_name_field, firstname)
        self.fill_text(self._last_name_field, lastname)
        self.fill_text(self._zip_field,zip)
    
    def click_continue(self):
        self.click(self._continue_button)

    def click_cancel(self):
        self.click(self._cancel_button)