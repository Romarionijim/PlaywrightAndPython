from playwright.sync_api import Page
from enums.Enums import ApplicationUrl
from enums.navigation_enums import NavigationEnum


class BasePage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, url: ApplicationUrl):
        self.page.goto(url.value)

    def click(self, locator):
        if isinstance(locator, str):
            self.page.locator(locator).click()
        else:
            locator.click()

    def fill_text(self, locator, text: str):
        self.page.locator(locator).fill(text)

    def get_inner_text(self, locator):
        return self.page.locator(locator).inner_text()

    def get_input_value(self, locator):
        return self.page.locator(locator).input_value()

    def get_current_url(self):
        url = self.page.url
        return url

    def get_order_of_items(self, locator):
        arr: list = []
        items = self.page.locator(locator).all()
        for i in range(len(items)):
            item_inner_text = items[i].inner_text()
            arr.append(item_inner_text)
        return arr

    def get_column_index_by_name(self, locator, text):
        columns = self.page.locator(locator).all()
        for i in range(len(columns)):
            column_inner_text = columns[i].inner_text()
            if column_inner_text == text:
                return i

    def get_order_of_cell_values(self, locator, columname):
        arr: list = []
        rows = self.page.locator(locator).all()
        column = self.get_column_index_by_name(locator, columname)
        for row in rows:
            cell = row.locator('td').nth(column)
            cell_inner_text = cell.inner_text()
            arr.append(cell_inner_text)
        return arr

    def get_table_cell_value(self, locator, rowtext: str, columnname: str):
        row = self.page.locator(locator, has_text=rowtext)
        column = self.get_column_index_by_name(locator, columnname)
        cell_value = row.locator('td').nth(column)
        cell_inner_text = cell_value.inner_text()
        return cell_inner_text

    # def get_input_fields_values(self, locator):
    #     input_fields_order:list = []
    #     fields = self.page.locator(locator).all()
    #     for i in range(len(fields)):
    #         field_inputs = fields[i]
    #         if field_inputs.evaluate(lambda e: e.tag_nma)
