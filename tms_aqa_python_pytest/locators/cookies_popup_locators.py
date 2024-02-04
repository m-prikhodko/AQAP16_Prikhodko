from tms_aqa_python_pytest.helpers.locators import get_element_by_css, get_element_by_xpath


class MFCookiesLocators:
    POPUP_IS_VISIBLE = get_element_by_css("[class='app-cookies__popup app-cookies__popup-initialized']")
    POPUP_BY_ACCEPT = get_element_by_css("#js-submit-btn")
    POPUP_BY_REJECT = get_element_by_css("#js-reject-btn")
    POPUP_BY_SETTINGS = get_element_by_css("#js-settings-btn")
    POPUP_BY_ANALYTICAL_COOKIES = get_element_by_xpath("//*[contains(text(), 'Аналитические')]")
    POPUP_BY_ADV_COOKIES = get_element_by_xpath("//*[contains(text(), 'Рекламные')]")
    POPUP_BY_ANALYTICAL_CHECKED = get_element_by_xpath(
        "//*[@class='app-cookies__popup-infobox mf-confirm']//*[contains(text(), 'Аналитические')]")
    POPUP_BY_ADV_CHECKED = get_element_by_xpath(
        "//*[@class='app-cookies__popup-infobox mf-confirm']//*[contains(text(), 'Рекламные')]")
    POPUP_BY_BACK_FROM_SETTINGS = get_element_by_css("#js-rollback-btn")
    POPUP_IS_NOT_VISIBLE = get_element_by_css("[class*=' hide']")

