from tms_aqa_python_pytest.helpers.locators import get_element_by_css, get_element_by_xpath


class MFItemCartLocators:
    ITEM_TITLE = get_element_by_css(".mf-product-title")
    ITEM_MODEL = get_element_by_css(".model-desktop")
    ITEM_COLOR = get_element_by_css(".current-color")
    ITEM_PRICE = get_element_by_css("._price")
    ITEM_PHOTO = get_element_by_css(".photo-item__new-photo")
    SIZE_DROPDOWN = get_element_by_css(".size-header.closed")
    CHOOSE_FIRST_SIZE = get_element_by_css(".size-table-row")
    SIZE_CHOSEN = get_element_by_css(".chosen-value")
    ADD_TO_CART_BUTTON = get_element_by_css(".button-main-text")
    ADDED_TO_CART_BUTTON = get_element_by_xpath("//script[contains(text(), 'Перейти в корзину')]")
    ADDED_TO_CART_NAV = get_element_by_xpath("//a[contains(@href,'cart')]/*[text()=1]")
    FAV_BUTTON = get_element_by_css(".icon.icon-heart.empty")
    # FAV_BUTTON = get_element_by_css("#js-btn-to-fav")
    ADDED_TO_FAVS = get_element_by_xpath("//a[@id='ico-favorites']/*[text()=1]")
    REVIEWS_POPUP = get_element_by_css(".reviews-quantity")
    DELIVERIES_POPUP = get_element_by_css(".delivery-info")
    DELIVERIES_OPENED = get_element_by_css("#popup-delivery")
    SIZE_TABLE_POPUP = get_element_by_css(".desktop-text-text")
    SIZE_TABLE_OPENED = get_element_by_css(".table-info")
    ADDITIONAL_INFO_POPUP = get_element_by_css(".description-link")
    ITEM_BREADCRUMBS_BLOCK = get_element_by_css(".nav-breadcrumbs-list")