from selenium.webdriver.common.by import By

from objects.base_page import BasePage
from objects.base_element import BaseElement

page_index = BasePage(url="https://www.qa-practice.com/")
page_index.link_input_text = BaseElement(by=By.XPATH, value_by='//*[@id="content"]/div/ol/li[1]/a')
