from locators import Locators
from conftest import driver
from conftest import login
from data import Data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAccountOutInConstByConstButton:

    def test_account_out_in_const_by_const_button(self, driver, login):
        # Найти элемент "Личный кабинет" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.AC_BUTTON).click()
        # Найти элемент "Конструктор" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.CONST_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "button")))
        assert driver.current_url == Data.SB_URL
