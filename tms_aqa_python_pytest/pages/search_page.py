from tms_aqa_python_pytest.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MFSearchLocators:
    LOCATOR_SEARCH_OPEN_BUTTON = (By.CSS_SELECTOR, ".search-lupa-btn")
    LOCATOR_SEARCH_FIELD = (By.CSS_SELECTOR, "#header-search-input")
    LOCATOR_SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-lupa-fake")
    LOCATOR_SEARCH_RESULT = (By.CSS_SELECTOR, "[data-entity='item']")


class SearchHelper(BasePage):

    def open_search(self):
        search_button = self.find_element(MFSearchLocators.LOCATOR_SEARCH_OPEN_BUTTON)
        search_button.click()
        return search_button

    def enter_word(self, word):
        search_field = self.find_element(MFSearchLocators.LOCATOR_SEARCH_FIELD)
        # search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(MFSearchLocators.LOCATOR_SEARCH_BUTTON, time=2).click()

    def check_search_result(self):
        return self.find_elements(MFSearchLocators.LOCATOR_SEARCH_RESULT, time=2)
