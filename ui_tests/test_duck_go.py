import pytest

from pages.images_page import ImagesPage
from pages.search_page import SearchPage


def send_test_data():
    return ["python", "Python", "kitty"]


class TestDuckGo:
    @pytest.mark.uitest
    @pytest.mark.parametrize("text", send_test_data())
    def test_verify_search(self, driver, text: str):
        result_page = SearchPage(driver).open().search_for(text)
        actual_result = result_page.get_result_link_text(2)

        assert text.lower() in actual_result.lower()

    @pytest.mark.uitest
    @pytest.mark.skip(reason="Test")
    def test_verify_images(self, driver, text):
        result_page = SearchPage(driver).open().search_for(text)
        images_page = result_page.switch_to_images_page()

        images = images_page.get_elements(ImagesPage.images)[:5]
        for image in images:
            assert image.is_displayed()
