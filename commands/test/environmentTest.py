"""
"""

import os
import unittest

from selenium import webdriver

class TestNitruxConfiguration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_isFileWithCommandsPresent(self):
        self.assertEqual(True, os.path.exists("../data"))

    def test_isSeleniumInstalled(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"
        self.driver.quit()


if __name__ == 'main':
    unittest.main()
