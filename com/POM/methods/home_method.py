from com.generic_lib.initilization import *
from com.generic_lib.excel_sheet import *
from selenium.webdriver.common.action_chains import ActionChains
from com.POM.locators.home_loc import *
import time
import logging

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):

    def navigate_men(self):
        element = self.driver.find_element(*HomeLoc.MEN_SECTION)
        element.click()
        time.sleep(2)

    def navigate_sports(self):
        element = self.driver.find_element(*HomeLoc.SPORTS_SECTION)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)

    def navigate_signin_page(self):
        element = self.driver.find_element(*HomeLoc.SIGNIN_LINK)
        element.click()

