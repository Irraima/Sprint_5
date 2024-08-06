import time
from conftest import driver
from conftest import login
from selenium.webdriver.common.by import By


class TestConstructBunActive:

    def test_construct_bun_active(self, driver, login):
        time.sleep(5)
        # Найти элемент "Начинки" и кликнуть по нему
        driver.find_element(By.XPATH, ".//span[text() = 'Начинки']").click()
        assert driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3][contains(@class, 'type_current')]")