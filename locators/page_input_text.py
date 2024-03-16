from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from objects.base_page import BasePage
from objects.base_element import BaseElement
# ------------------------


class PageInputText(BasePage):
    url = "https://www.qa-practice.com/elements/input/simple"
    name_page = BaseElement(by=By.CSS_SELECTOR, value_by="div h1")
    name_page.check_value = "Поле ввода"

    tab_text_field = BaseElement(by=By.XPATH, value_by='//*[@id="content"]/ul/li[1]/a')
    tab_email_field = BaseElement(by=By.XPATH, value_by='//*[@id="content"]/ul/li[2]/a')
    tab_password_field = BaseElement(by=By.XPATH, value_by='//*[@id="content"]/ul/li[3]/a')
# ------------------------


class PageInputSimple(BasePage):
    url = "https://www.qa-practice.com/elements/input/simple"
    name_page = BaseElement(by=By.CSS_SELECTOR, value_by="div h1")
    name_page.check_value = "Поле ввода"

    entry_text_field = BaseElement(by=By.CSS_SELECTOR, value_by="div.content input[name='text_string']")

    entry_text_field.check_value = 'tut_bil_Vasia-2'

    button_keyboard_enter = Keys.ENTER

    message_for_check = BaseElement(by=By.CSS_SELECTOR, value_by="div.result p.result-text")
    message_for_check.check_value = 'tut_bil_Vasia-2'
# ------------------------


class PageInputEmail(BasePage):
    url = "https://www.qa-practice.com/elements/input/email"
    name_page = BaseElement(by=By.CSS_SELECTOR, value_by="div h1")
    name_page.check_value = "Поле ввода"

    entry_email_field = BaseElement(by=By.CSS_SELECTOR, value_by="div.content input[name='email']")
    entry_email_field.check_value = 'user_name@mail.test'

    button_keyboard_enter = Keys.ENTER

    message_for_check = BaseElement(by=By.CSS_SELECTOR, value_by="div.result p.result-text")
    message_for_check.check_value = 'user_name@mail.test'
# ------------------------


class PageInputPassword(BasePage):
    url="https://www.qa-practice.com/elements/input/passwd"
    name_page = BaseElement(by=By.CSS_SELECTOR, value_by="div h1")
    name_page.check_value = "Поле ввода"

    entry_password_field = BaseElement(by=By.CSS_SELECTOR, value_by="div.content input[name='password']")
    entry_password_field.check_value = 'Qwerty*1'

    button_keyboard_enter = Keys.ENTER

    message_for_check = BaseElement(by=By.CSS_SELECTOR, value_by="div.result p.result-text")
    message_for_check.check_value = 'Qwerty*1'


