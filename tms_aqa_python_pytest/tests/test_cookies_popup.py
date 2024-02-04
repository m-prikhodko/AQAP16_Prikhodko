import pytest
from tms_aqa_python_pytest.locators.cookies_popup_locators import MFCookiesLocators
from tms_aqa_python_pytest.pages.cookies_popup_page import CookiesHelper
from tms_aqa_python_pytest.conftest import driver_chrome


@pytest.mark.cookies_popup
def test_cookies_rejected_main_page(driver_chrome):
    mf_main_page = CookiesHelper(driver_chrome)
    mf_main_page.open_url("by/")
    mf_main_page.cookies_by_popup_reject()
    assert mf_main_page.find_element(MFCookiesLocators.POPUP_IS_NOT_VISIBLE)


@pytest.mark.cookies_popup
def test_cookies_accept_all_main_page(driver_chrome):
    mf_main_page = CookiesHelper(driver_chrome)
    mf_main_page.open_url("by/")
    mf_main_page.cookies_by_popup_accept_all()
    assert mf_main_page.find_element(MFCookiesLocators.POPUP_IS_NOT_VISIBLE)


def test_cookies_accept_analytical_main_page(driver_chrome):
    mf_main_page = CookiesHelper(driver_chrome)
    mf_main_page.open_url("by/")
    mf_main_page.cookies_by_popup_accept_analytical()
    assert mf_main_page.find_element(MFCookiesLocators.POPUP_IS_NOT_VISIBLE)


def test_cookies_accept_adv_main_page(driver_chrome):
    mf_main_page = CookiesHelper(driver_chrome)
    mf_main_page.open_url("by/")
    mf_main_page.cookies_by_popup_accept_adv()
    assert mf_main_page.find_element(MFCookiesLocators.POPUP_IS_NOT_VISIBLE)
