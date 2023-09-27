from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutOverview(BasePage):
    _inventory_item = '.inventory_item_name'
    _total_price = '[class="summary_info_label summary_total_label"]'
    _finish_locator = '#finish'

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def get_over_view_list_items(self):
        return self.get_order_of_items(self._inventory_item)

    def get_total_price(self):
        return self.get_inner_text(self._total_price)

    def click_finish(self):
        self.click(self._finish_locator)