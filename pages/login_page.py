from playwright.sync_api import Page
from pages.base_page import BasePage
import os
from dotenv import load_dotenv
load_dotenv()

class LoginPage(BasePage):
    __user_field_locator = "#user-name"
    __password_field_locator = "#password"
    __submit_button = "#login-button"
    __error_locator = '[data-test="error"]'

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def login_to_sauce_demo(self, user = os.getenv("USER_NAME"), password = os.getenv("PASSWORD"), error_message:bool = False):
        self.fill_text(self.__user_field_locator, user)
        self.fill_text(self.__password_field_locator, password)
        self.click(self.__submit_button)
        if error_message is not False:
            error_msg = self.get_inner_text(self.__error_locator)
            return error_msg
        
    def get_post_login_url(self):
        url = self.get_current_url()
        return url

    