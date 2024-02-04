from tms_aqa_python_pytest.locators.item_card_locators import MFItemCartLocators
from tms_aqa_python_pytest.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class ItemCard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


class ItemHelper(BasePage):

    def item_card_opened(self):
        title = self.find_element(MFItemCartLocators.ITEM_TITLE)
        return title

    def choose_size(self):
        size_popup = self.find_element(MFItemCartLocators.SIZE_DROPDOWN)
        size_popup.click()
        choose = self.find_element(MFItemCartLocators.CHOOSE_FIRST_SIZE)
        choose.click()
        return choose

    def open_size_table(self):
        return self.find_element(MFItemCartLocators.SIZE_TABLE_POPUP).click()

    def item_to_cart(self):
        return self.find_element(MFItemCartLocators.ADD_TO_CART_BUTTON)

    def item_added_to_cart(self):
        return (self.find_element(MFItemCartLocators.ADDED_TO_CART_BUTTON),
                self.find_element(MFItemCartLocators.ADDED_TO_CART_NAV))

    def item_to_favorites(self):
        fav_icon = self.find_element(MFItemCartLocators.FAV_BUTTON)
        delivery_btn = self.find_element(MFItemCartLocators.DELIVERIES_POPUP)
        # self.scroll_to_element(delivery_btn)
        # actions.move_to_element(delivery_btn)
        # actions.perform()
        # self.driver.execute_script("arguments[0].click();", MFItemCartLocators.FAV_BUTTON)
        self.driver.execute_script("arguments[0](open_url).click();",
                                   MFItemCartLocators.FAV_BUTTON)
        return fav_icon

    def open_deliveries(self):
        return self.find_element(MFItemCartLocators.DELIVERIES_POPUP).click()
