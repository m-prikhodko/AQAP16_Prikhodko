import pytest

from tms_aqa_python_pytest.mf_pages import SearchHelper
from tms_aqa_python_pytest.mf_pages import ItemHelper


@pytest.mark.smoke
def test_mf_search(driver_chrome):
    mf_main_page = SearchHelper(driver_chrome)
    mf_main_page.go_to_site()
    mf_main_page.open_search()
    mf_main_page.enter_word("Платье")
    mf_main_page.click_on_the_search_button()
    assert 'Поиск' in driver_chrome.title
    assert mf_main_page.check_search_result()


@pytest.mark.smoke
def test_item_card_opened(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.go_to_item()
    assert mf_item_page.item_card_opened()


@pytest.mark.smoke
def test_item_size_chosen(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.go_to_item()
    mf_item_page.choose_size()
    assert mf_item_page.size_chosen()


@pytest.mark.smoke
def test_item_added_to_cart(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.go_to_item()
    mf_item_page.choose_size()
    mf_item_page.item_to_cart()
    assert mf_item_page.item_added_to_cart()


@pytest.mark.medium
def test_table_size_opened(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.go_to_item()
    mf_item_page.open_size_table()
    assert mf_item_page.size_table_opened()

