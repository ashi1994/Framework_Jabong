from selenium.webdriver.common.by import By

class MenLoc(object):

    SUITE_BLAZER = (By.XPATH,"//div[@class='dropdown-container row']//a[text()='Suits & Blazers']")
    FILTER_SLIM = (By.XPATH, "//input[@type='checkbox' and @value='Slim']")
    SORT_FILTER = (By.XPATH), "//option[text()='Popularity']"
    SUITE_01_IMAGE = (By.XPATH, "//div[div[contains(text(),'The Design Factory ')]//span[contains(text(),'Solid Maroon  Blazer')]]"
                             "/preceding-sibling::figure")
    SUITE_02_IMAGE = (By.XPATH, "//div[div[contains(text(),'Mufti')]//span[contains(text(),'Blue Jackets & Blazers')]]"
                                "/preceding-sibling::figure")
    SELECT_SIZE = (By.XPATH, "//ul[@class='options']//li[contains(@class,'first popover-options')]")
    ADD_TO_BAG = (By.ID, "add-to-cart")
    BAG_ICON = (By.ID,"mini-cart")
    REMOVE_BUTTON = (By.XPATH, "//a[text()='REMOVE']")

