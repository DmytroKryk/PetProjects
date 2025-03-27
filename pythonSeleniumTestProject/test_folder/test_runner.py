import unittest
from tests.test_MainPage import TestMainPage
from tests.test_SearchPage import TestSearchPage

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMainPage))
    suite.addTest(unittest.makeSuite(TestSearchPage))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)