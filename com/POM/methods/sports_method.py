from com.POM.locators.sports_loc import *
import time
import logging

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class Sport(BasePage):

    def buy_jerseys(self):
        element = self.driver.find_element(*SportsLoc.JERSEYS)
        element.click()
        time.sleep(2)

