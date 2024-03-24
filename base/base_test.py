import pytest
from config.data import Data
from pages.page_single_line_input_text_field import PageSingleLineInputTextField


class BaseTest:

    data: Data

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.page_single_line_input_text_field: PageSingleLineInputTextField = \
            PageSingleLineInputTextField(driver)

