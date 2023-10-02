from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutOverview(BasePage):
    __inventory_item = '.inventory_item_name'
    __total_price = '[class="summary_info_label summary_total_label"]'
    __finish_locator = '#finish'

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def get_over_view_list_items(self):
        return self.get_order_of_items(self.__inventory_item)

    def get_total_price(self):
        return self.get_inner_text(self.__total_price)

    def click_finish(self):
        self.click(self.__finish_locator)