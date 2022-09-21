import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Utilities import configReader


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def chrome_browser():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def get_browser(request):
    # global driver
    remote_url = "http://localhost:4444/wd/hub"
    if request.param == "chrome":
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "chrome"})
    if request.param == "firefox":
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "firefox"})

    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def log_on_failure(request, get_browser1):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def get_browser1(request):
    # global driver
    remote_url = "http://localhost:4444/wd/hub"
    if request.param == "chrome":
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "chrome"})
    if request.param == "firefox":
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "firefox"})
    request.cls.driver = driver
    driver.get(configReader.readConfig("basic info", "testsiteurl"))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
