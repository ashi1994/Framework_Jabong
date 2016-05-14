import unittest
import time
from selenium import webdriver
import os
import subprocess
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.alert import Alert
class Example():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.gmail.com")
    print (driver.title)
    time.sleep(4)
    driver.find_element_by_xpath("//input[@type='email']").send_keys("ashitestmail@gmail.com")
    driver.find_element_by_xpath("//input[@id='next']").click()
    time.sleep(4)
    driver.find_element_by_xpath("//input[@id='Passwd']").send_keys("researcher")
    driver.find_element_by_xpath("//input[@id='signIn']").click()
    time.sleep(4)
    driver.find_element_by_xpath("//div[text()='COMPOSE']").click()
    time.sleep(4)
    driver.find_element_by_xpath("//div[@data-tooltip='Attach files']").click()

    time.sleep(4)
    os.popen(r'"D:\CBT_Automation\Ashish\AutoIt_Script\AutoIt_Script_to_FileUpload.exe"')
    time.sleep(4)
