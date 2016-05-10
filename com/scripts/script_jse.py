import time
from selenium import webdriver

class JavaScriptExecutor():
    driver = webdriver.Firefox()
    driver.get("http://www.w3schools.com/html/html_headings.asp")

    element = driver.execute_script("document.getElementsByClassName('w3-btn w3-margin-bottom')[0].click()")
   # actionChain = ActionChains(driver)
    windowhandels =  driver.window_handles
    print (windowhandels)
    driver.switch_to_window(windowhandels[1])
    print ('Now on Child Window')
    time.sleep(3)
  #  robot = Robot()
    driver.close()
    print ('Closed Child Window')
    time.sleep(3)
    driver.switch_to_window(windowhandels[0])
    print ('Closed Parent Window')
    driver.close()