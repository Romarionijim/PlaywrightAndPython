from playwright.sync_api import Page
from pages.base_page import BasePage
import os
from dotenv import load_dotenv
load_dotenv()

class LoginPage(BasePage):
    user_field_locator = "#user-name"
    password_field_locator = "#password"
    submit_button = "#login-button"
    error_locator = '[data-test="error"]'

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def login_to_sauce_demo(self, user = os.getenv("USER_NAME"), password = os.getenv("PASSWORD"), error_message:bool = False):
        self.fill_text(self.user_field_locator, user)
        self.fill_text(self.password_field_locator,password)
        self.click(self.submit_button)
        if error_message is not False:
            error_msg = self.get_inner_text(self.error_locator)
            return error_msg
        
    def get_post_login_url(self):
        url = self.get_current_url()
        return url

    