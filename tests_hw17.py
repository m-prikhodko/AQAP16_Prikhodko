import time

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver_firefox():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.minimize_window()
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


def test_getting_the_auth_code(driver_chrome):
    driver_chrome.get('https://markformelle.by/')

    xpath = '/html/body/div[3]/header/div[2]/div[4]/nav/span'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()

    el_id = 'regWithPhoneNumber'
    element = driver_chrome.find_element(By.ID, el_id)
    element.send_keys('292463073')

    time.sleep(5)
    xpath = '// *[ @ id = "popmechanic-form-75446"] / div[2]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()

    el2_id = 'getCodeRegistration'
    element = driver_chrome.find_element(By.ID, el2_id)
    element.click()

    time.sleep(5)

    xpath2 = '//*[@id="registrationForm"]/div[1]/div[2]/button'
    element = driver_chrome.find_element(By.XPATH, xpath2)

    assert element.text == 'Войти'


def test_open_listing_from_main(driver_chrome):
    driver_chrome.get('https://markformelle.by/')
    time.sleep(1)
    xpath = '/html/body/div[3]/header/div[2]/div[1]/div[1]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()
    time.sleep(1)
    xpath = '//*[@id="catalog-menu-list"]/li[1]/ul/li[1]/a'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()

    xpath = '/html/body/div[3]/main/div[4]/div[1]/h1'
    element = driver_chrome.find_element(By.XPATH, xpath)

    assert element.text == 'Женщинам'


def test_change_location(driver_chrome):
    driver_chrome.get('https://markformelle.by/')
    time.sleep(1)

    xpath = '/html/body/div[3]/header/div[2]/div[1]/div[2]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()
    time.sleep(1)

    xpath = '/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/ul/li[8]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()
    time.sleep(3)

    xpath = '// *[ @ id = "popmechanic-form-75446"] / div[2]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()
    time.sleep(1)

    xpath = '/html/body/div[3]/header/div[2]/div[1]/div[2]/span'
    element = driver_chrome.find_element(By.XPATH, xpath)
    assert element.text == 'Дзержинск'


def test_search_item(driver_chrome):
    driver_chrome.get('https://markformelle.by/')
    time.sleep(1)

    xpath = '/html/body/div[3]/header/div[2]/div[4]/nav/div[1]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()

    el_id = 'header-search-input'
    element = driver_chrome.find_element(By.ID, el_id)
    element.send_keys('юбка')
    element.submit()
    time.sleep(3)

    assert driver_chrome.title == 'Поиск'


def test_open_item_card_from_landing(driver_chrome):
    driver_chrome.get('https://markformelle.by/catalog/collections/Nationalartmuseum/')
    time.sleep(2)

    xpath = '/html/body/div[3]/main/div[4]/div[4]/button'
    element = driver_chrome.find_element(By.XPATH, xpath)
    actions = ActionChains(driver_chrome)
    actions.move_to_element(element).perform()

    xpath = '//*[@id="js-reject-btn"]'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()
    time.sleep(1)

    xpath = '//*[@id="bx_3966226736_575524_7e1b8e3524755c391129a9d7e6f2d206"]/div[1]/div[2]/a'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()
    time.sleep(1)

    xpath = '//*[@id="bx_117848907_575524_add_basket_link"]'
    element = driver_chrome.find_element(By.XPATH, xpath)

    assert element.is_displayed()
    assert 'Брюки' in driver_chrome.title
