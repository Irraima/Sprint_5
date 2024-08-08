from locators import Locators
from conftest import driver
from data import Data
from selenium.webdriver.common.by import By


class TestSBRegisterShortPassword:

    def test_register_short_password(self, driver):
        # Найти элемент "Личный кабинет" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.AC_BUTTON).click()
        # Найти элемент "Зарегистрироваться" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.ALT_REG_BUTTON).click()
        # Найти элемент "Имя" и заполнить его из переменной SB_NAME
        driver.find_element(By.XPATH, Locators.NAME_INPUT).send_keys(Data.SB_NAME)
        # Найти элемент "Email" и заполнить его из переменной SB_EMAILREG
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Data.SB_EMAILREG)
        # Найти элемент "Пароль" и заполнить его значением "123"
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys('123')
        # Найти элемент "Зарегистрироваться" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.REG_BUTTON).click()
        assert driver.find_element(By.XPATH, Locators.PASSWORD_ERROR)

