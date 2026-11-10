from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = wait.until(EC.element_to_be_clickable((By.ID, "delay")))
    delay_input.clear()
    delay_input.send_keys("45")
    locators = ["//span[text()='7']",
                "//span[text()='+']",
                "//span[text()='8']",
                "//span[text()='=']"
                ]
    for locator in locators:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()
    wait = WebDriverWait(driver, 45)
    wait.until_not(EC.text_to_be_present_in_element((
        By.CLASS_NAME, "screen"), "7+8"))
    result = driver.find_element(By.CLASS_NAME, "screen")
    assert result.text == "15"

    driver.quit()
