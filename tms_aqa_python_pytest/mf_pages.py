from base_app import BasePage
from selenium.webdriver.common.by import By


def get_element_by_css(selector):
    return By.CSS_SELECTOR, selector


def get_element_by_xpath(xpath):
    return By.XPATH, xpath


class MFSearchLocators:
    SEARCH_OPEN_BUTTON = get_element_by_css(".search-lupa-btn")
    SEARCH_FIELD = get_element_by_css("#header-search-input")
    SEARCH_BUTTON = get_element_by_css(".search-lupa-fake")
    SEARCH_RESULT = get_element_by_css("[data-entity='item']")


class SearchHelper(BasePage):

    def open_search(self):
        search_button = self.find_element(MFSearchLocators.SEARCH_OPEN_BUTTON)
        search_button.click()
        return search_button

    def enter_word(self, word):
        search_field = self.find_element(MFSearchLocators.SEARCH_FIELD)
        # search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(MFSearchLocators.SEARCH_BUTTON, time=2).click()

    def check_search_result(self):
        return self.find_elements(MFSearchLocators.SEARCH_RESULT, time=2)


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
    ADDED_TO_CART_NAV = get_element_by_xpath("//a/*[text()=1]")
    FAV_BUTTON = get_element_by_css("#js-btn-to-fav")
    REVIEWS_POPUP = get_element_by_css(".reviews-quantity")
    DELIVERIES_POPUP = get_element_by_css(".delivery-info")
    SIZE_TABLE_POPUP = get_element_by_css(".desktop-text-text")
    SIZE_TABLE_OPENED = get_element_by_css(".table-info")
    ADDITIONAL_INFO_POPUP = get_element_by_css(".description-link")
    ITEM_BREADCRUMBS_BLOCK = get_element_by_css(".nav-breadcrumbs-list")


class ItemHelper(BasePage):

    def item_card_opened(self):
        return self.find_element(MFItemCartLocators.ITEM_TITLE)

    def choose_size(self):
        size_popup = self.find_element(MFItemCartLocators.SIZE_DROPDOWN)
        size_popup.click()
        choose = self.find_element(MFItemCartLocators.CHOOSE_FIRST_SIZE)
        choose.click()
        return choose

    def size_chosen(self):
        return self.find_element(MFItemCartLocators.SIZE_CHOSEN)

    def open_size_table(self):
        return self.find_element(MFItemCartLocators.SIZE_TABLE_POPUP).click()

    def size_table_opened(self):
        return self.find_element(MFItemCartLocators.SIZE_TABLE_OPENED)

    def item_to_cart(self):
        return self.find_element(MFItemCartLocators.ADD_TO_CART_BUTTON)

    def item_added_to_cart(self):
        return (self.find_element(MFItemCartLocators.ADDED_TO_CART_BUTTON),
                self.find_element(MFItemCartLocators.ADDED_TO_CART_NAV))
