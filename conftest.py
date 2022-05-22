import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.quit()
