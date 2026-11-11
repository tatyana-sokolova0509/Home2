from lesson_07.calculator_page import CalculatorPage
from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    page = CalculatorPage(driver)
    page.open()
    page.type_value(45)
    page.press_buttons()
    page.check_result()
    assert page.check_result() == "15"
