from tms_aqa_python_pytest.locators.search_locators import MFSearchLocators
from tms_aqa_python_pytest.pages.base_page import BasePage


class SearchHelper(BasePage):

    def open_search(self):
        search_button = self.find_element(MFSearchLocators.SEARCH_OPEN_BUTTON)
        search_button.click()
        return search_button

    def enter_word(self, word):
        search_field = self.find_element(MFSearchLocators.SEARCH_FIELD)
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(MFSearchLocators.SEARCH_BUTTON, time=2).click()

    def check_search_result(self):
        return self.find_elements(MFSearchLocators.SEARCH_RESULT, time=2)
