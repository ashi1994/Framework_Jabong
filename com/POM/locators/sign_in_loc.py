from selenium.webdriver.common.by import By

class SignInLoc(object):

    SIGN_IN = (By.XPATH,"//a[text()='Sign In']")
    EMAIL_TEXTBOX = (By.ID,"login-email")
    PASSWORD_TEXTBOX = (By.NAME,"password")
    SIGNIN_BUTTON = (By.XPATH,"//button[text()='SIGN IN']")
    ERROR_TEXT = (By.XPATH,"//span[contains(text(),'Incorrect username or password.')]")
    CLOSE_BUTTON = (By.CLASS_NAME,"close")
