import pytest

from tms_aqa_python_pytest.pages.main_page import SearchHelper


@pytest.mark.smoke
def test_mf_search(driver_chrome):
    mf_main_page = SearchHelper(driver_chrome)
    mf_main_page.open_url()
    mf_main_page.open_search()
    mf_main_page.enter_word("Платье")
    mf_main_page.click_on_the_search_button()
    assert 'Поиск' in driver_chrome.title
    assert mf_main_page.check_search_result()
