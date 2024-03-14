from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, url):
        self.driver = None
        self.url = url

    def activate_page(self, driver):
        self.driver = driver
        if self.driver.current_url not in ('data:,',):
            self.check_url()
            return True
        else:
            self.driver.get(url=self.url)

    def find_and_save_element(self, element):
        try:
            tmp = self.driver.find_element(element.by, element.value_by)
        except NoSuchElementException(">> Error. 'by' and 'value_by' can't find element on the page."):
            return False
        element.save(tmp)
        return True

    def check_find_and_save_element(self, element):
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

    @classmethod
    def click_on_link(cls, element):
        if element.is_present():
            element.click_element()
        else:
            assert False, "NoSuchElementException >> Error. Not such element in this page. Try use function " \
                          "'find_element' or 'check_and_find_element' before to do it."

    @classmethod
    def is_displayed(cls, element):
        if element.is_present():
            assert element.is_displayed(), "NoSuchAttributeException >> Error. Element not displayed in page."
        else:
            assert False, "NoSuchElementException >> Error. Not such element in this page. Try use function " \
                          "'find_element' or 'check_and_find_element' before to do it."

    def check_url(self):
        tmp = self.driver.current_url
        assert tmp == self.url, f">> Error. Not correct url on the page. Url in driver: '{tmp}'."

    @classmethod
    def send_strung_on_element(cls, element, string):
        element.send_keys(string)

    def put_button_on_the_keyboard(self, keyboard_button):
        action = ActionChains(self.driver)
        action.send_keys(keyboard_button)
        action.perform()

    @classmethod
    def check_attribute_text(cls, element):
        tmp = element.element.get_attribute('innerHTML')
        assert tmp == element.check_value, \
            f">> Error. Not correct attribute 'innerHTML': '{tmp}'. Expected 'check_value':'{element.check_value}'."
