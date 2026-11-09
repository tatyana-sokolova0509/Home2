from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    username_input = wait.until(EC.element_to_be_clickable((
        By.ID, 'user-name')))
    username_input.clear()
    username_input.send_keys("standard_user")
    password_input = wait.until(EC.element_to_be_clickable((
        By.ID, 'password')))
    password_input.clear()
    password_input.send_keys("secret_sauce")
    login_btn = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
    login_btn.click()
    supplies = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for i in supplies:
        add_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            f"//div[@class='inventory_item_description']"
            f"[.//div[text()='{i}']]//button[text()='Add to cart']")))
        add_btn.click()
    bucket = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "[data-test='shopping-cart-link']")))
    bucket.click()

    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    locator_id = ["first-name",
                  "last-name",
                  "postal-code"]
    value = ["Татьяна",
             "Соколова",
             "666666"]
    for locator, value in zip(locator_id, value):
        form = wait.until(EC.element_to_be_clickable((By.ID, locator)))
        form.send_keys(value)
    continue_btn = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    continue_btn.click()
    total_label = wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "[data-test='total-label']")))
    total_sum = total_label.text[7:]

    driver.quit()

    assert total_sum == "$58.29"
