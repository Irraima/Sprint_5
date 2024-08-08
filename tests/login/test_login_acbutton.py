from locators import Locators
from conftest import driver
from data import Data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSBLoginAcButton:

    def test_login_ac_button(self, driver):
        # Найти элемент "Личный кабинет" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.AC_BUTTON).click()
        # Найти элемент "Email" и заполнить его из переменной SB_EMAIL
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(Data.SB_EMAIL)
        # Найти элемент "Пароль" и заполнить его из переменной SB_PASSWORD
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(Data.SB_PASSWORD)
        # Найти элемент "Войти" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "img")))
        assert driver.current_url == Data.SB_URL
