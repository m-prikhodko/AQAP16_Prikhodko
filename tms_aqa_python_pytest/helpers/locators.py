from selenium.webdriver.common.by import By


def get_element_by_css(selector):
    return By.CSS_SELECTOR, selector


def get_element_by_xpath(xpath):
    return By.XPATH, xpath
