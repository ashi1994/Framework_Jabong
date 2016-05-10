import time
#from pyrobot import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class ScriptDownload():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://www.seleniumhq.org/download")
    time.sleep(2)
    driver.find_element_by_xpath("//td[text()='Java']//..//a[text()='Download']").click()
    time.sleep(2)
    #robot = Robot()
    #robot.press_and_release(Keys.enter)
    driver.close()

    print ('Its downloaded')

class ScriptHandling():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://www.google.com")
    driver.execute_script("window.alert('This is window alert.');")
    time.sleep(2)
    driver.switch_to.alert.accept()
    print ('Alert is accepeted')
    driver.close()

class JavaScriptExecutor():
    driver = webdriver.Firefox()
    driver.get("http://www.w3schools.com/html/html_headings.asp")
    driver.maximize_window()
    time.sleep(2)
    element = driver.execute_script("document.getElementsByClassName('w3-btn w3-margin-bottom')[1]")
    element.click()
    #actionChain = ActionChains(driver)
    #windowhandels = self.driver.window_handles
    driver.close()