from playwright.sync_api import Page
from pages.base_page import BasePage

class CheckoutStepOnePage(BasePage):

    __first_name_field = '#first-name'
    __last_name_field = '#last-name'
    __zip_field = '#postal-code'
    __continue_button = '#continue'
    __cancel_button = '#cancel'

    def __init__(self, page: Page) -> None:
        super().__init__(page)


    def fill_checkout_details(self, firstname, lastname, zip):
        self.fill_text(self.__first_name_field, firstname)
        self.fill_text(self.__last_name_field, lastname)
        self.fill_text(self.__zip_field, zip)
    
    def click_continue(self):
        self.click(self.__continue_button)

    def click_cancel(self):
        self.click(self.__cancel_button)