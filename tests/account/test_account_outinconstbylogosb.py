import time
from data import Data
from conftest import driver
from conftest import login
from selenium.webdriver.common.by import By


class TestAccountOutInConstByLogoSB:

    def test_account_out_in_const_by_logo_sb(self, driver, login):
        # Найти элемент "Личный кабинет" и кликнуть по нему
        driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()
        # Найти элемент с лого SB и кликнуть по нему
        driver.find_element(By.XPATH, "/html/body/div/div/header/nav/div").click()
        time.sleep(1)
        assert driver.current_url == Data.SB_URL
