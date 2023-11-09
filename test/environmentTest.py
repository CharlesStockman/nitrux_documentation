"""
  Verify that the environment can execute python tests and interact with the chrome browser
"""

import unittest
import time
from selenium import webdriver


class TestNitruxConfiguration(unittest.TestCase):


    # def setUp(self):
    #     self.driver = webdriver.Chrome()

    # def tearDown(self):
    #     self.driver.quit()

    def test_selenium_environment(self):
        driver = webdriver.Chrome()
        time.sleep(2)
        driver.get("https://www.google.com")
        time.sleep(2)
        #assert self.driver.title == "Google"

        time.sleep(2)
        print("--- ", driver.title)
        driver.close()



if __name__ == 'main':
    unittest.main()
