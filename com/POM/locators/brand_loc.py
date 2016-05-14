from selenium.webdriver.common.by import By
class BrandLoc(object):

# Category

    INTERNATIONAL_BRANDS = (By.ID,"international")
    BOUTIQUES_BRANDS = (By.ID,"boutiques")
    GAS_BRAND = (By.XPATH, "//article//span//a[contains(@href,'Gas')]")


