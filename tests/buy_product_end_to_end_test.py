from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.checkout_overview import CheckoutOverview
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.order_completion import OrderCompletion
from enums.Enums import ApplicationUrl
from utils.faker import Randomizer


def test_buy_product_and_checkout(page: Page):
    login_page = LoginPage(page)
    cart_page = CartPage(page)
    product_page = ProductPage(page)
    checkout_overview = CheckoutOverview(page)
    checkout_step_one = CheckoutStepOnePage(page)
    order_completion = OrderCompletion(page)

    login_page.goto(ApplicationUrl.SAUCE_DEMO)
    login_page.login_to_sauce_demo()

    remove_btn = product_page.choose_product_from_list("Sauce Labs Bolt T-Shirt")
    assert "remove" in remove_btn
    remove_btn2 = product_page.choose_product_from_list("Sauce Labs Backpack")
    assert "remove" in remove_btn2
    
    items_count = product_page.get_shopping_cart_items()
    assert items_count == "2"
    product_page.click_on_cart_basket()

    basket_items = cart_page.count_basket_items()
    assert basket_items == 2
    order = cart_page.return_order_of_items_in_cart()
    assert order == ["Sauce Labs Bolt T-Shirt", "Sauce Labs Backpack"]

    bolt_shirt = cart_page.get_item_quantity("Sauce Labs Bolt T-Shirt")
    assert bolt_shirt == "1"

    back_pack = cart_page.get_item_quantity("Sauce Labs Backpack")
    assert back_pack == "1"

    cart_page.click_checkout()

    checkout_step_one.fill_checkout_details(Randomizer.generate_Random_name(), Randomizer.generate_random_lastname(),
                                            Randomizer.generate_random_address())
    checkout_step_one.click_continue()

    list_items = checkout_overview.get_over_view_list_items()
    assert list_items == ["Sauce Labs Bolt T-Shirt", "Sauce Labs Backpack"]

    total_price = checkout_overview.get_total_price()
    assert total_price == "Total: $49.66"

    checkout_overview.click_finish()

    completion = order_completion.get_order_confirmation()
    assert completion == "Thank you for your order!"