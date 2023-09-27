from playwright.sync_api import Page, expect
from enums.Enums import ApplicationUrl
from pages.login_page import LoginPage
import pytest

# @classmethod
# @pytest.fixture(autouse=True, scope="function")
# def init_instance(page:Page):
#     login_page = LoginPage(page)

    
def test_valid_login(page:Page):
    login_page = LoginPage(page)
    login_page.goto(ApplicationUrl.SAUCE_DEMO)
    login_page.login_to_sauce_demo()
    url = login_page.get_post_login_url()
    assert "inventory.html" in url

def test_invalid_username_and_password(page:Page):
    login_page = LoginPage(page)
    login_page.goto(ApplicationUrl.SAUCE_DEMO)
    error_message = login_page.login_to_sauce_demo("John", "Doe", error_message=True)
    assert error_message == "Epic sadface: Username and password do not match any user in this service"

# def test_invalid_username(page:Page):
#     login_page = LoginPage(page)
#     login_page.goto(ApplicationUrl.SAUCE_DEMO)
#     login_page.login_to_sauce_demo()