from .base import BasePage
from selenium.webdriver.common.by import By

class ShoesPage(BasePage):
    def __init__(self, driver):
        super().__init__(self, driver)
        url = 'https://www.ozon.ru/category/obuv-17777/'
        driver.get(url)
        self.title = driver.find_element(By.TAG_NAME,'h1')