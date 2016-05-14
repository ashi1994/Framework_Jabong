from com.generic_lib.initilization import *
from com.POM.methods.home_method import *
from com.POM.methods.sign_in_method import *
import logging
from com.generic_lib.listener import *

class QuickList(Initilization):

    testCaseId = "SignIn_01"
    sheetName = "SignInData"

    def test_quick_list(self):
        test_method_name = self._testMethodName
        home_page = HomePage(self.driver)

        home_page.navigate_quick_list_page()
        logging.info("Inside SignIn script.")

if __name__ == "__main__":
    unittest.main()