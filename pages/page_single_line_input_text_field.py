import allure
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as ec


class PageSingleLineInputTextField(BasePage):

    PAGE_URL = Links.PAGE_SINGLE_LINE_INPUT_TEXT_FIELD

    OBJECT_SINGLE_LINE_INPUT_TEXT_FIELD = (By.CSS_SELECTOR, "input#id_text_string")
    VALUE_INPUT_TEXT = 'KIURNDLFVD'
    BUTTON_ENTER = Keys.ENTER
    OBJECT_CHECK_RESULT = (By.CSS_SELECTOR, "p#result-text")
    VALUE_CHECK_RESULT = 'KIURNDLFVD'

    @allure.step("Enter valid value in input field.")
    def enter_value_in_input_field(self):
        self.wait.until(ec.element_to_be_clickable(self.OBJECT_SINGLE_LINE_INPUT_TEXT_FIELD)).\
            send_keys(self.VALUE_INPUT_TEXT)

    @allure.step("Click enter keyboard button.")
    def click_enter_keyboard_button(self):
        action = ActionChains(self.driver)
        action.send_keys(self.BUTTON_ENTER)
        action.perform()

    @allure.step("Check result value text")
    def check_element_attribute_text(self):
        tmp = self.wait.until(ec.presence_of_element_located(self.OBJECT_CHECK_RESULT))
        assert tmp.get_attribute('innerHTML') == self.VALUE_CHECK_RESULT
