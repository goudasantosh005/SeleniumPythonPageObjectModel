from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities import configReader


class Registration(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def fillform(self,name,phoneNum,email,country,city,username,password):
        self.type("nike_XPATH",name)
        self.type("puma_XPATH",phoneNum)
        self.type("email_XPATH",email)
        self.select("country_XPATH",country)
        self.type("city_XPATH", city)
        self.type("username_XPATH", username)
        self.type("password_XPATH", password)
        self.click("submit_XPATH")
