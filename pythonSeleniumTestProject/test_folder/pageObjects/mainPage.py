from selenium.webdriver.common.by import By
from ..locators.mainPageLocators import MainPageLocators
from test_folder.tests.testBasePage import TestBasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# a Class to keep General page objects  --> !!!Page Object Pattern!!!

class MainPage(TestBasePage):
    """ The MainPage is inherited from a TestBasePage"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    """Single component interaction"""

    def accept_cookies(self):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, ".//a[@aria-label='allow cookies']")))
        element.click()

    def click_logo_button(self):
        # element = self.wait.until(EC.presence_of_element_located(*GeneralPageLocators.MAIN_PAGE_LOGO_BUTTON))
        element = self.driver.find_element(*MainPageLocators.MAIN_PAGE_LOGO_BUTTON)
        element.click()

    def go_to_footwear(self):
        element = self.driver.find_element(*MainPageLocators.FOOTWEAR_BUTTON)
        element.click()

    def go_to_menswear(self):
        element = self.driver.find_element(*MainPageLocators.MENSWEAR_BUTTON)
        element.click()

    def go_to_finalSale(self):
        element = self.driver.find_element(*MainPageLocators.FINAL_SALE_BUTTON)
        element.click()

    def go_to_search(self):
        button = self.wait.until(EC.presence_of_element_located((By.XPATH, ".//button/span[@class='header-extensive-menu__button-label'][contains(text(),'Search')]")))
        self.driver.execute_script("arguments[0].click();", button)

    def go_to_service(self):
        element = self.driver.find_element(*MainPageLocators.SERVICE_BUTTON)
        element.click()

    def go_to_MyAccount(self):
        element = self.driver.find_element(*MainPageLocators.MY_ACCOUNT_BUTTON)
        element.click()

    def go_to_Cart(self):
        element = self.driver.find_element(*MainPageLocators.CART_BUTTON)
        element.click()

    """Page functionality"""
    def is_title_match(self):
        return "ETQ Amsterdam Online Store - Wardrobe Essentials for Men" in self.driver.title

    def go_To_Main_Menu(self):
        element = self.driver.find_element(*MainPageLocators.MAIN_PAGE_LOGO_BUTTON)
        element.click()