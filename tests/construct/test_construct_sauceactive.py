from locators import Locators
from conftest import driver
from conftest import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructBunActive:

    def test_construct_bun_active(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "img")))
        # Найти элемент "Соусы" и кликнуть по нему
        driver.find_element(By.XPATH, Locators.SAUCE).click()
        assert driver.find_element(By.XPATH, Locators.SAUCE_ACTIVE)
