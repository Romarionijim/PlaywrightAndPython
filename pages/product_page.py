from playwright.sync_api import Page
from pages.base_page import BasePage


class ProductPage(BasePage):
    _product_list = '[class="inventory_item"]'
    _list_items = '[class="inventory_item_name"]'
    _cart = '[class="shopping_cart_badge"]'
    _cart_basket = ".shopping_cart_link"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def choose_product_from_list(self, product_name: str):
        product_list = self.page.locator(self._product_list).all()
        for product in product_list:
            product_inner_text = product.inner_text()
            if product_inner_text.__contains__(product_name):
                button = product.locator("button")
                button.click()
                remove_attribute = button.get_attribute("name")
                return remove_attribute

    def choose_product_by_name(self, prod: str):
        product = self.page.locator(self._list_items)
        self.click(product.filter(has_text=prod))

    def get_shopping_cart_items(self):
        cart = self.page.locator(self._cart)
        return cart.inner_text()

    def click_on_cart_basket(self):
        self.click(self._cart_basket)