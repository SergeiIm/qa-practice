from time import sleep

from locators.page_index import PageIndex
from locators.page_input_text import PageInputText, PageInputSimple, PageInputEmail, PageInputPassword


def test_positive_input_simple(driver):
    page_index = PageIndex(driver)
    page_index.check_find_and_save_element(page_index.link_input_text)
    page_index.link_input_text.click_element()

    page_input_text = PageInputText(driver)
    page_input_text.check_find_and_save_element(page_input_text.tab_text_field)
    page_input_text.tab_text_field.click_element()

    page_input_simple = PageInputSimple(driver)
    page_input_simple.check_find_and_save_element(page_input_simple.entry_text_field)
    page_input_simple.entry_text_field.input_string(page_input_simple.entry_text_field.check_value)
    page_input_simple.put_button_on_the_keyboard(page_input_simple.button_keyboard_enter)
    page_input_simple.check_find_and_save_element(page_input_simple.message_for_check)
    page_input_simple.message_for_check.check_attribute_text()


def test_positive_input_email(driver):
    page_index = PageIndex(driver)
    page_index.check_find_and_save_element(page_index.link_input_text)
    page_index.link_input_text.click_element()

    page_input_text = PageInputText(driver)
    page_input_text.check_find_and_save_element(page_input_text.tab_email_field)
    page_input_text.tab_email_field.click_element()

    page_input_email = PageInputEmail(driver)
    page_input_email.check_find_and_save_element(page_input_email.entry_email_field)
    page_input_email.entry_email_field.input_string(page_input_email.entry_email_field.check_value)
    page_input_email.put_button_on_the_keyboard(page_input_email.button_keyboard_enter)
    page_input_email.check_find_and_save_element(page_input_email.message_for_check)
    page_input_email.message_for_check.check_attribute_text()


def test_positive_input_password(driver):
    page_index = PageIndex(driver)
    page_index.check_find_and_save_element(page_index.link_input_text)
    page_index.link_input_text.click_element()

    page_input_text = PageInputText(driver)
    page_input_text.check_find_and_save_element(page_input_text.tab_password_field)
    page_input_text.tab_password_field.click_element()

    page_input_password = PageInputPassword(driver)
    page_input_password.check_find_and_save_element(page_input_password.entry_password_field)
    page_input_password.entry_password_field.input_string(page_input_password.entry_password_field.check_value)
    page_input_password.put_button_on_the_keyboard(page_input_password.button_keyboard_enter)
    page_input_password.check_find_and_save_element(page_input_password.message_for_check)
    page_input_password.message_for_check.check_attribute_text()
