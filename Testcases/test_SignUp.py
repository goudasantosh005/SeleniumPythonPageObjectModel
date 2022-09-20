import allure
import pytest

from Testcases.baseTest import basetest
from Utilities import dataProvider

from allure_commons.types import AttachmentType
from Pages.RegistrationPage import Registration
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class TestSign(basetest):
    @pytest.mark.parametrize("name, phoneNum, email, country, city, username, password",
                             dataProvider.get_data("Logintest"))
    def test_signup(self, name, phoneNum, email, country, city, username, password):
        log.logger.info("Test Sign UpStarted")
        regPage = Registration(self.driver)
        regPage.fillform(name, phoneNum, email, country, city, username, password)
        log.logger.info("Test Sign Up executed successfully")
