from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from objects.base_page import BasePage
from objects.base_element import BaseElement

# ------------------------

page_input_text = BasePage(url="https://www.qa-practice.com/elements/input/simple")
page_input_text.name_page = BaseElement(by=By.CSS_SELECTOR, value_by="div h1")
page_input_text.name_page.check_value = "Поле ввода"

page_input_text.tab_text_field = BaseElement(by=By.XPATH, value_by='//*[@id="content"]/ul/li[1]/a')
page_input_text.tab_email_field = BaseElement(by=By.XPATH, value_by='//*[@id="content"]/ul/li[2]/a')
page_input_text.tab_password_field = BaseElement(by=By.XPATH, value_by='//*[@id="content"]/ul/li[3]/a')

# ------------------------

page_input_simple = BasePage(url="https://www.qa-practice.com/elements/input/simple")
page_input_simple.name_page = BaseElement(by=By.CSS_SELECTOR, value_by="div h1")
page_input_simple.name_page.check_value = "Поле ввода"

page_input_simple.entry_text_field = BaseElement(by=By.CSS_SELECTOR, value_by="div.content input[name='text_string']")

page_input_simple.entry_text_field.check_value = 'tut_bil_Vasia-2'

page_input_simple.button_keyboard_enter = Keys.ENTER

page_input_simple.message_for_check = BaseElement(by=By.CSS_SELECTOR, value_by="div.result p.result-text")
page_input_simple.message_for_check.check_value = 'tut_bil_Vasia-2'

# ------------------------

page_input_email = BasePage(url="https://www.qa-practice.com/elements/input/email")
page_input_email.name_page = BaseElement(by=By.CSS_SELECTOR, value_by="div h1")
page_input_email.name_page.check_value = "Поле ввода"

page_input_email.entry_email_field = BaseElement(by=By.CSS_SELECTOR, value_by="div.content input[name='email']")
page_input_email.entry_email_field.check_value = 'user_name@mail.test'

page_input_email.button_keyboard_enter = Keys.ENTER

page_input_email.message_for_check = BaseElement(by=By.CSS_SELECTOR, value_by="div.result p.result-text")
page_input_email.message_for_check.check_value = 'user_name@mail.test'

# ------------------------

page_input_password = BasePage(url="https://www.qa-practice.com/elements/input/passwd")
page_input_password.name_page = BaseElement(by=By.CSS_SELECTOR, value_by="div h1")
page_input_password.name_page.check_value = "Поле ввода"

page_input_password.entry_password_field = BaseElement(by=By.CSS_SELECTOR,
                                                       value_by="div.content input[name='password']")
page_input_password.entry_password_field.check_value = 'Qwerty*1'

page_input_password.button_keyboard_enter = Keys.ENTER

page_input_password.message_for_check = BaseElement(by=By.CSS_SELECTOR, value_by="div.result p.result-text")
page_input_password.message_for_check.check_value = 'Qwerty*1'


