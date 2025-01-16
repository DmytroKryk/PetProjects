'''
import unittest
from tests.test_login import TestLogin
from tests.test_cart import TestCart

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLogin))
    suite.addTest(unittest.makeSuite(TestCart))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
'''