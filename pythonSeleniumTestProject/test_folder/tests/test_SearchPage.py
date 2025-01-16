import time
import unittest
from test_folder.tests.testBasePage import TestBasePage
from test_folder.pageObjects.mainPage import MainPage
from test_folder.pageObjects.searchPage import SearchPage
from test_folder.constants import URL

class TestSearchPage(TestBasePage):

    def setUp(self):
        super().setUp()
        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.main_page.accept_cookies()

    def test_SearchPlaceholderValue(self):
        time.sleep(0)
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        time.sleep(1)
        self.assertEqual(self.search_page.get_search_placeholder_value(), "Start typing what you're looking for")

    def test_SearchNothing(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        time.sleep(0)
        self.search_page.input_data_to_search("")
        time.sleep(1)
        self.search_page.press_the_enter()
        time.sleep(1)
        # print(f"result of the search - ", self.search_page.get_search_header_row_text())
        self.assertEqual(self.search_page.get_search_header_row_text(), "0 items")

    def test_PresenceOfInfoBlock(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        time.sleep(1)
        self.assertTrue(self.search_page.is_info_column_present())

    def test_PresenceOfShopBlock(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        time.sleep(1)
        self.assertTrue(self.search_page.is_shop_column_present())

    def test_PresenceOfFeaturedBlock(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        time.sleep(1)
        self.assertTrue(self.search_page.is_featured_column_present())

    def test_ListOfLinksInInfoBlock(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        time.sleep(1)
        listFromGUI = self.search_page.get_list_of_rows_from_info_block()
        self.assertListEqual(['Shipping & Delivery', 'Returns & Exchanges', 'Size Guide', 'Product Care', 'All Topics & Customer Care'], listFromGUI)

    def test_ListOfLinksInShopBlock(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        time.sleep(1)
        listFromGUI = self.search_page.get_list_of_rows_from_shop_block()
        self.assertListEqual(['Shoes', 'Sneakers', 'Loafers', 'Espadrilles', 'Sandals', 'Sale'], listFromGUI)

    def test_ListOfLinksInFeaturedBlock(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        time.sleep(1)
        listFromGUI = self.search_page.get_list_of_rows_from_featured_block()
        self.assertListEqual(['Loafers', 'Premium Suede', 'Essence', 'Premium Nappa'], listFromGUI)

        # def test_SearchBySpecialCharacters (like ! @ # $ % ^ & * ( ) - _ = + \ | [ ] { } ; : / ? . >)
        # def test_SearchByOneChar()
        # def test_NonExistentProduct()
        # def test_ExistentProduct()
        # def test_SuggestedCollections()
        # def test_SuggestedInfoBlocks()


    def tearDown(self):
        super().tearDown()

if __name__ == '__main__':
    unittest.main()