from selenium.webdriver.common.by import By
from ..locators.mainPageLocators import MainPageLocators

class SearchPageLocators(MainPageLocators):

    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_HEADER_ROW = (By.XPATH, "//div[@class='search__header-row']/div")
    SEARCH_INFO_COLUMN = (By.XPATH, ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Info')]")
    SEARCH_SHOP_COLUMN = (By.XPATH, ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Shop')]")
    SEARCH_FEATURED_COLUMN = (By.XPATH, ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Featured')]")
