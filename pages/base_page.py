from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    _URL = "http://duckduckgo.com"

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    def navigate_to(self, url):
        self._driver.get(url)

    def get_element(self, locator: tuple, timeout=5):
        return WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_element_located(locator), ' : '.join(locator))

    def get_elements(self, locator: tuple, timeout=5):
        return WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_any_elements_located(locator), ' : '.join(locator))
