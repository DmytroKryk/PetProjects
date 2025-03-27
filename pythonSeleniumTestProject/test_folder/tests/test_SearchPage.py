import time
import unittest
from test_folder.tests.testBasePage import TestBasePage
from test_folder.pageObjects.mainPage import MainPage
from test_folder.pageObjects.searchPage import SearchPage

class TestSearchPage(TestBasePage):

    ITEM_NAME = "TS 01 Essence regular Heavyweight White"
    ITEM_NAME_FOR_FILTERING = "TS 01 Essence regular Heavyweight"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.main_page = MainPage(cls.driver)
        cls.search_page = SearchPage(cls.driver)
        cls.main_page.accept_cookies()
        cls.driver.implicitly_wait(10)
        # cls.driver.fullscreen_window()

    '''    
    def setUp(self):
        super().setUp()
        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.main_page.accept_cookies()
    '''

    def test_SearchPlaceholderValue(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.assertEqual(self.search_page.get_search_placeholder_value(), "Start typing what you're looking for")

    def test_SearchNothing(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        time.sleep(2)   # do not remove 2 sec sleep, needed for is_info_column_present!!!
        self.assertTrue(self.search_page.is_info_column_present())
        self.search_page.input_data_to_search("")
        self.search_page.press_the_enter()
        self.assertEqual(self.search_page.get_coll_products_count(), "0 items")
        time.sleep(1)  # do not remove 1 sec sleep
        self.assertFalse(self.search_page.is_info_column_present())
        self.assertFalse(self.search_page.is_shop_column_present())
        self.assertFalse(self.search_page.is_featured_column_present())

    def test_PresenceOfInfoBlock(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        time.sleep(1)  # do not remove 1 sec sleep
        self.assertTrue(self.search_page.is_info_column_present())

    def test_PresenceOfShopBlock(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        time.sleep(1)  # do not remove 1 sec sleep
        self.assertTrue(self.search_page.is_shop_column_present())

    def test_PresenceOfFeaturedBlock(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        time.sleep(1)  # do not remove 1 sec sleep
        self.assertTrue(self.search_page.is_featured_column_present())

    def test_ListOfLinksInInfoBlock(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        listFromGUI = self.search_page.get_list_of_rows_from_info_block()
        print(listFromGUI)
        self.assertListEqual(['Shipping & Delivery', 'Returns & Exchanges', 'Size Guide', 'Product Care', 'All Topics & Customer Care'], listFromGUI)

    def test_ListOfLinksInShopBlock(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        listFromGUI = self.search_page.get_list_of_rows_from_shop_block()
        self.assertListEqual(['Shoes', 'Sneakers', 'Loafers', 'Espadrilles', 'Sandals', 'Sale'], listFromGUI)

    def test_ListOfLinksInFeaturedBlock(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        listFromGUI = self.search_page.get_list_of_rows_from_featured_block()
        self.assertListEqual(['Loafers', 'Premium Suede', 'Essence', 'Premium Nappa'], listFromGUI)

    def test_PreSearchByOneChar(self):
        input_value = "T"
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(input_value)
        self.search_page.switch_to_default_content()
        time.sleep(1)  # do not remove 1 sec sleep
        self.assertFalse(self.search_page.is_info_column_present())
        self.assertFalse(self.search_page.is_shop_column_present())
        self.assertFalse(self.search_page.is_featured_column_present())
        self.assertTrue(self.search_page.is_result_products_column_present())
        self.assertTrue(self.search_page.is_result_collections_column_present())
        self.assertTrue(self.search_page.is_result_info_column_present())
        self.assertTrue(self.search_page.list_of_product_search_result() > 0)
        collListFromGUI = self.search_page.get_list_of_collection_search_result()
        self.assertListEqual(['T-Shirts', 'Oversized T-Shirts', 'Regular T-Shirts'], collListFromGUI)
        infoListFromGUI = self.search_page.get_list_of_info_search_result()
        self.assertListEqual(['Explore - Water Zero®', 'Explore TENCEL - ECONYL', 'Help topics and customer care - Ask us anything'], infoListFromGUI)

    def test_SearchByOneChar(self):
        input_value = "P"
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(input_value)
        self.search_page.press_the_enter()
        self.assertNotEqual(self.search_page.get_coll_products_count(), "0 items", "Check search item result: ")

    def test_PreSearchNonExistentProduct(self):
        input_value = "YYY"
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(input_value)
        self.assertEqual(self.search_page.get_pre_search_result_info(), f'No results found for "'+ input_value +'"', "Check pre-search result: ")

    def test_SearchNonExistentProduct(self):
        input_value = "djfndjfjd"
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(input_value)
        self.search_page.press_the_enter()
        self.assertEqual(self.search_page.get_coll_products_count(), "0 items", "Check search item result: ")

    def test_PreSearchExistentProductByFullName(self):
        input_value = self.ITEM_NAME
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(input_value)
        self.search_page.switch_to_default_content()
        time.sleep(1)  # do not remove 1 sec sleep
        self.assertFalse(self.search_page.is_info_column_present())
        self.assertFalse(self.search_page.is_shop_column_present())
        self.assertFalse(self.search_page.is_featured_column_present())
        self.assertTrue(self.search_page.is_result_products_column_present()) # True!!!
        self.assertFalse(self.search_page.is_result_collections_column_present())
        self.assertFalse(self.search_page.is_result_info_column_present())
        self.assertTrue(self.search_page.list_of_product_search_result() > 0)
        productListFromGUI = self.search_page.get_list_of_product_pre_search_result()
        self.assertTrue('TS 01 Essence Regular Heavyweight White\nRON 430 RON 299' in productListFromGUI,
                        'Check presence of "TS 01 Essence Regular Heavyweight White\nRON 430 RON 299" in result list')
        self.assertTrue('TS 01 Essence Regular Heavyweight Off White\nRON 430 RON 299' in productListFromGUI,
                        'Check presence of "TS 01 Essence Regular Heavyweight Off White\nRON 430 RON 299" in result list')

    def test_SearchExistentProductByFullName(self):
        input_value = self.ITEM_NAME
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(input_value)
        self.search_page.go_to_all_searched_results()
        self.search_page.switch_to_default_content()
        self.assertNotEqual(self.search_page.get_coll_products_count(), "0 items", "Check search item result: ")
        serachResultsFromGUI = self.search_page.get_list_of_product_search_result()
        # self.assertListEqual(
        #     ['TS 01 Essence Regular Heavyweight White', 'TS 01 Essence Regular Heavyweight Off White'],
        #     serachResultsFromGUI)
        self.assertTrue('TS 01 Essence Regular Heavyweight White' in serachResultsFromGUI, 'Check presence of "TS 01 Essence Regular Heavyweight White" in result list')
        self.assertTrue('TS 01 Essence Regular Heavyweight Off White' in serachResultsFromGUI, 'Check presence of "TS 01 Essence Regular Heavyweight Off White" in result list')

    def test_SearchResultSwitchers(self):
        input_value = self.ITEM_NAME
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(input_value)
        self.search_page.go_to_all_searched_results()
        serachResultsFromGUIInGrid = self.search_page.get_list_of_product_search_result()
        # self.assertListEqual(
        #     ['TS 01 Essence Regular Heavyweight White', 'TS 01 Essence Regular Heavyweight Off White'],
        #     serachResultsFromGUIInGrid)
        self.assertTrue('TS 01 Essence Regular Heavyweight White' in serachResultsFromGUIInGrid,
                        'Check presence of "TS 01 Essence Regular Heavyweight White" in result list')
        self.assertTrue('TS 01 Essence Regular Heavyweight Off White' in serachResultsFromGUIInGrid,
                        'Check presence of "TS 01 Essence Regular Heavyweight Off White" in result list')
        self.search_page.switch_searched_results_to_list()
        serachResultsFromGUIInList = self.search_page.get_list_of_product_search_result()
        # self.assertListEqual(
        #     ['TS 01 Essence Regular Heavyweight White', 'TS 01 Essence Regular Heavyweight Off White'],
        #     serachResultsFromGUIInList)
        self.assertTrue('TS 01 Essence Regular Heavyweight White' in serachResultsFromGUIInList,
                        'Check presence of "TS 01 Essence Regular Heavyweight White" in result list')
        self.assertTrue('TS 01 Essence Regular Heavyweight Off White' in serachResultsFromGUIInList,
                        'Check presence of "TS 01 Essence Regular Heavyweight Off White" in result list')

    # def test_SearchBySpecialCharacters (like ! @ # $ % ^ & * ( ) - _ = + \ | [ ] { } ; : / ? . >)

    # !!! Block of Tests to check FILTER !!!

    def test_FilterAndSortBlockCheck(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(self.ITEM_NAME_FOR_FILTERING)
        self.search_page.go_to_all_searched_results()
        self.search_page.go_to_filter_and_sort()
        time.sleep(2)
        sortByGUI = self.search_page.get_sortBy_values()
        self.assertListEqual(
                ['Relevance', 'Price Low to High', 'Price High to Low'],
                sortByGUI)
        self.assertListEqual(
            ['TS 01'],
            self.search_page.get_Style_values())
        self.assertListEqual(
            ['White', 'Black', 'Green', 'Blue', 'Taupe'],
            self.search_page.get_Color_values())
        self.assertListEqual(
            ['S', 'M', 'L', 'XL'],
            self.search_page.get_Size_values())
        self.assertListEqual(
            ['Italian Fleece'],
            self.search_page.get_Material_values())

    def test_SortBy_price(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(self.ITEM_NAME_FOR_FILTERING)
        self.search_page.go_to_all_searched_results()
        self.search_page.go_to_filter_and_sort()
        self.search_page.switch_to_default_content()
        time.sleep(2) # do not remove 2 sec sleep!!!
        self.assertEqual(self.search_page.get_selected_SortBy(), 'Relevance')
        self.search_page.sortBy('Price Low to High') # possible values: Relevance, Price Low to High, Price High to Low
        time.sleep(2) # do not remove 2 sec sleep!!!
        self.assertEqual(self.search_page.get_selected_SortBy(), 'Price Low to High')
        # self.search_page.click_show_button()

    def test_FilterBy_style(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(self.ITEM_NAME_FOR_FILTERING)
        self.search_page.go_to_all_searched_results()
        self.search_page.go_to_filter_and_sort()
        self.search_page.switch_to_default_content()
        self.assertEqual(self.search_page.get_selected_Style(), 'Style is not selected')
        self.search_page.filterByStyle('1')
        self.search_page.click_show_button()
        self.assertEqual(self.search_page.get_coll_products_count(), "10 items", "Check search item result: ")
        searchResultsFromGUIInList = self.search_page.get_list_of_product_search_result()
        self.assertTrue('TS 01 Essence Regular Heavyweight Black' in searchResultsFromGUIInList,
                        'Check presence of "TS 01 Essence Regular Heavyweight Black" in result list')
        self.assertEqual(self.search_page.get_active_filters(), ['TS 01'],
                         'Comparison of active filter list: ')

    def test_FilterBy_color(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(self.ITEM_NAME_FOR_FILTERING)
        self.search_page.go_to_all_searched_results()
        self.search_page.go_to_filter_and_sort()
        self.search_page.switch_to_default_content()
        self.assertEqual(self.search_page.get_filtered_color(), 'The color is not selected')
        self.search_page.filterByColor('Black')
        self.search_page.click_show_button()
        self.assertEqual(self.search_page.get_coll_products_count(), "10 items", "Check search item result: ")
        searchResultsFromGUIInList = self.search_page.get_list_of_product_search_result()
        self.assertTrue('TS 01 Essence Regular Heavyweight Black' in searchResultsFromGUIInList,
                        'Check presence of "TS 01 Essence Regular Heavyweight Black" in result list')
        self.assertEqual(self.search_page.get_active_filters(), ['Black'], 'Comparison of active filter list: ')

    def test_FilterBy_size(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(self.ITEM_NAME_FOR_FILTERING)
        self.search_page.go_to_all_searched_results()
        self.search_page.go_to_filter_and_sort()
        self.search_page.switch_to_default_content()
        self.assertEqual(self.search_page.get_filtered_size(), 'The Size value is not selected')
        self.search_page.filterBySize('XL')
        self.search_page.click_show_button()
        self.assertEqual(self.search_page.get_coll_products_count(), "10 items", "Check search item result: ")
        searchResultsFromGUIInList = self.search_page.get_list_of_product_search_result()
        self.assertTrue('TS 01 Essence Regular Heavyweight Black' in searchResultsFromGUIInList,
                        'Check presence of "TS 01 Essence Regular Heavyweight Black" in result list')
        self.assertEqual(self.search_page.get_active_filters(), ['Size XL'], 'Comparison of active filter list: ')

    def test_FilterBy_material(self):
        self.search_page.switch_to_default_content()
        self.main_page.go_to_search()
        self.search_page.input_data_to_search(self.ITEM_NAME_FOR_FILTERING)
        self.search_page.go_to_all_searched_results()
        self.search_page.go_to_filter_and_sort()
        self.search_page.switch_to_default_content()
        self.assertEqual(self.search_page.get_filtered_material(), 'Material is not selected')
        self.search_page.filterByMaterial('1')
        self.search_page.click_show_button()
        self.assertEqual(self.search_page.get_coll_products_count(), "10 items", "Check search item result: ")
        searchResultsFromGUIInList = self.search_page.get_list_of_product_search_result()
        self.assertTrue('TS 01 Essence Regular Heavyweight Black' in searchResultsFromGUIInList,
                        'Check presence of "TS 01 Essence Regular Heavyweight Black" in result list')
        self.assertEqual(self.search_page.get_active_filters(), ['Italian Fleece'], 'Comparison of active filter list: ')

    '''
    def tearDown(self):
        super().tearDown()
    '''

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()

if __name__ == '__main__':
    unittest.main()