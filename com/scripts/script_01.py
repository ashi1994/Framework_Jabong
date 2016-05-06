from com.generic_lib.initilization import *
from com.POM.methods.home_method import *
from com.POM.methods.men_method import *
from com.POM.methods.sports_method import *
import logging

class Men(Initilization):
    def test_buy_blazers(self):
        home_page = HomePage(self.driver)
        clothing = Clothing(self.driver)
        logging.info('Now in Men Script')

        home_page.navigate_men()
        clothing.buy_suits_blazers()

class Sports(Initilization):
    def test_buy_jersey(self):
        home_page = HomePage(self.driver)
        sport = Sport(self.driver)
        logging.info('Now in Sport Script')

        home_page.navigate_sports()
        sport.buy_jerseys()






