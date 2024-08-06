import time
from data import Data
from conftest import driver
from selenium.webdriver.common.by import By


class TestSBLoginButton:

    def test_login_button(self, driver):
        # Найти элемент "Войти в аккаунт" и кликнуть по нему
        driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
        # Найти элемент "Email" и заполнить его из переменной SB_EMAIL
        driver.find_element(By.XPATH, ".//label[text() = 'Email']/parent::*/input").send_keys(Data.SB_EMAIL)
        # Найти элемент "Пароль" и заполнить его из переменной SB_PASSWORD
        driver.find_element(By.XPATH, ".//label[text() = 'Пароль']/parent::*/input").send_keys(Data.SB_PASSWORD)
        # Найти элемент "Войти" и кликнуть по нему
        driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()
        time.sleep(1)
        assert driver.current_url == Data.SB_URL