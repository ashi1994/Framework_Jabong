import unittest
import time
from selenium import webdriver
import Config
import logging
from datetime import datetime
import sys
import os

class Initilization(unittest.TestCase):
    dir = os.path.dirname(__file__)
    path = dir[:len(dir)-15]
    logging.basicConfig(level=logging.INFO,filename = path+"Report\Logs\Test.log")

    def setUp(self):
        if Config.Browser.lower() == 'Firefox'.lower():
            self.driver = webdriver.Firefox()
            logging.info('Firefox browser launched.')

        elif Config.Browser.lower() == 'Chrome'.lower():
            chromeDriver = "D:\CBT_Automation\Python\Workspace_Python\Jabong\chromedriver.exe"
            self.driver = webdriver.Chrome(chromeDriver)
            logging.info('Chrome browser launched.')
        else:
            ieDriver = "D:\CBT_Automation\Python\Workspace_Python\Jabong\IEDriverServer.exe"
            self.driver = webdriver.Ie
        #self.driver = webdriver.Firefox()
        logging.info('Inside Setup method')
        self.driver.get(Config.URL)
        logging.info('Jabong Application Launched.')
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.implicitly_wait(20)

    def tearDown(self):
        logging.info("Inside TearDown Method.")
        self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()