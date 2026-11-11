from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.delay_input = (By.ID, "delay")
        self.locators = [(By.XPATH, "//span[text()='7']"),
                         (By.XPATH, "//span[text()='+']"),
                         (By.XPATH, "//span[text()='8']"),
                         (By.XPATH, "//span[text()='=']")
                         ]
        self.result = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(
            f"https://bonigarcia.dev/"
            f"selenium-webdriver-java/slow-calculator.html")

    def type_value(self, value: int):
        delay_input = self.wait.until(
            EC.element_to_be_clickable(self.delay_input))
        delay_input.clear()
        delay_input.send_keys(value)

    def press_buttons(self):
        for locator in self.locators:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()

    def check_result(self):
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(self.result, "15"))
        res = self.driver.find_element(*self.result).text
        return res
