import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.images_page import ImagesPage


class ResultPage(BasePage):
    _result_links = (By.CSS_SELECTOR, ".result__title a.result__a")
    _images_tab_link = (By.XPATH, "//a[@data-zci-link='images']")

    @allure.step
    def open_result_link(self, position):
        super().get_elements(self._result_links)[position - 1].click()

    @allure.step
    def get_result_link_text(self, position) -> str:
        return super().get_elements(self._result_links, 20)[position-1].text

    @allure.step
    def switch_to_images_page(self):
        super().get_element(self._images_tab_link).click()
        return ImagesPage(self._driver)
