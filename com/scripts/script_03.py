from com.generic_lib.initilization import *
from com.generic_lib.listener import *
from com.POM.methods.home_method import *
from com.POM.methods.men_method import *
from com.POM.methods.sports_method import *
from selenium.common.exceptions import *
import logging
import traceback

class Script03_Men(Initilization):
    global testCaseId
    def test_03_buy_blazers(self):
        # global testCaseId
        testCaseId = 'TestCase_03'
        test_method_name = self._testMethodName
        try:
            home_page = HomePage(self.driver)
            clothing = Clothing(self.driver)

            logging.info('Now in Men Script')
            home_page.navigate_men()
            clothing.click_suits_blazers()
            clothing.scroll_down()
            clothing.click_filter_slim()
            clothing.open_blazer()
            clothing.select_size()
            clothing.click_add_to_bag()
            clothing.click_bag_icon()
            clothing.click_remove_button()
            logging.info(testCaseId + "=" + "Pass")


        except WebDriverException:
            logging.error('Exception raised in method - ' + test_method_name)
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(
                Initilization.path + "Report\Screenshots\\" + test_method_name + "-" + now + ".png")
            traceback.print_exc()
            logging.info(testCaseId + "=" + "Fail")
            raise WebDriverException
