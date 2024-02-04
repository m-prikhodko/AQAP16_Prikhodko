from tms_aqa_python_pytest.helpers.locators import get_element_by_css


class MFSearchLocators:
    SEARCH_OPEN_BUTTON = get_element_by_css(".search-lupa-btn")
    SEARCH_FIELD = get_element_by_css("#header-search-input")
    SEARCH_BUTTON = get_element_by_css(".search-lupa-fake")
    SEARCH_RESULT = get_element_by_css("[data-entity='item']")