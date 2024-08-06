import time
from data import Data
from conftest import driver
from conftest import login
from selenium.webdriver.common.by import By


class TestAccountOutInConstByConstButton:

    def test_account_out_in_const_by_const_button(self, driver, login):
        # Найти элемент "Личный кабинет" и кликнуть по нему
        driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()
        # Найти элемент "Конструктор" и кликнуть по нему
        driver.find_element(By.XPATH, ".//p [text() = 'Конструктор']").click()
        time.sleep(1)
        assert driver.current_url == Data.SB_URL
