from com.POM.locators.men_loc import *
import time
from selenium.webdriver.common.action_chains import ActionChains
import logging

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class Clothing(BasePage):

    def click_suits_blazers(self):
        element = self.driver.find_element(*MenLoc.SUITE_BLAZER)
        element.click()
        logging.info('Clicked on Suits and Blazers in Clothing category.')
        time.sleep(2)

    def scroll_down(self):
        element = self.driver.find_element(*MenLoc.FILTER_SLIM)
        ActionChains(self.driver).move_to_element(element).perform()
        logging.info('Scrolled down to Filter out products.')
        time.sleep(2)

    def click_filter_slim(self):
        element = self.driver.find_element(*MenLoc.FILTER_SLIM)
        element.click()
        logging.info('Clicked on Slim in Filter category.')
        time.sleep(2)

    def open_blazer(self):
        element = self.driver.find_element(*MenLoc.SUITE_02_IMAGE)
        element.click()
        logging.info("Product opened to see it's details.")
        time.sleep(2)

    def select_size(self):
        select_size = self.driver.find_element(*MenLoc.SELECT_SIZE)
        select_size.click()
        logging.info('Size is selected for the product.')
        time.sleep(2)

    def click_add_to_bag(self):
        add_to_bag_button = self.driver.find_element(*MenLoc.ADD_TO_BAG)
        add_to_bag_button.click()
        logging.info('Clicked to add product in Cart')
        time.sleep(10)

    def click_bag_icon(self):
        bag_icon = self.driver.find_element(*MenLoc.BAG_ICON)
        # ActionChains.move_to_element(bag_icon).perform()
        bag_icon.click()
        logging.info('Clicked on Bag icon and Product is successfully added to Cart.')
        time.sleep(5)

    def click_remove_button(self):
        remove_button = self.driver.find_element(*MenLoc.REMOVE_BUTTON)
        remove_button.click()
        logging.info('Product removed from Cart.')
        time.sleep(2)