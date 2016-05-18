from com.generic_lib.initilization import *
from com.POM.methods.home_method import *

from com.POM.methods.sports_method import *
from selenium.common.exceptions import *
import traceback

from com.POM.methods.sign_in_method import *
import logging
#from com.generic_lib.listener import *


class Script02_Sports(Initilization):
    testCaseId = "TestCase_02"


    def test_02_buy_jersey(self):
        global testCaseId
        test_method_name = self._testMethodName
        try:
            home_page = HomePage(self.driver)
            sport = Sport(self.driver)
            logging.info('Now in Sport Script')

            home_page.navigate_sports()
            sport.buy_jerseys()
            logging.info(testCaseId + "=" + "Pass")

        except WebDriverException:
            logging.error('Exception raised in method - ' + test_method_name)
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(
                Initilization.path + "Report\Screenshots\\" + test_method_name + "-" + now + ".png")
            traceback.print_exc()
            logging.info(testCaseId + "=" + "Fail")
            raise WebDriverException

# if __name__ == "__main__":
#     unittest.main()

