import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.results_page import ResultPage


class SearchPage(BasePage):
    _search_field = (By.ID, "search_form_input_homepage")

    @allure.step
    def open(self):
        super().navigate_to(super()._URL)
        return self

    @allure.step("search for {text}")
    def search_for(self, text):
        super().get_element(self._search_field).send_keys(text)
        super().get_element(self._search_field).submit()
        return ResultPage(self._driver)
