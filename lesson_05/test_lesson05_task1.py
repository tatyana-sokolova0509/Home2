from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    link_form = driver.find_element(By.XPATH, "//a[text()='HTML Form']")
    link_form.click()
    assert driver.current_url == "https://httpbin.qa-territory.online/forms/post"
    driver.back()
    assert driver.current_url == "https://httpbin.qa-territory.online/"
    driver.quit()
