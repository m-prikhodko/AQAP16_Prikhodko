import pytest
from tms_aqa_python_pytest.locators.item_card_locators import MFItemCartLocators
from tms_aqa_python_pytest.pages.cookies_popup_page import CookiesHelper
from tms_aqa_python_pytest.pages.item_card_page import ItemHelper
from tms_aqa_python_pytest.conftest import driver_chrome


@pytest.mark.smoke
def test_item_card_opened(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.open_url("by/catalog/zhenshchinam/bryuki-leginsy/bryuki-leginsi/182491-86465-1050/")
    assert mf_item_page.item_card_opened()


@pytest.mark.smoke
def test_item_size_chosen(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.open_url("by/catalog/zhenshchinam/bryuki-leginsy/bryuki-leginsi/182491-86465-1050/")
    mf_item_page.choose_size()
    assert mf_item_page.find_element(MFItemCartLocators.SIZE_CHOSEN)


@pytest.mark.smoke
def test_item_added_to_cart(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.open_url("by/catalog/zhenshchinam/bryuki-leginsy/bryuki-leginsi/182491-86465-1050/")
    mf_item_page.choose_size()
    mf_item_page.item_to_cart()
    assert mf_item_page.item_added_to_cart()


# Doesn't work, get JavascriptException: Message: javascript error: arguments[0].scrollInToView is not a function
# @pytest.mark.smoke
# def test_adding_to_favorites(driver_chrome):
#     mf_item_page = ItemHelper(driver_chrome)
#     mf_item_page.open_url("by/catalog/zhenshchinam/bryuki-leginsy/bryuki-leginsi/182491-86465-1050/")
#     mf_cookies_popup = CookiesHelper(driver_chrome)
#     mf_cookies_popup.cookies_by_popup_reject()
#     mf_item_page.item_to_favorites()
#     assert mf_item_page.find_element(MFItemCartLocators.ADDED_TO_FAVS)


@pytest.mark.medium
def test_table_size_opened(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.open_url("by/catalog/zhenshchinam/bryuki-leginsy/bryuki-leginsi/182491-86465-1050/")
    mf_item_page.open_size_table()
    assert mf_item_page.find_element(MFItemCartLocators.SIZE_TABLE_OPENED)


@pytest.mark.medium
def test_deliveries_opened(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.open_url("by/catalog/zhenshchinam/bryuki-leginsy/bryuki-leginsi/182491-86465-1050/")
    mf_cookies_popup = CookiesHelper(driver_chrome)
    mf_cookies_popup.cookies_by_popup_reject()
    mf_item_page.open_deliveries()
    assert mf_item_page.find_element(MFItemCartLocators.DELIVERIES_OPENED)
