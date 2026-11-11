from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_btn = (By.ID, 'login-button')
        self.supplies = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        self.bucket = (
            By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        self.checkout_btn = (By.ID, "checkout")
        self.locator_id = ["first-name",
                           "last-name",
                           "postal-code"]
        self.value = ["Татьяна",
                      "Соколова",
                      "666666"]
        self.continue_btn = (By.ID, "continue")
        self.total_label = (
            By.CSS_SELECTOR, "[data-test='total-label']")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self):
        username_input = self.wait.until(
            EC.element_to_be_clickable(self.username_input))
        username_input.clear()
        username_input.send_keys("standard_user")
        password_input = self.wait.until(
            EC.element_to_be_clickable(self.password_input))
        password_input.clear()
        password_input.send_keys("secret_sauce")
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.login_btn))
        login_btn.click()

    def add_to_bucket(self):
        for i in self.supplies:
            add_btn = self.wait.until(EC.element_to_be_clickable((
                By.XPATH,
                f"//div[@class='inventory_item_description']"
                f"[.//div[text()='{i}']]//button[text()='Add to cart']")))
            add_btn.click()

    def open_bucket(self):
        bucket = self.wait.until(EC.element_to_be_clickable(self.bucket))
        bucket.click()

    def checkout(self):
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable(self.checkout_btn))
        checkout_btn.click()

    def filled_form(self):
        for locator, value in zip(self.locator_id, self.value):
            form = self.wait.until(
                EC.element_to_be_clickable((By.ID, locator)))
            form.send_keys(value)
        continue_btn = self.wait.until(
            EC.element_to_be_clickable(self.continue_btn))
        continue_btn.click()

    def check_result(self):
        total_label = self.wait.until(
            EC.visibility_of_element_located(self.total_label))
        total_sum = total_label.text[7:]
        return total_sum
