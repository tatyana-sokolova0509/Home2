from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    url = "https://httpbin.qa-territory.online/forms/post"
    driver.get(url)
    input_custname = driver.find_element(By.NAME, "custname")
    input_custname.send_keys("Соколова Татьяна")
    btn_submit = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn_submit.click()
    assert driver.current_url != url
    driver.quit()
