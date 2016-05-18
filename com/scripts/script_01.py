from com.generic_lib.initilization import *
from com.POM.methods.home_method import *
from com.POM.methods.sign_in_method import *
import logging
#from com.generic_lib.listener import *



class Script01_SignIn(Initilization):

        # test_method_name = self._testMethodName

        # pjsdriver = webdriver.PhantomJS("phantomjs")
        # self.driver = EventFiringWebDriver(pjsdriver, ScreenshotListener(test_method_name))


    testCaseId = "TestCase_01"
    sheetName = "SignInData"

    def test_01_sign_in(self):
        global testCaseId
        try:
            #test_method_name = self._testMethodName

            #**********Instiantiation can not be done here********

            # pjsdriver = webdriver.PhantomJS("phantomjs")
            # d = EventFiringWebDriver(pjsdriver, ScreenshotListener(test_method_name))

            home_page = HomePage(self.driver)
            sign_in_page = SignInPage(self.driver)

            home_page.navigate_signin_page()
            sign_in_page.enter_email_id(self.testCaseId, self.sheetName)
            sign_in_page.enterPassword(self.testCaseId, self.sheetName)
            sign_in_page.clickSignInBtn()
            sign_in_page.display_error_msg()
            sign_in_page.verifyErrorMsg()
            sign_in_page.sign_in_with_google()
            sign_in_page.enter_gmail_id(self.testCaseId, self.sheetName)
            sign_in_page.enter_gmail_password(self.testCaseId, self.sheetName)
            sign_in_page.click_gmail_signin_button()
            sign_in_page.verify_jabong_loggedin()

            # sign_in_page.clickCancelBtn()
            logging.info("*****Congratulations we have successfully passed this Login to Jabong script.*****")
            logging.info(testCaseId + "=" + "Pass")

        except AssertionError:
            test_method_name = self._testMethodName
            logging.error('Exception raised in method - '+ test_method_name)
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(
                Initilization.path + "Report\Screenshots\\" + test_method_name + "-" + now + ".png")
            traceback.print_exc()
            logging.info(testCaseId + "=" + "Fail")
            raise AssertionError

# if __name__ == "__main__":
#     unittest.main()

