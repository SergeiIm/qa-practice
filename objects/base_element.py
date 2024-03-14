

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
        self.element.click()

    def check_activity(self):
        self.element.is_displayed()

    def send_keys(self, value):
        self.element.send_keys(value)

