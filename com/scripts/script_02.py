from com.generic_lib.initilization import *
from com.POM.methods.home_method import *
from com.POM.methods.sign_in_method import *
import logging
from com.generic_lib.listener import *

class SignIn(Initilization):

    testCaseId = "SignIn_01"
    sheetName = "SignInData"

    def test_sign_in(self):
        test_method_name = self._testMethodName

        #**********Instiantiation can not be done here********
        #home_page = HomePage(self.driver)
        #sign_in_page = SignInPage(self.driver)

        pjsdriver = webdriver.PhantomJS("phantomjs")
        self.driver = EventFiringWebDriver(pjsdriver, ScreenshotListener(test_method_name))

        #test_method_name = self._testMethodName
        home_page = HomePage(self.driver)
        sign_in_page = SignInPage(self.driver)

        home_page.navigate_signin_page()
        sign_in_page.enter_email_id(self.testCaseId, self.sheetName)
        sign_in_page.enterPassword(self.testCaseId, self.sheetName)
        sign_in_page.clickSignInBtn()
        sign_in_page.verifyErrorMsg(test_method_name)
        sign_in_page.clickCancelBtn()
        logging.info("Inside SignIn script.")

if __name__ == "__main__":
    unittest.main()