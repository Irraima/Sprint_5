import time
from data import Data
from conftest import driver
from selenium.webdriver.common.by import By


class TestSBRegisterShortPassword:

    def test_register_short_password(self, driver):
        # Найти элемент "Личный кабинет" и кликнуть по нему
        driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()
        # Найти элемент "Зарегистрироваться" и кликнуть по нему
        driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
        # Найти элемент "Имя" и заполнить его из переменной SB_NAME
        driver.find_element(By.XPATH, ".//label[text() = 'Имя']/parent::*/input").send_keys(Data.SB_NAME)
        # Найти элемент "Email" и заполнить его из переменной SB_EMAILREG
        driver.find_element(By.XPATH, ".//label[text() = 'Email']/parent::*/input").send_keys(Data.SB_EMAILREG)
        # Найти элемент "Пароль" и заполнить его значением "123"
        driver.find_element(By.XPATH, ".//label[text() = 'Пароль']/parent::*/input").send_keys('123')
        # Найти элемент "Зарегистрироваться" и кликнуть по нему
        driver.find_element(By.XPATH, ".//button[text() = 'Зарегистрироваться']").click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, ".//p[text() = 'Некорректный пароль']")

