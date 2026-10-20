from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "OGQ2OTY5OWYtOTA2Zi00ZDZlLTg2YzEtN2E0MmM5N2UzYWEx",
        "domain": "gitflic.ru", })
    driver.refresh()
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/t_kondratenko")
    user1_url = driver.current_url
    driver.delete_all_cookies()
    driver.add_cookie({
        "name": "SESSION",
        "value": "NGY0NGQyYzAtYjAyNS00NDBkLWFiYzQtMTYwMzg0NGRiOWYy",
        "domain": "gitflic.ru", })
    driver.refresh()
    driver.get("https://gitflic.ru/user/airsworld")
    user2_url = driver.current_url
    assert user1_url != user2_url

    driver.quit()
