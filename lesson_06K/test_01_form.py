from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    locator_names = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]
    values = [
        "Иван",
        "Петров",
        "Ленина, 55-3",
        "test@skypro.com",
        "+7985899998787",
        "Москва",
        "Россия",
        "QA",
        "SkyPro",
    ]
    for locator, value in zip(locator_names, values):
        element = wait.until(EC.element_to_be_clickable((By.NAME, locator)))
        element.send_keys(value)

    submit_btn = wait.until(EC.element_to_be_clickable((
        By.CLASS_NAME, "btn-outline-primary")))
    submit_btn.click()

    zip_code_input = wait.until(EC.visibility_of_element_located((
        By.ID, "zip-code")))
    assert "alert-danger" in zip_code_input.get_attribute("class")

    for locator, value in zip(locator_names, values):
        element = wait.until(EC.visibility_of_element_located((
            By.ID, locator)))
        assert "alert-success" in element.get_attribute("class")

    driver.quit()
