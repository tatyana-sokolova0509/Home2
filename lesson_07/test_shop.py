from lesson_07.shop_page import ShopPage
from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    page = ShopPage(driver)
    page.open()
    page.login()
    page.add_to_bucket()
    page.open_bucket()
    page.checkout()
    page.filled_form()

    assert page.check_result() == "$58.29"
