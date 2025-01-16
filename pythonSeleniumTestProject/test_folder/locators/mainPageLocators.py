from selenium.webdriver.common.by import By

class MainPageLocators(object):

    SEARCH_INPUT = (By.XPATH, ".//a[@aria-label='allow cookies']")
    MAIN_PAGE_LOGO_BUTTON = (By.XPATH, ".//a[1]/span[@class='header__logo-inner']")

    FOOTWEAR_BUTTON = (By.XPATH, ".//a/span[@class='header-extensive-menu__button-label'][contains(text(),'Footwear')]")
    MENSWEAR_BUTTON = (By.XPATH, ".//a/span[@class='header-extensive-menu__button-label'][contains(text(),'Menswear')]")
    FINAL_SALE_BUTTON = (By.XPATH, ".//a/span[@class='header-extensive-menu__button-label'][contains(text(),'Final Sale')]")

    SEARCH_BUTTON = (By.XPATH, ".//button/span[@class='header-extensive-menu__button-label'][contains(text(),'Search')]")
    SERVICE_BUTTON = (By.XPATH, ".//button/span[@class='header-extensive-menu__button-label'][contains(text(),'Service')]")
    MY_ACCOUNT_BUTTON = (By.XPATH, ".//button/span[@class='header-extensive-menu__button-label'][contains(text(),'My account')]")
    CART_BUTTON = (By.CLASS_NAME, "header__cart")

