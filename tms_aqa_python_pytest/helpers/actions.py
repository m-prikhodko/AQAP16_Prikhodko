from selenium.webdriver.common.keys import Keys
from tms_aqa_python_pytest.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class ActionHelpers(BasePage):

    def mouse_click(self, locator):
        ActionChains(self.driver).move_to_element(locator).click().perform()

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def keyboard_click(self, locator):
        locator.send_keys(Keys.ENTER)

    def fill(self, locator, text: str):
        locator.send_keys(text)

    def clear(self, locator):
        locator.clear()

    def alert_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def alert_reject(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def alert_get_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

    def alert_fill_prompt(self, text: str):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def scroll_to_element(self, locator):
        return self.driver.execute_script("arguments[0].scrollInToView();", locator)

    def get_all_windows(self):
        return self.driver.window_handles

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def open_new_window(self):
        self.driver.execute_script("window.open('');")

    def switch_to_last_tab(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])

    def close_current_window(self):
        self.driver.close()

    def interact_with_iframe(self, iframe_identifier, interaction_func):
        self.driver.switch_to.frame(iframe_identifier)
        interaction_func(self.driver)
        self.driver.switch_to.default_content()

    def upload_file(self, file_input_selector, file_path: str):
        file_input = self.driver.find_element_by_css_selector(file_input_selector)
        file_input.send_keys(file_path)
