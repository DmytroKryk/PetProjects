import time
import unittest
from selenium import webdriver
from test_folder.constants import URL

class TestBasePage(unittest.TestCase):
    '''
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        # cls.driver.get("https://www.allterraincycles.co.uk")
        cls.driver.get("https://www.decathlon.pl/")
        cls.driver.fullscreen_window()
    '''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.driver.fullscreen_window()

    def test_url_correctness(self):
        self.driver.implicitly_wait(10)
        self.assertEqual(self.driver.current_url, URL)
        # time.sleep(5)

    '''
    # @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    '''

    def navigate_to(self, url):
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()
