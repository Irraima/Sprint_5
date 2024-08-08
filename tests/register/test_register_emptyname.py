from locators import Locators
from conftest import driver
from data import Data
from selenium.webdriver.common.by import By


class TestSBRegisterEmptyName:

    def test_register_empty_name(self, driver):
        # Найти элемент "Личный кабинет" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.AC_BUTTON).click()
        # Найти элемент "Зарегистрироваться" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.ALT_REG_BUTTON).click()
        # Найти элемент "Email" и заполнить его из переменной SB_EMAILREG
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Data.SB_EMAILREG)
        # Найти элемент "Пароль" и заполнить его из переменной SB_PASSWORD
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(Data.SB_PASSWORD)
        # Найти элемент "Зарегистрироваться" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.REG_BUTTON).click()
        url = "https://stellarburgers.nomoreparties.site/register"
        assert driver.current_url == url
