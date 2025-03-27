import unittest
from test_folder.tests.testBasePage import TestBasePage
from test_folder.pageObjects.mainPage import MainPage
from test_folder.constants import URL

class TestMainPage(TestBasePage):

    '''
    def setUp(self):
        # super().setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.accept_cookies()
    '''
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.main_page = MainPage(cls.driver)
        cls.main_page.accept_cookies()

    def test_GoToGeneralPageByLogo(self):
        self.main_page.click_logo_button()
        self.assertEqual(self.driver.current_url, URL)
        self.assertTrue(self.main_page.is_title_match(), 'Title value is wrong')

    '''
    def tearDown(self):
        super().tearDown()
    '''

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()

if __name__ == '__main__':
    unittest.main()