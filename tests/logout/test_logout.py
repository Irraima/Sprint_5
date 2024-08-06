import time
from conftest import driver
from conftest import login
from selenium.webdriver.common.by import By


class TestLogout:

    def test_logout(self, driver, login):
        # Найти элемент "Личный кабинет" и кликнуть по нему
        driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()
        time.sleep(1)
        # Найти элемент "Выход" и кликнуть по нему
        driver.find_element(By.XPATH, ".//button[text() = 'Выход']").click()
        time.sleep(3)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
