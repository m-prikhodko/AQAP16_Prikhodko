import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='session', autouse=False)
def driver_firefox():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope='session', autouse=False)
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(autouse=True)
def driver():
    print("Start driver\n")
    yield
    print("Finish driver\n")
