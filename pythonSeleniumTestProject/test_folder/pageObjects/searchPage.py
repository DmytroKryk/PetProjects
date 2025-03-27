from selenium.common import TimeoutException
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
        # iframe = self.driver.find_element(By.NAME, "web-pixel-sandbox-CUSTOM-152764797-LAX-740c64e3w77d0d2c6pffaaa8c0m859bd135")
        iframe = self.driver.find_element(By.XPATH, ".//iframe[@height=0][@width=0][1]")
        self.driver.switch_to.frame(iframe)
        # self.driver.switch_to.frame("web-pixel-sandbox-CUSTOM-152764797-LAX-740c64e3w77d0d2c6pffaaa8c0m859bd135")
        # self.driver.switch_to.frame("web-pixel-sandbox-CUSTOM-98238802-LAX-740c64e3w77d0d2c6pffaaa8c0m859bd135")

    def custom_wait(self, webElement):
        self.webElement = webElement
        return self.wait.until(EC.presence_of_element_located(webElement))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def input_data_to_search(self, input_value):
        self.input_value = input_value
        element = self.wait.until(EC.presence_of_element_located(SearchPageLocators.SEARCH_INPUT))
        element.clear()
        element.send_keys(self.input_value)

    def press_the_enter(self):
        element = self.wait.until(EC.presence_of_element_located(SearchPageLocators.SEARCH_INPUT))
        element.send_keys(Keys.RETURN)

    def get_search_header_row_text(self):
        element = self.wait.until(EC.presence_of_element_located(SearchPageLocators.SEARCH_HEADER_ROW))
        return element.text

    def get_search_placeholder_value(self):
        element = self.wait.until(EC.presence_of_element_located(SearchPageLocators.SEARCH_INPUT))
        return element.get_attribute("placeholder")

    def is_info_column_present(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_INFO_COLUMN).is_displayed()

    def is_shop_column_present(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_SHOP_COLUMN).is_displayed()

    def is_featured_column_present(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_FEATURED_COLUMN).is_displayed()

    def get_list_of_rows_from_info_block(self):
        try:
            list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                        ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Info')]//../ul/li")))
            names = []
            if len(list) > 0:
                for i in range(len(list)):
                    link_text = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                            ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Info')]//../ul/li[" + str(
                                                                                i + 1) + "]/a"))).text
                    names.append(link_text)

            return names

        except TypeError as error:
            print('ERROR: The Info Block is empty or not found! More details: ', error)

    def get_list_of_rows_from_shop_block(self):
        try:
            list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                        ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Shop')]//../ul/li")))
            names = []
            if len(list) > 0:
                for i in range(len(list)):
                    link_text = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                            ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Shop')]//../ul/li[" + str(
                                                                                i + 1) + "]/a"))).text
                    names.append(link_text)

            return names

        except TypeError as error:
            print('ERROR: The Shop Block is empty or not found! More details: ', error)

    def get_list_of_rows_from_featured_block(self):
        try:
            list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                        ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Featured')]//../ul/li")))
            names = []
            if len(list) > 0:
                for i in range(len(list)):
                    link_text = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                            ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Featured')]//../ul/li[" + str(
                                                                                i + 1) + "]/a"))).text
                    names.append(link_text)

            return names

        except TypeError as error:
            print('ERROR: The Featured Block is empty or not found! More details: ', error)

    def click_on_clear_button(self):
        element = self.wait.until(EC.element_to_be_clickable(SearchPageLocators.SEARCH_CLEAR_BUTTON))
        element.click()

    def is_result_products_column_present(self):
        element = self.wait.until(EC.visibility_of_element_located(SearchPageLocators.SEARCH_RESULT_PRODUCTS_COLUMN))
        return element.is_displayed()

    def is_result_collections_column_present(self):
        element = self.wait.until(EC.presence_of_element_located(SearchPageLocators.SEARCH_RESULT_COLLECTIONS_COLUMN))
        return element.is_displayed()

    def is_result_info_column_present(self):
        element = self.wait.until(EC.presence_of_element_located(SearchPageLocators.SEARCH_RESULT_INFO_COLUMN))
        return element.is_displayed()

    def list_of_product_search_result(self):
        elements = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, ".//div[@class='header-overlay-search__inner']/div/div[h3[contains(., 'Products')]]/div/a")))
        return len(elements)

    def get_list_of_collection_search_result(self):
        try:
            list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                        ".//div[@class='header-overlay-search__inner']/div/div[h3[contains(., 'Collections')]]/div/div")))
            names = []
            if len(list) > 0:
                for i in range(len(list)):
                    link_text = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                            ".//div[@class='header-overlay-search__inner']/div/div[h3[contains(., 'Collections')]]/div/div[" + str(
                                                                                i + 1) + "]/a"))).text
                    names.append(link_text)

            return names

        except TypeError as error:
            print('ERROR: The Collection search result is empty or not found! More details: ', error)

    def get_list_of_info_search_result(self):
        try:
            list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                        ".//div[@class='header-overlay-search__inner']//div[@class='search-results__col js-search-results-col'][h3[contains(., 'Info')]]/div/div")))
            names = []
            if len(list) > 0:
                for i in range(len(list)):
                    link_text = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                            ".//div[@class='header-overlay-search__inner']//div[@class='search-results__col js-search-results-col'][h3[contains(., 'Info')]]/div/div[" + str(
                                                                                i + 1) + "]/a"))).text
                    names.append(link_text)

            return names

        except TypeError as error:
            print('ERROR: The Info search result is empty or not found! More details: ', error)

    def get_coll_products_count(self):
        element = self.wait.until(EC.visibility_of_element_located((SearchPageLocators.COLLECTION_PRODUCTS_COUNT)))
        return element.text

    def get_pre_search_result_info(self):
        element = self.wait.until(EC.visibility_of_element_located((SearchPageLocators.PRE_SEARCH_RESULT_INFO)))
        return element.text

    def get_list_of_product_pre_search_result(self):
        try:
            list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                        ".//div[@class='header-overlay-search__inner']/div/div[h3[contains(., 'Products')]]/div/a")))
            names = []
            if len(list) > 0:
                for i in range(len(list)):
                    link_text = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                            ".//div[@class='header-overlay-search__inner']/div/div[h3[contains(., 'Products')]]/div/a[" + str(i + 1) + "]"))).text
                    names.append(link_text)

            return names

        except TypeError as error:
            print('ERROR: The Product pre-search result is empty or not found! More details: ', error)

    def go_to_all_searched_results(self):
        self.wait.until(EC.element_to_be_clickable((SearchPageLocators.SHOW_ALL_RESULTS_BUTTON))).click()

    def get_list_of_product_search_result(self):
        try:
            list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                        ".//section[@class='search__grid animate-in-view js-collection-products-grid js-product-item-list']/div")))
            names = []
            if len(list) > 0:
                for i in range(len(list)):
                    link_text = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                            ".//section[@class='search__grid animate-in-view js-collection-products-grid js-product-item-list']/div[" + str(i + 1) + "]/a/div[2]/p[1]"))).text
                    names.append(link_text)

            return names

        except TypeError as error:
            print('ERROR: The Product search result is empty or not found! More details: ', error)

    def switch_searched_results_to_grid(self):
        self.driver.find_element(*SearchPageLocators.GRID_SWITCHING_TO_GRID_BUTTON).click()

    def switch_searched_results_to_list(self):
        self.wait.until(EC.element_to_be_clickable((SearchPageLocators.GRID_SWITCHING_TO_LIST_BUTTON))).click()

    """ FILTER & SORT"""

    def go_to_filter_and_sort(self):
        self.wait.until(EC.element_to_be_clickable((SearchPageLocators.FILTER_AND_SORT_BUTTON))).click()

    def get_sortBy_values(self):
        try:
            number_of_values = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                        ".//div[@class='filters__filter filter'][div/h3[contains(.,'Sort by')]]/div[2]/div[@class='filter__options']/label")))
            sortBy = []
            if len(number_of_values) > 0:
                for i in range(len(number_of_values)):
                    value = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                            ".//div[@class='filters__filter filter'][div/h3[contains(.,'Sort by')]]/div[2]/div[@class='filter__options']/label[" + str(i + 1) + "]/span[2]"))).text
                    sortBy.append(value)

            return sortBy

        except TypeError as error:
            print('ERROR: SortBy list is empty or not found! More details: ', error)

    def get_Style_values(self):
        try:
            number_of_values = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                    ".//div[@class='filters__filters js-filters-filters']/div[@data-key='filter.p.m.product.style'][div/h3[contains(., 'Style')]]/div[2]/div/label")))
            stylies = []
            if len(number_of_values) > 0:
                for i in range(len(number_of_values)):
                    value = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                        ".//div[@class='filters__filters js-filters-filters']/div[@data-key='filter.p.m.product.style'][div/h3[contains(., 'Style')]]/div[2]/div/label[" + str(i + 1) + "]/span"))).text
                    stylies.append(value)

            return stylies

        except TypeError as error:
            print('ERROR: Style value list is empty or not found! More details: ', error)

    def get_Color_values(self):
        try:
            number_of_values = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                    ".//div[@class='filters__filters js-filters-filters']/div[@data-key='filter.p.m.product.color_filter'][./div/h3[contains(., 'Colour')]]/div[2]/div/label")))
            colors = []
            if len(number_of_values) > 0:
                for i in range(len(number_of_values)):
                    value = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                        ".//div[@class='filters__filters js-filters-filters']/div[@data-key='filter.p.m.product.color_filter'][./div/h3[contains(., 'Colour')]]/div[2]/div/label[" + str(i + 1) + "]/span[2]"))).text
                    colors.append(value)

            return colors

        except TypeError as error:
            print('ERROR: Color list is empty or not found! More details: ', error)

    def get_Size_values(self):
        try:
            number_of_values = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                    ".//div[@class='filters__filters js-filters-filters']/div[@data-key='filter.v.option.size - clothing'][./div/h3[contains(., 'Size')]]/div[2]/div/label")))
            sizes = []
            if len(number_of_values) > 0:
                for i in range(len(number_of_values)):
                    value = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                        ".//div[@class='filters__filters js-filters-filters']/div[@data-key='filter.v.option.size - clothing'][./div/h3[contains(., 'Size')]]/div[2]/div/label[" + str(i + 1) + "]/span"))).text
                    sizes.append(value)

            return sizes

        except TypeError as error:
            print('ERROR: Size list is empty or not found! More details: ', error)

    def get_Material_values(self):
        try:
            number_of_values = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                    ".//div[@class='filters__filters js-filters-filters']/div[@data-key='filter.p.m.general.material'][./div/h3[contains(., 'Material')]]/div[2]/div/label")))
            materials = []
            if len(number_of_values) > 0:
                for i in range(len(number_of_values)):
                    value = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                        ".//div[@class='filters__filters js-filters-filters']/div[@data-key='filter.p.m.general.material'][./div/h3[contains(., 'Material')]]/div[2]/div/label[" + str(i + 1) + "]/span[2]"))).text
                    materials.append(value)

            return materials

        except TypeError as error:
            print('ERROR: Material list is empty or not found! More details: ', error)

    def click_show_button(self):
        self.wait.until(EC.element_to_be_clickable((SearchPageLocators.SHOW_BUTTON))).click()

    def sortBy(self, text):
        self.text = text
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='filters__filter filter'][div/h3[contains(.,'Sort by')]]/div[2]/div[@class='filter__options']/label[span[2][contains(.,'" + self.text + "')]]"))).click()

    def get_selected_Style(self):
        try:
            selectedStyle = self.wait.until(EC.presence_of_element_located(SearchPageLocators.SELECTED_STYLE)).text
        except:
            return 'Style is not selected'

        return selectedStyle

    def filterByStyle(self, index):
        self.index = index
        self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                    "//div[div/h3[contains(.,'Style')]]/div[2]/div[@class='filter__options']/label[" + self.index + "]/span[1]"))).click()

    def get_selected_SortBy(self):
        selectedSortBy = self.wait.until(EC.presence_of_element_located(SearchPageLocators.SELECTED_SORT_BY)).text
        return selectedSortBy

    def filterByColor(self, color):
        self.color = color
        self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                    "//div[div/h3[contains(.,'Colour')]]/div[2]/div[@class='filter__options']/label[span[2][contains(.,'" + self.color + "')]]"))).click()

    def get_filtered_color(self):
        try:
            selectedColor = self.wait.until(EC.presence_of_element_located(SearchPageLocators.SELECTED_COLOR)).text
        except:
            return 'The color is not selected'

        return selectedColor

    def get_filtered_size(self):
        try:
            selectedSize = self.wait.until(EC.presence_of_element_located(SearchPageLocators.SELECTED_SIZE)).text

        except:
            return 'The Size value is not selected'

        return selectedSize

    def filterBySize(self, size):
        self.size = size
        self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                    "//div[div/h3[contains(.,'Size')]]/div[2]/div[@class='filter__options']/label[span[1][contains(.,'" + self.size + "')]]"))).click()

    def get_filtered_material(self):
        try:
            selectedMaterial = self.wait.until(EC.presence_of_element_located(SearchPageLocators.SELECTED_MATERIAL)).text
        except:
            return 'Material is not selected'

        return selectedMaterial

    def filterByMaterial(self, index):
        self.index = index
        self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                    "//div[div/h3[contains(.,'Material')]]/div[2]/div[@class='filter__options']/label[" + self.index + "]/span[1]"))).click()

    def get_active_filters(self):
        try:
            number_of_values = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                    ".//button[@class='search__active-filter js-active-filter-remove']/span")))
            activeFilters = []
            if len(number_of_values) > 0:
                for i in range(len(number_of_values)):
                    value = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                        ".//button[@class='search__active-filter js-active-filter-remove'][" + str(i + 1) + "]/span"))).text
                    activeFilters.append(value)

        except:
            return 'There is no active filter'

        return activeFilters

    def remove_all_active_filters(self):
        element = self.wait.until(EC.presence_of_element_located(SearchPageLocators.SEARCH_HEADER_ROW))
        element.click()
