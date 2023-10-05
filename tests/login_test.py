from playwright.sync_api import Page, expect
from enums.Enums import ApplicationUrl
from pages.login_page import LoginPage
import pytest


@pytest.fixture(scope="function")
def login_page(page: Page):
    print("starting login sanity tests")
    yield LoginPage(page)
    print("Login sanity tests finished execution")


@pytest.mark.SANITY
def test_valid_login(login_page):
    login_page.goto(ApplicationUrl.SAUCE_DEMO)
    login_page.login_to_sauce_demo()
    url = login_page.get_post_login_url()
    assert "inventory.html" in url


@pytest.mark.SANITY
def test_invalid_username_and_password(login_page):
    login_page.goto(ApplicationUrl.SAUCE_DEMO)
    error_message = login_page.login_to_sauce_demo("John", "Doe", error_message=True)
    assert error_message == "Epic sadface: Username and password do not match any user in this service"

# def test_invalid_username(page:Page):
#     login_page = LoginPage(page)
#     login_page.goto(ApplicationUrl.SAUCE_DEMO)
#     login_page.login_to_sauce_demo()
