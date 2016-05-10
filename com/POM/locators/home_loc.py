from selenium.webdriver.common.by import By

class HomeLoc(object):
    DOWNLOAD_APP_LINK = (By.XPATH, "//a[text()='download app']]")
    HELP_LINK = (By.XPATH, "//a[text()='help']")
    TRACK_ORDER_LINK = (By.XPATH, "//a[text()='Track Order']")
    SIGNIN_LINK = (By.XPATH,"//a[text()='Sign In']")
    SIGNUP_LINK = (By.XPATH, "//a[text()='Signup']")
    LIKE_LINK = (By.ID,"header-like-sec")

    # Navigation Bar Locators.
    WOMEN_SECTION = (By.XPATH,"//*[@id='mainTopNav']//li[@class='nav-women']")
    MEN_SECTION = (By.XPATH, "//ul[@id='mainTopNav']/li[@class='nav-men']")
    KIDS_SECTION = (By.XPATH, "//ul[@id='mainTopNav']/li[@class='nav-kids']")
    ACCESSORIES_SECTION = (By.XPATH, "//ul[@id='mainTopNav']/li[@class='nav-accessories-store']")
    BRANDS_SECTION = (By.XPATH, "//ul[@id='mainTopNav']/li[@class='nav-brands']")
    SPORTS_SECTION = (By.XPATH, "//ul[@id='mainTopNav']/li[@class='nav-sports']")
    SALE_SECTION = (By.XPATH, "//ul[@id='mainTopNav']//a[@class='jabong-red']")
    THE_JUICE_SECTION = (By.XPATH, "//ul[@id='mainTopNav']//a[contains(text(),'The JUICE')]")



