from com.POM.methods.home_method import *
from com.POM.methods.men_method import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from com.generic_lib.initilization import *

class WindowHandling(Initilization):

    def test_window_handling(self):
        element = self.driver.find_element(*HomeLoc.SALE_SECTION)
        actionChain = ActionChains(self.driver)
        print ('now down at action chain')
        actionChain.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        windowhandels = self.driver.window_handles
        time.sleep(2)
        self.driver.switch_to_window(windowhandels[1])
        title = self.driver.title
        print (title)
        assert "Official Jabong Coupons, Online Sale Offers, Discount Deals" in self.driver.title
        print ('assert is passed')