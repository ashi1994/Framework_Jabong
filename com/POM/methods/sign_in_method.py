from com.generic_lib.excel_sheet import *
from com.POM.locators.sign_in_loc import *
from com.generic_lib.initilization import *
import time
import logging
import sys, traceback
from datetime import datetime
from selenium import webdriver
import os

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class SignInPage(BasePage,ExcelSheet):

    def enter_email_id(self, testCaseId, sheetName):
        data = self.readData(testCaseId, sheetName)
        email_textbox = self.driver.find_element(*SignInLoc.EMAIL_TEXTBOX)
        email_textbox.send_keys(data[1])
        logging.info('Login Email Id entered.')
        time.sleep(2)

    def enterPassword(self, testCaseId, sheetName):
        data = self.readData(testCaseId, sheetName)
        passwordtextbox = self.driver.find_element(*SignInLoc.PASSWORD_TEXTBOX)
        passwordtextbox.send_keys(data[2])
        logging.info('Login Password entered.')
        time.sleep(2)

    def clickSignInBtn(self):
        signInBtn = self.driver.find_element(*SignInLoc.SIGNIN_BUTTON)
        signInBtn.click()
        logging.info('Clicked on Signin button for login Jabong.')
        time.sleep(2)

    def display_error_msg(self):
        error_msg_display = self.driver.find_element(*SignInLoc.ERROR_TEXT).is_displayed()
        if error_msg_display == True:
            logging.error('Oops....We have entered incorrect login Email Id or Password.')
        time.sleep(2)

    def verifyErrorMsg(self):
        actualMsg = self.driver.find_element(*SignInLoc.ERROR_TEXT).text
        assert actualMsg == 'Incorrect username or password.'
        logging.info('Error message verified.')
        time.sleep(2)

    def sign_in_with_google(self):
        signin_google = self.driver.find_element(*SignInLoc.SIGNIN_GOOGLE)
        signin_google.click()
        logging.info('Trying to login via Google account.')
        time.sleep(2)

    def enter_gmail_id(self, testCaseId, sheetName):
        data = self.readData(testCaseId, sheetName)
        gmail_id_textbox = self.driver.find_element(*SignInLoc.GMAIL_ID_TEXTBOX)
        gmail_id_textbox.send_keys(data[1])
        click_next_button = self.driver.find_element(*SignInLoc.GMAIL_ID_NEXT_BUTTON)
        click_next_button.click()
        logging.info('Gmail login Id entered.')
        time.sleep(2)

    def enter_gmail_password(self, testCaseId, sheetName):
        data = self.readData(testCaseId, sheetName)
        gmail_id_textbox = self.driver.find_element(*SignInLoc.GMAIL_PASSWORD_TEXTBOX)
        gmail_id_textbox.send_keys(data[2])
        logging.info('Gmail login password entered.')
        time.sleep(2)

    def click_gmail_signin_button(self):
        gmail_signin_button = self.driver.find_element(*SignInLoc.GMAIL_SIGNIN_BUTTON)
        gmail_signin_button.click()
        logging.info('Clicked on Gmail Signin button.')
        time.sleep(2)

    def verify_jabong_loggedin(self):
        account_loggedin = self.driver.find_element(*SignInLoc.ACCOUNT_LOGEDIN).is_displayed()
        if account_loggedin == True:
            logging.info('We have successfully logged in Jabong application.')
        time.sleep(2)

    def clickCancelBtn(self):
        cancelBtn = self.driver.find_element(*SignInLoc.CLOSE_BUTTON)
        cancelBtn.click()
        time.sleep(2)
