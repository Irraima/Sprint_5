from locators import Locators
from conftest import driver
from data import Data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSBRegister:

    def test_register(self, driver):
        # Найти элемент "Личный кабинет" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.AC_BUTTON).click()
        # Найти элемент "Зарегистрироваться" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.ALT_REG_BUTTON).click()
        # Найти элемент "Имя" и заполнить его из переменной SB_NAME
        driver.find_element(By.XPATH, Locators.NAME_INPUT).send_keys(Data.SB_NAME)
        # Найти элемент "Email" и заполнить его из переменной SB_EMAILREG
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Data.SB_EMAILREG)
        # Найти элемент "Пароль" и заполнить его из переменной SB_PASSWORD
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(Data.SB_PASSWORD)
        # Найти элемент "Зарегистрироваться" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_BUTTON)))
        url = "https://stellarburgers.nomoreparties.site/login"
        assert driver.current_url == url
