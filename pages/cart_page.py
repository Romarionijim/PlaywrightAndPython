from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):
    __basket_items = '.cart_item'
    __product_name = '.inventory_item_name'
    __item_quantity = '.cart_quantity'
    __item_price = '.inventory_item_price'
    __continue_shopping = '#continue-shopping'
    __checkout_locator = '#checkout'

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def count_basket_items(self):
        items = self.page.locator(self.__basket_items)
        items_count = items.count()
        return items_count

    def return_order_of_items_in_cart(self):
        return self.get_order_of_items(self.__product_name)

    def remove_item_from_cart(self, item_name: str):
        item = self.page.locator(self.__basket_items, has_text=item_name)
        remove_button = item.locator('button')
        self.click(remove_button)

    def get_item_quantity(self, item_name: str):
        item = self.page.locator(self.__basket_items, has_text=item_name)
        quantity = item.locator(self.__item_quantity).inner_text()
        return quantity

    def get_item_price(self, item_name: str):
        item = self.page.locator(self.__basket_items, has_text=item_name)
        price = item.locator(self.__item_price).inner_text()
        return price

    def continue_shopping(self):
        self.click(self.__continue_shopping)

    def click_checkout(self):
        self.click(self.__checkout_locator)