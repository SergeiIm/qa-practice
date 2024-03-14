# from time import sleep

from locators.page_index import page_index
from locators.page_input_text import page_input_text, page_input_simple, page_input_email, page_input_password


def test_positive_input_simple(browser):
    page_index.activate_page(browser)
    page_index.check_find_and_save_element(page_index.link_input_text)
    page_index.click_on_link(page_index.link_input_text)

    page_input_text.activate_page(browser)
    page_input_text.check_find_and_save_element(page_input_text.tab_text_field)
    page_input_text.click_on_link(page_input_text.tab_text_field)

    page_input_simple.activate_page(browser)
    page_input_simple.check_find_and_save_element(page_input_simple.entry_text_field)
    page_input_simple.send_strung_on_element(page_input_simple.entry_text_field,
                                             page_input_simple.entry_text_field.check_value)
    page_input_simple.put_button_on_the_keyboard(page_input_simple.button_keyboard_enter)
    page_input_simple.check_find_and_save_element(page_input_simple.message_for_check)
    page_input_simple.check_attribute_text(page_input_simple.message_for_check)


def test_positive_input_email(browser):
    page_index.activate_page(browser)
    page_index.check_find_and_save_element(page_index.link_input_text)
    page_index.click_on_link(page_index.link_input_text)

    page_input_text.activate_page(browser)
    page_input_text.check_find_and_save_element(page_input_text.tab_email_field)
    page_input_text.click_on_link(page_input_text.tab_email_field)

    page_input_email.activate_page(browser)
    page_input_email.check_find_and_save_element(page_input_email.entry_email_field)
    page_input_email.send_strung_on_element(page_input_email.entry_email_field,
                                            page_input_email.entry_email_field.check_value)
    page_input_email.put_button_on_the_keyboard(page_input_email.button_keyboard_enter)
    page_input_email.check_find_and_save_element(page_input_email.message_for_check)
    page_input_email.check_attribute_text(page_input_email.message_for_check)


def test_positive_input_password(browser):
    page_index.activate_page(browser)
    page_index.check_find_and_save_element(page_index.link_input_text)
    page_index.click_on_link(page_index.link_input_text)

    page_input_text.activate_page(browser)
    page_input_text.check_find_and_save_element(page_input_text.tab_password_field)
    page_input_text.click_on_link(page_input_text.tab_password_field)

    page_input_password.activate_page(browser)
    page_input_password.check_find_and_save_element(page_input_password.entry_password_field)
    page_input_password.send_strung_on_element(page_input_password.entry_password_field,
                                               page_input_password.entry_password_field.check_value)
    page_input_password.put_button_on_the_keyboard(page_input_password.button_keyboard_enter)
    page_input_password.check_find_and_save_element(page_input_password.message_for_check)
    page_input_password.check_attribute_text(page_input_password.message_for_check)
