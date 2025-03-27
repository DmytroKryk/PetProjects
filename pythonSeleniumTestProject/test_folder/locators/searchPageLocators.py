from selenium.webdriver.common.by import By
from ..locators.mainPageLocators import MainPageLocators

class SearchPageLocators(MainPageLocators):

    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_HEADER_ROW = (By.XPATH, "//div[@class='search__header-row']/div")
    SEARCH_INFO_COLUMN = (By.XPATH, ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Info')]")
    SEARCH_SHOP_COLUMN = (By.XPATH, ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Shop')]")
    SEARCH_FEATURED_COLUMN = (By.XPATH, ".//form[@class='header-overlay-search__form']//following-sibling::div[@class='search-navigations js-search-navigations'][1]//h3[contains(text(),'Featured')]")
    SEARCH_CLEAR_BUTTON = (By.CLASS_NAME, "header-overlay-search__clear js-search-clear")
    SEARCH_RESULT_PRODUCTS_COLUMN = (By.XPATH,".//div[@class='header-overlay-search__inner']/div/div/h3[contains(., 'Products')]")
    SEARCH_RESULT_COLLECTIONS_COLUMN = (By.XPATH, ".//div[@class='header-overlay-search__inner']/div/div/h3[contains(., 'Collections')]")
    SEARCH_RESULT_INFO_COLUMN = (By.XPATH, ".//div[@class='header-overlay-search__inner']/div/div/h3[contains(., 'Info')][1]")
    COLLECTION_PRODUCTS_COUNT = (By.CLASS_NAME, "js-collection-products-count")
    PRE_SEARCH_RESULT_INFO = (By.XPATH, ".//div[@class='header-overlay-search__inner']/div/div[@class='search-results__no-results js-search-results-none']")
    SHOW_ALL_RESULTS_BUTTON = (By.LINK_TEXT, "Show all results")
    GRID_SWITCHING_TO_GRID_BUTTON = (By.XPATH,".//div[@class='search__grid-switch']/button[@class='search__grid-switch-type js-collection-switch-type'][@data-type='grid']")
    GRID_SWITCHING_TO_LIST_BUTTON = (By.XPATH, ".//div[@class='search__grid-switch']/button[@class='search__grid-switch-type js-collection-switch-type'][@data-type='list']")
    """ FILTER & SORT"""
    FILTER_AND_SORT_BUTTON = (By.XPATH, ".//button[@class='search__filter-trigger js-popup-trigger']")
    SHOW_BUTTON = (By.XPATH, ".//button[contains(.,'Show')]")
    SELECTED_SORT_BY = (By.XPATH, "//div[@class='filters__filter filter'][div/h3[contains(.,'Sort by')]]/div[2]/div[@class='filter__options']/label[input[@checked]]/span[2]")
    SELECTED_STYLE = (By.XPATH, "//div[div/h3[contains(.,'Style')]]/div[2]/div[@class='filter__options']/label[input[@checked]]/span[1]")
    SELECTED_COLOR = (By.XPATH, "//div[div/h3[contains(.,'Colour')]]/div[2]/div[@class='filter__options']/label[input[@checked]]/span[2]")
    SELECTED_SIZE = (By.XPATH, "//div[div/h3[contains(.,'Size')]]/div[2]/div[@class='filter__options']/label[input[@checked]]/span[1]")
    SELECTED_MATERIAL = (By.XPATH, "//div[div/h3[contains(.,'Material')]]/div[2]/div[@class='filter__options']/label[input[@checked]]/span[1]")
    ACTIVE_FILERS_REMOVE_BUTTON = (By.XPATH, "//button[@class='search__active-filter js-active-filter-remove']/span[contains(.,'Remove all')]")