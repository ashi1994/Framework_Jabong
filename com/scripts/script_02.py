from com.POM.methods.home_method import *
from com.POM.methods.sign_in_method import *
import logging
class SignIn(Initilization, ExcelSheet):

    testCaseId = "SignIn_01"
    sheetName = "SignInData"

    def test_sign_in(self):

        home_page = HomePage(self.driver)
        sign_in_page = SignInPage(self.driver)

        home_page.navigate_signin_page()
        sign_in_page.enter_email_id(self.testCaseId, self.sheetName)
        sign_in_page.enterPassword(self.testCaseId, self.sheetName)
        sign_in_page.clickSignInBtn()
        sign_in_page.verifyErrorMsg()
        sign_in_page.clickCancelBtn()
        logging.info("Inside SignIn script.")



if __name__ == "__main__":
    unittest.main()