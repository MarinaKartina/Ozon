from pages.base import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        url = 'https://www.ozon.ru/'
        super().__init__(driver, url)
        driver.get(url)
        self.search_form = driver.find_element(By.XPATH, "//form[@action='/search']")
        self.main_menu = driver.find_elements(By.XPATH, "//ul[@data-widget='horizontalMenu']//a")
        self.catalog_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Каталог')]")
        self.catalog_menu = driver.find_elements(By.XPATH, "//div[@data-widget='catalogMenu']//a/span")
        self.advbanner = driver.find_element(By.XPATH, '//div[@data-widget="advBanner"]')
        self.slide_button = driver.find_element(By.XPATH, '//button[@aria-label="Previous slide"]')
        self.topbar = driver.find_elements(By.XPATH, '//div[@data-widget="topBar"]//a/span')
        self.banner = driver.find_element(By.XPATH, '//div[@data-widget="banner"]')
        self.search_field = driver.find_element(By.XPATH, '//input[@placeholder="Искать на Ozon"]')
        self.search_button = driver.find_element(By.XPATH, '//*[@aria-label="Поиск"]/..')
        self.result_table = driver.find_elements(By.XPATH, '//a[contains(@href, "/product/")]')

    def main_search_field(self, input_text):
        self.search_field.clear()
        self.search_field.send_keys(input_text)
        self.search_button.click()
