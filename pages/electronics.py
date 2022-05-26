from pages.base import BasePage
from selenium.webdriver.common.by import By


class ElectronicsPage(BasePage):
    def __init__(self, driver):
        url = 'https://www.ozon.ru/category/elektronika-15500/'
        super().__init__(driver, url)
        driver.get(url)
        self.main_menu = self.driver.find_elements(By.XPATH, '//div[@data-widget="catalogHorizontalMenu"]//a')
        self.title = (By.TAG_NAME, 'h1')
        self.quadrocopter = self.driver.find_element(By.XPATH, '//div[contains(text(), "Квадрокоптеры")]')
        self.vidgets = self.driver.find_elements(By.XPATH, '//div[@data-widget="objectLine"]//a[contains(@href, "/category/")]')
