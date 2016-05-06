import unittest
import time
from selenium import webdriver
import Config
import logging
from datetime import datetime
import sys
import os

class Initilization(unittest.TestCase):

    logging.basicConfig(level=logging.INFO,filename = 'D:\CBT_Automation\Python\Workspace_Python\Report\Framework_Jabong\Logs\example.log')

    # def __init__(self):
    #
    #     if Config.Browser.lower() == 'Firefox'.lower():
    #
    #         self.driver = webdriver.Firefox()
    #         logging.info('Firefox browser launched.')
    #
    #     elif Config.Browser.lower() == 'Chrome'.lower():
    #         chromeDriver = "D:\CBT_Automation\Python\Workspace_Python\Jabong\chromedriver.exe"
    #         self.driver = webdriver.Chrome(chromeDriver)
    #         logging.info('Chrome browser launched.')
    #     else:
    #         ieDriver = "D:\CBT_Automation\Python\Workspace_Python\Jabong\IEDriverServer.exe"
    #         self.driver = webdriver.Ie
    #
    #     return self.driver

    def setUp(self):
        self.driver = webdriver.Firefox()
        logging.info('Inside Setup method')
        self.driver.get("http://www.jabong.com")
        logging.info('Jabong Application Launched.')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        logging.info("Inside TearDown Method.")
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot("D:\CBT_Automation\Python\Workspace_Python\Report\Framework_Jabong\Screenshots" + test_method_name + "-" + now + ".png")
            print("Screenshot done.")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()