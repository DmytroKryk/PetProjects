import time
import unittest
from selenium import webdriver
from test_folder.constants import URL

class TestBasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = webdriver.ChromeOptions()
        cls.options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(cls.options)
        cls.driver.get(URL)
        # cls.driver.fullscreen_window()

    def setUp(self):
        self.driver.get(URL)
    '''    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.driver.fullscreen_window()
    '''

    def test_url_correctness(self):
        self.driver.implicitly_wait(10)
        self.assertEqual(self.driver.current_url, URL)

    def navigate_to(self, url):
        self.driver.get(url)

    '''
    def tearDown(self):
        self.driver.quit()
    '''

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
