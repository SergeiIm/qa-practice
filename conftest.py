import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_Chrome
from selenium.webdriver.firefox.options import Options as Options_Firefox
from selenium.webdriver.safari.options import Options as Options_Safari


@pytest.fixture(autouse=True, scope='function')
def driver():
    options = Options_Chrome()
    options.add_argument("--headless")  # запуск без отображения.
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
