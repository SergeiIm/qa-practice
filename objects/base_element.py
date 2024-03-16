

class BaseElement:
    def __init__(self, by, value_by: str):
        self.by = by
        self.value_by = value_by
        self.element = None
        self.check_value = None

    def save(self, element):
        self.element = element

    def is_present(self):
        return True if self.element else False

    def click_element(self):
        if not self.is_present():
            assert False, f"NoSuchElementException >> Error. Not such element '{self}' in this page. Try use function" \
                           " 'find_element' or 'check_and_find_element' before to do it."
        self.element.click()

    def check_is_displayed(self):
        if self.is_present():
            assert self.element.is_displayed(), "NoSuchAttributeException >> Error. Element not displayed in page."
        else:
            assert False, "NoSuchElementException >> Error. Not such element '{self}' in this page. Try use function " \
                          "'find_element' or 'check_and_find_element' before to do it."

    def input_string(self, value):
        self.element.send_keys(value)

    def check_attribute_text(self):
        tmp = self.element.get_attribute('innerHTML')
        assert tmp == self.check_value, \
            f">> Error. Not correct attribute 'innerHTML': '{tmp}'. Expected 'check_value':'{self.check_value}'."
