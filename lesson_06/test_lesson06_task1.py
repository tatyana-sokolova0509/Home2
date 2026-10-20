from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[text()='Start']"
    )))
    start_btn.click()
    message = wait.until(EC.visibility_of_element_located((
        By.XPATH, "//h4[text()='Hello World!']")))
    driver.save_screenshot("lesson_06/screen/message_hello.png")
    assert driver.execute_script("return arguments[0].textContent;", message) == "Hello World!"

    driver.quit()
