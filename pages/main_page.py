from pages.base import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(self, driver)
        url = 'https://www.ozon.ru/'
        driver.get(url)
        self.search_form = driver.find_element(By.XPATH, "//form[@action='/search']")
        self.main_menu = driver.find_elements(By.XPATH, "//ul[@data-widget='horizontalMenu']//a")
        self.catalog_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Каталог')]")
        self.catalog_menu = driver.find_elements(By.XPATH, "//div[@data-widget='catalogMenu']//a/span")
        self.advbanner = driver.find_element(By.XPATH, '//div[@data-widget="advBanner"]')
        self.slide_button = driver.find_element(By.XPATH, '//button[@aria-label="Next slide"]')
        self.topbar = driver.find_elements(By.XPATH, '//div[@data-widget="topBar"]//a/span')

