from com.generic_lib.initilization import *
from com.generic_lib.listener import *
from com.POM.methods.home_method import *
from com.POM.methods.men_method import *
from com.POM.methods.sports_method import *


class Women(Initilization):

    def test_buy_blazers(self):
        test_method_name = self._testMethodName

        pjsdriver = webdriver.PhantomJS("phantomjs")
        self.driver = EventFiringWebDriver(pjsdriver, ScreenshotListener(test_method_name))

        # **********Instiantiation should be here, after listener invoking.********
        home_page = HomePage(self.driver)
        clothing = Clothing(self.driver)
        logging.info('Now in Women Script')

        home_page.navigate_men()
        clothing.buy_suits_blazers()

class Kids(Initilization):
    def test_buy_jersey(self):
        test_method_name = self._testMethodName

        pjsdriver = webdriver.PhantomJS("phantomjs")
        self.driver = EventFiringWebDriver(pjsdriver, ScreenshotListener(test_method_name))

        # **********Instiantiation should be here, after listener invoking.********
        test_method_name = self._testMethodName

        pjsdriver = webdriver.PhantomJS("phantomjs")
        self.driver = EventFiringWebDriver(pjsdriver, ScreenshotListener(test_method_name))

        # **********Instiantiation should be here, after listener invoking.********
        home_page = HomePage(self.driver)
        sport = Sport(self.driver)
        logging.info('Now in Kids Script')

        home_page.navigate_sports()
        sport.buy_jerseys()