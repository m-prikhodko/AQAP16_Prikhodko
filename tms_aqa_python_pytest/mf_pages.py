from itertools import count

from base_app import BasePage
from selenium.webdriver.common.by import By


class MFSearchLocators:
    LOCATOR_SEARCH_OPEN_BUTTON = (By.CSS_SELECTOR, ".search-lupa-btn")
    LOCATOR_SEARCH_FIELD = (By.CSS_SELECTOR, "#header-search-input")
    LOCATOR_SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-lupa-fake")
    LOCATOR_SEARCH_RESULT = (By.CSS_SELECTOR, "[data-entity='item']")


class SearchHelper(BasePage):

    def open_search(self):
        search_button = self.find_element(MFSearchLocators.LOCATOR_SEARCH_OPEN_BUTTON)
        search_button.click()
        return search_button

    def enter_word(self, word):
        search_field = self.find_element(MFSearchLocators.LOCATOR_SEARCH_FIELD)
        # search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(MFSearchLocators.LOCATOR_SEARCH_BUTTON, time=2).click()

    def check_search_result(self):
        return self.find_elements(MFSearchLocators.LOCATOR_SEARCH_RESULT, time=2)


class MFItemCartLocators:
    LOCATOR_ITEM_TITLE = (By.CSS_SELECTOR, ".mf-product-title")
    LOCATOR_ITEM_MODEL = (By.CSS_SELECTOR, ".model-desktop")
    LOCATOR_ITEM_COLOR = (By.CSS_SELECTOR, ".current-color")
    LOCATOR_ITEM_PRICE = (By.CSS_SELECTOR, "._price")
    LOCATOR_ITEM_PHOTO = (By.CSS_SELECTOR, ".photo-item__new-photo")
    LOCATOR_SIZE_DROPDOWN = (By.CSS_SELECTOR, ".size-header.closed")
    LOCATOR_CHOOSE_FIRST_SIZE = (By.CSS_SELECTOR, ".size-table-row")
    LOCATOR_SIZE_CHOSEN = (By.CSS_SELECTOR, ".chosen-value")
    LOCATOR_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".button-main-text")
    LOCATOR_ADDED_TO_CART_BUTTON = (By.XPATH, "//script[contains(text(), 'Перейти в корзину')]")
    LOCATOR_ADDED_TO_CART_NAV = (By.XPATH, "//a/*[text()=1]")
    LOCATOR_FAV_BUTTON = (By.CSS_SELECTOR, "#js-btn-to-fav")
    LOCATOR_REVIEWS_POPUP = (By.CSS_SELECTOR, ".reviews-quantity")
    LOCATOR_DELIVERIES_POPUP = (By.CSS_SELECTOR, ".delivery-info")
    LOCATOR_SIZE_TABLE_POPUP = (By.CSS_SELECTOR, ".desktop-text-text")
    LOCATOR_SIZE_TABLE_OPENED = (By.CSS_SELECTOR, ".table-info")
    LOCATOR_ADDITIONAL_INFO_POPUP = (By.CSS_SELECTOR, ".description-link")
    LOCATOR_ITEM_BREADCRUMBS_BLOCK = (By.CSS_SELECTOR, ".nav-breadcrumbs-list")


class ItemHelper(BasePage):

    def item_card_opened(self):
        title = self.find_element(MFItemCartLocators.LOCATOR_ITEM_TITLE)
        return title

    def choose_size(self):
        size_popup = self.find_element(MFItemCartLocators.LOCATOR_SIZE_DROPDOWN)
        size_popup.click()
        choose = self.find_element(MFItemCartLocators.LOCATOR_CHOOSE_FIRST_SIZE)
        choose.click()
        return choose

    def size_chosen(self):
        return self.find_element(MFItemCartLocators.LOCATOR_SIZE_CHOSEN)

    def open_size_table(self):
        return self.find_element(MFItemCartLocators.LOCATOR_SIZE_TABLE_POPUP).click()

    def size_table_opened(self):
        return self.find_element(MFItemCartLocators.LOCATOR_SIZE_TABLE_OPENED)

    def item_to_cart(self):
        return self.find_element(MFItemCartLocators.LOCATOR_ADD_TO_CART_BUTTON)

    def item_added_to_cart(self):
        return (self.find_element(MFItemCartLocators.LOCATOR_ADDED_TO_CART_BUTTON),
                self.find_element(MFItemCartLocators.LOCATOR_ADDED_TO_CART_NAV))
