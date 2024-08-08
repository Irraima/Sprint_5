import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from data import Data


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.SB_URL)

    yield chrome_driver

    chrome_driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
    driver.find_element(By.XPATH, ".//label[text() = 'Email']/parent::*/input").send_keys(Data.SB_EMAIL)
    driver.find_element(By.XPATH, ".//label[text() = 'Пароль']/parent::*/input").send_keys(Data.SB_PASSWORD)
    driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()