from locators import Locators
from conftest import driver
from conftest import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogout:

    def test_logout(self, driver, login):
        # Найти элемент "Личный кабинет" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.AC_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "input")))
        # Найти элемент "Выход" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.RES_PASS_BUTTON)))
        url = "https://stellarburgers.nomoreparties.site/login"
        assert driver.current_url == url
