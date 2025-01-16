from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ..locators.searchPageLocators import SearchPageLocators
from test_folder.tests.testBasePage import TestBasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(TestBasePage):
    """ The SearcPage (actually is a PopUp window) is inherited from TestBasePage"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    """Single component interaction"""

    def switch_to_frame(self):
        iframe = self.driver.find_element(By.NAME, "web-pixel-sandbox-CUSTOM-152764797-LAX-740c64e3w77d0d2c6pffaaa8c0m859bd135")
        self.driver.switch_to.frame(iframe)
        # self.driver.switch_to.frame("web-pixel-sandbox-CUSTOM-152764797-LAX-740c64e3w77d0d2c6pffaaa8c0m859bd135")
        # self.driver.switch_to.frame("web-pixel-sandbox-CUSTOM-98238802-LAX-740c64e3w77d0d2c6pffaaa8c0m859bd135")

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def input_data_to_search(self, input):
        self.input = input
        element = self.driver.find_element(*SearchPageLocators.SEARCH_INPUT)
        element.clear()
        element.send_keys(self.input)

    def press_the_enter(self):
        element = self.driver.find_element(*SearchPageLocators.SEARCH_INPUT)
        element.send_keys(Keys.RETURN)

    def get_search_header_row_text(self):
        element = self.driver.find_element(*SearchPageLocators.SEARCH_HEADER_ROW)
        return element.text

    def get_search_placeholder_value(self):
        element = self.driver.find_element(*SearchPageLocators.SEARCH_INPUT)
        return element.get_attribute("placeholder")

    def is_info_column_present(self):
        element = self.driver.find_element(*SearchPageLocators.SEARCH_INFO_COLUMN)
        return element.is_displayed()

    def is_shop_column_present(self):
        element = self.driver.find_element(*SearchPageLocators.SEARCH_SHOP_COLUMN)
        return element.is_displayed()

    def is_featured_column_present(self):
        element = self.driver.find_element(*SearchPageLocators.SEARCH_FEATURED_COLUMN)
        return element.is_displayed()

    def get_list_of_rows_from_info_block(self):
        list = self.driver.find_elements(By.XPATH, ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Info')]//../ul/li")
        # print(f"list - ", len(list))
        names = []
        if len(list) > 0:
            for i in range(len(list)):
                link_text = self.driver.find_element(By.XPATH, ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Info')]//../ul/li["+str(i+1)+"]/a").text
                names.append(link_text)

        return names

    def get_list_of_rows_from_shop_block(self):
        list = self.driver.find_elements(By.XPATH, ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Shop')]//../ul/li")
        # print(f"list - ", len(list))
        names = []
        if len(list) > 0:
            for i in range(len(list)):
                link_text = self.driver.find_element(By.XPATH, ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Shop')]//../ul/li["+str(i+1)+"]/a").text
                names.append(link_text)

        return names

    def get_list_of_rows_from_featured_block(self):
        list = self.driver.find_elements(By.XPATH,
                                         ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Featured')]//../ul/li")
        names = []
        if len(list) > 0:
            for i in range(len(list)):
                link_text = self.driver.find_element(By.XPATH,
                                                     ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Featured')]//../ul/li[" + str(
                                                         i + 1) + "]/a").text
                names.append(link_text)

        return names
