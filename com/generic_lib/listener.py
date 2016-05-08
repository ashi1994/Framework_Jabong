import unittest
from com.generic_lib.initilization import *
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener

class ScreenshotListener(AbstractEventListener, Initilization):

    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def on_exception(self, exception, driver):
        dir = os.path.dirname(__file__)
        path = dir[:len(dir)-15]
        screenshot_name = self.test_method_name
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        driver.get_screenshot_as_file(path+'/Screenshots/'+screenshot_name + "-" + now + ".jpg")
        driver.save_screenshot(path + '/Screenshots/' + screenshot_name + "-" + now + ".png")
        time.sleep(3)
        print("Screenshot saved as '%s'" % screenshot_name)

    def fail(self, msg=None):
        print('Inside Fail function of listener class')
