from com.POM.locators.men_loc import *
import time
import logging

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class Clothing(BasePage):

    def buy_suits_blazers(self):
        element = self.driver.find_element(*MenLoc.SUITE_BLAZER)
        element.click()
        time.sleep(2)