import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium import webdriver

@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()

def get_by_data_id(data_id):
    return f"//*[data-id={data_id}]"

def get_by_class_css(selector):
    return f'[class={selector}]'