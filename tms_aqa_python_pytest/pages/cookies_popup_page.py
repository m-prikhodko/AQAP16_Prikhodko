from tms_aqa_python_pytest.locators.cookies_popup_locators import MFCookiesLocators
from tms_aqa_python_pytest.pages.base_page import BasePage


class CookiesHelper(BasePage):
    def cookies_by_popup_reject(self):
        self.find_element(MFCookiesLocators.POPUP_IS_VISIBLE)
        reject_button = self.find_element(MFCookiesLocators.POPUP_BY_REJECT)
        reject_button.click()
        return reject_button

    def cookies_by_popup_accept_all(self):
        self.find_element(MFCookiesLocators.POPUP_IS_VISIBLE)
        accept_button = self.find_element(MFCookiesLocators.POPUP_BY_ACCEPT)
        accept_button.click()
        return accept_button

    def cookies_by_popup_accept_analytical(self):
        self.find_element(MFCookiesLocators.POPUP_IS_VISIBLE)
        settings = self.find_element(MFCookiesLocators.POPUP_BY_SETTINGS)
        settings.click()
        analytical = self.find_element(MFCookiesLocators.POPUP_BY_ANALYTICAL_COOKIES)
        analytical.click()
        self.find_element(MFCookiesLocators.POPUP_BY_ANALYTICAL_CHECKED)
        accept_button = self.find_element(MFCookiesLocators.POPUP_BY_ACCEPT)
        accept_button.click()
        return accept_button

    def cookies_by_popup_accept_adv(self):
        self.find_element(MFCookiesLocators.POPUP_IS_VISIBLE)
        settings = self.find_element(MFCookiesLocators.POPUP_BY_SETTINGS)
        settings.click()
        adv = self.find_element(MFCookiesLocators.POPUP_BY_ADV_COOKIES)
        adv.click()
        self.find_element(MFCookiesLocators.POPUP_BY_ADV_CHECKED)
        accept_button = self.find_element(MFCookiesLocators.POPUP_BY_ACCEPT)
        accept_button.click()
        return accept_button
