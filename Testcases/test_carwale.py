import sys
import time
import allure
import pytest

from Pages.CarBasePage import car_Base
from Pages.HomePage import HomePage
from Testcases.baseTest import basetest
from Utilities import dataProvider

from allure_commons.types import AttachmentType
from Pages.RegistrationPage import Registration
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_Carwale(basetest):

    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("*************Testing go to new card **********")
        home = HomePage(self.driver)
        home.newCarPage()
        time.sleep(3)

    class TestSign(basetest):
        @pytest.mark.parametrize("card_brand,car_title",
                                 dataProvider.get_data("NewCarTest"))
        def test_signup(self, card_brand, car_title):
            log.logger.info("*************Inside select card tests **********")
            home = HomePage(self.driver)
            car = car_Base(self.driver)
            if card_brand == 'BMW':
                home.newCarPage().selectBmw()
                title = car.get_car_title()
                assert title == car_title, "Cars Title are not matching"
                car.get_car_names_prices()
            elif card_brand == 'Hyundai':
                home.newCarPage().selectHyundai()
                title = car.get_car_title()
                assert title == car_title, "Cars Title are not matching"
                car.get_car_names_prices()
            elif card_brand == 'Honda':
                home.newCarPage().selectHonda()
                title = car.get_car_title()
                assert title == car_title, "Cars Title are not matching"
                car.get_car_names_prices()
            elif card_brand == 'Toyota':
                home.newCarPage().selectToyota()
                title = car.get_car_title()
                assert title == car_title, "Cars Title are not matching"
                car.get_car_names_prices()
            time.sleep(3)
