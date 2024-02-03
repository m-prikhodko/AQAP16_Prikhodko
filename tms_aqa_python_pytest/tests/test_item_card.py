import pytest

from tms_aqa_python_pytest.pages.item_card_page import ItemHelper


@pytest.mark.smoke
def test_item_card_opened(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.open_url("catalog/zhenshchinam/bryuki-leginsy/bryuki-leginsi/182491-86465-1050/")
    assert mf_item_page.item_card_opened()


@pytest.mark.smoke
def test_item_size_chosen(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.open_url("catalog/zhenshchinam/bryuki-leginsy/bryuki-leginsi/182491-86465-1050/")
    mf_item_page.choose_size()
    assert mf_item_page.size_chosen()


@pytest.mark.smoke
def test_item_added_to_cart(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.open_url("catalog/zhenshchinam/bryuki-leginsy/bryuki-leginsi/182491-86465-1050/")
    mf_item_page.choose_size()
    mf_item_page.item_to_cart()
    assert mf_item_page.item_added_to_cart()


@pytest.mark.medium
def test_table_size_opened(driver_chrome):
    mf_item_page = ItemHelper(driver_chrome)
    mf_item_page.open_url("catalog/zhenshchinam/bryuki-leginsy/bryuki-leginsi/182491-86465-1050/")
    mf_item_page.open_size_table()
    assert mf_item_page.size_table_opened()
