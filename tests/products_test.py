from pages.login_page import LoginPage
from pages.product_page import ProductPage
from playwright.sync_api import Page, expect
from enums.Enums import ApplicationUrl
import pytest


def test_choose_product(page:Page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.goto(ApplicationUrl.SAUCE_DEMO)
    login_page.login_to_sauce_demo()
    url = login_page.get_post_login_url()
    assert "inventory.html" in url
    prod = "Sauce Labs Bolt T-Shirt"
    product_page.choose_product_from_list(prod)
    items = product_page.get_shopping_cart_items()
    assert items == "1"
    expect(url)