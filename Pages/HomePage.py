import time

from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def newCarPage(self):
        self.moveto("newcar_XPATH")
        time.sleep(3)
        self.click("findnewcar_XPATH")
        return NewCarsPage(self.driver)
