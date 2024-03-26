import random
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Single line input text field")
class TestSingleLineInputTextField(BaseTest):

    @allure.title("Enter valid text on field.")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.page_single_line_input_text_field.open()
        self.page_single_line_input_text_field.enter_value_in_input_field()
        self.page_single_line_input_text_field.click_enter_keyboard_button()
        self.page_single_line_input_text_field.check_element_attribute_text()
