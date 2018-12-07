from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ImagesPage(BasePage):
    images = (By.XPATH, "//div[@class='tile-wrap']//img")
