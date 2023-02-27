import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture
def getDriver(request, getBrowser):
    if getBrowser == "firefox":
        options = FirefoxOptions()
        options.binary_location = r'C:\Users\SachinKumar\AppData\Local\Mozilla Firefox\firefox.exe'
        _driver = webdriver.Firefox(executable_path=r'C:\BrowserDriver\geckodriver.exe', options=options)
    else:
        options = Options()
        options.add_argument("start-maximized")
        _driver = webdriver.Chrome(service=Service(executable_path=r'C:\BrowserDriver\chromedriver.exe'), options=options)
    _driver.maximize_window()
    _driver.implicitly_wait(10)
    _driver.set_page_load_timeout(60)
    _driver.get("https://www.saucedemo.com/")
    request.cls.driver = _driver
    yield request.cls.driver
    time.sleep(3)
    _driver.close()

@pytest.fixture
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
