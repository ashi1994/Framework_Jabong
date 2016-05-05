from com.generic_lib.excel_sheet import *
from com.POM.locators.sign_in_loc import *
import time
import logging
import sys, traceback

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class SignInPage(BasePage,ExcelSheet):

    def enter_email_id(self, testCaseId, sheetName):
        data = self.readData(testCaseId, sheetName)
        email_textbox = self.driver.find_element(*SignInLoc.EMAIL_TEXTBOX)
        email_textbox.send_keys(data[1])

    def enterPassword(self, testCaseId, sheetName):
        data = self.readData(testCaseId, sheetName)
        passwordtextbox = self.driver.find_element(*SignInLoc.PASSWORD_TEXTBOX)
        passwordtextbox.send_keys(data[2])

    def clickSignInBtn(self):
        signInBtn = self.driver.find_element(*SignInLoc.SIGNIN_BUTTON)
        signInBtn.click()
        time.sleep(5)

    def clickCancelBtn(self):
        cancelBtn = self.driver.find_element(*SignInLoc.CLOSE_BUTTON)
        cancelBtn.click()
        time.sleep(2)

    def verifyErrorMsg(self):
        try:
            actualMsg = self.driver.find_element(*SignInLoc.ERROR_TEXT).text
            assert actualMsg == 'Incorrect username or Password.'
            logging.info('Error message verified.')
        except:
            logging.error('Error msg not verified, so Assertion failed.')
            self.driver.save_screenshot('D:\CBT_Automation\Python\Workspace_Python\Report\Framework_Jabong\Screenshots\screenshot1.png')
            traceback._some_str("there is some exception.")







