from com.generic_lib.initilization import *
from com.POM.methods.home_method import *
from com.POM.methods.sign_in_method import *
import logging
#from com.generic_lib.listener import *


class SignIn(Initilization):

    testCaseId = "SignIn_01"
    sheetName = "SignInData"

    # def test_sign(self):
    #     try:
    #         # test_method_name = self._testMethodName
    #
    #         # **********Instiantiation can not be done here********
    #
    #         # pjsdriver = webdriver.PhantomJS("phantomjs")
    #         # d = EventFiringWebDriver(pjsdriver, ScreenshotListener(test_method_name))
    #         home_page = HomePage(self.driver)
    #         home_page.navigate_signin_page()
    #
    #         logging.info("Inside SignIn script.")
    #
    #     except Exception as err:
    #         listener = Listener()
    #         test_method_name = self._testMethodName
    #         logging.error('Exception raised in method - ' + test_method_name)
    #         traceback.print_exc()
    #         listener.test_fail()






    def test_sign_in(self):
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
            sign_in_page.verifyErrorMsg()
            sign_in_page.clickCancelBtn()
            logging.info("Inside SignIn script.")

        except AssertionError:
            test_method_name = self._testMethodName
            logging.error('Exception raised in method - '+ test_method_name)
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.save_screenshot(
                Initilization.path + "Report\Screenshots\\" + test_method_name + "-" + now + ".png")
            traceback._some_str("there is some exception.")



# if __name__ == "__main__":
#     unittest.main()