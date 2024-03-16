from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from objects.base_element import BaseElement


class BasePage:

    url: str = None

    def __init__(self, driver):
        self.driver = driver
        if self.driver.current_url not in ('', 'data:,'):
            self.check_url_page()
        else:
            self.go_to_url_page()

    def go_to_url_page(self):
        self.driver.get(self.url)

    def find_and_save_element(self, element: BaseElement):
        try:
            tmp = self.driver.find_element(element.by, element.value_by)
        except NoSuchElementException(">> Error. 'by' and 'value_by' can't find element on the page."):
            return False
        element.save(tmp)
        return True

    def check_find_and_save_element(self, element: BaseElement):
        tmp = self.driver.find_elements(element.by, element.value_by)
        if len(tmp) > 1:
            assert False, f"NoSuchElementException >> Error. 'by' and 'value_by' get more one '{len(tmp)}'" \
                          f" elements on the page. Change 'by' and 'value_by' for this element."
        elif len(tmp) < 1:
            assert False, "NoSuchElementException >> Error. 'by' and 'value_by' can't find element on the page. " \
                          f"Change 'by': '{element.by}' and 'value_by':'{element.value_by}' for this element."
        else:
            element.save(tmp[0])
            return True

    def check_url_page(self):
        tmp = self.driver.current_url
        assert tmp == self.url, f">> Error. Not correct url on the page. Url in driver: '{tmp}', expected: {self.url}."

    def put_button_on_the_keyboard(self, keyboard_button):
        action = ActionChains(self.driver)
        action.send_keys(keyboard_button)
        action.perform()
