from selenium.webdriver.common.by import By

from Utilities import configReader


class car_Base:

    def __init__(self, driver):
        self.driver = driver

    def get_car_title(self):
        carstitle = self.driver.find_element(By.XPATH, configReader.readConfig("locators","carTitle_XPATH")).text
        return carstitle

    def get_car_names_prices(self):
        carname = self.driver.find_elements(By.XPATH, configReader.readConfig("locators","carname_XPATH"))
        carprice = self.driver.find_elements(By.XPATH, configReader.readConfig("locators","carprice_XPATh"))

        for i in range(1,5):
            print("Car Name is "+carname[i].text+" And the price is "+carprice[i].text)

