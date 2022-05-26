from pages.base import BasePage
from selenium.webdriver.common.by import By


class ShoesPage(BasePage):
    def __init__(self, driver):
        url = 'https://www.ozon.ru/category/obuv-17777/'
        super().__init__(driver, url)
        driver.get(url)
        self.title = driver.find_element(By.TAG_NAME, 'h1')
        self.count = driver.find_element(By.XPATH, '//div[@data-widget="catalogResultsHeader"]/div')
        self.sort = driver.find_element(By.XPATH, '//div[@role="listbox"]')
        self.prices = (By.XPATH, '//div[@data-widget="searchResultsV2"]//span[@class="ui-u ui-u1 ui-u6"]')
        self.man_shoes = driver.find_element(By.XPATH, '//a[contains(text(), "Мужчинам")]')
        self.cross_shoes = (By.XPATH, '//a[contains(text(), " Кеды, кроссовки и слипоны")]')
        self.shoes_type = (By.TAG_NAME, 'h1')
        self.banner = driver.find_elements(By.XPATH, '//div[@data-widget="objectBannerList"]//a')
        self.demiseason = (By.XPATH, '//span[contains(text(), "Сезон: Демисезон")]')
        self.page_numbers = driver.find_elements(By.XPATH, '//div[@class="w2u"]//a')
        self.current_page = (By.XPATH, '//a[@class="w0u u1w"]')
        self.next_button = (By.XPATH, '//div[contains(text(), "Дальше")]')

    def delivery_time(self, value):
        delivery_filter = self.driver.find_element(By.XPATH, f'//span[contains(text(), {value!r})]')
        del_type = 'Сроки доставки: ' + value
        delivery_type = (By.XPATH, f'//span[contains(text(), {del_type!r})]')
        return delivery_filter, delivery_type

    def all_filters(self):
        all_filters_button = self.driver.find_element(By.XPATH, '//button//span[contains(text(), "Все фильтры")]')
        season = (By.XPATH, '//span[contains(text(), "Сезон")]')
        demiseason = (By.XPATH, '//span[contains(text(), "Демисезон")]')
        submit_button = (By.XPATH, '//span[@class="ui-c4 ui-c7"]/..')
        return all_filters_button, season, demiseason, submit_button
