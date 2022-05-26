from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FirstFooter(BasePage):
    def __init__(self, driver):
        url = 'https://www.ozon.ru/'
        super().__init__(driver, url)
        driver.get(url)

        self.body = driver.find_element(By.TAG_NAME, 'body')
        self.footer = (By.XPATH, '//footer')
        self.page_title = (By.ID, 'pageTitle')

        self.your_goods = (By.XPATH, '//a[@title = "Ваши товары на Ozon"]')
        self.sell_on_ozon = (By.XPATH, '//a[@title = "Продавайте на Ozon"]')
        self.ozon_box = (By.XPATH, '//a[@title = "Установите постамат Ozon Box"]')
        self.new_point = (By.XPATH, '//a[@title = "Откройте пункт выдачи Ozon"]')
        self.supplier = (By.XPATH, '//a[@title = "Стать Поставщиком Ozon"]')
        self.what_to_sell = (By.XPATH, '//a[@title = "Что продавать на Ozon"]')
        self.ozon_global = (By.XPATH, '//a[@title = "Selling on Ozon"]')

        self.help_links = (By.XPATH, '//span[contains(text(), "Помощь")]/../a')

    def scroll_to_footer(self):
        self.body.send_keys(Keys.END)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.footer))
        self.body.send_keys(Keys.END)


class SecondFooter(BasePage):
    def __init__(self, driver):
        url = 'https://www.ozon.ru/'
        super().__init__(driver, url)
        driver.get(url)

        self.body = driver.find_element(By.TAG_NAME, 'body')
        self.footer = (By.XPATH, '//footer')
        self.safety_service = (By.XPATH, '//img[@alt="Зона безопасного сервиса"]')
        self.vacancy = driver.find_element(By.XPATH, '//a[contains(text(), "Ozon Вакансии")]')
        self.travel = driver.find_element(By.XPATH, '//a[contains(text(), "OZON Travel")]')
        self.it_course = driver.find_element(By.XPATH, '//a[contains(text(), "Route 256")]')
        self.litres = driver.find_element(By.XPATH, '//a[contains(text(), "LITRES.ru")]')

    def scroll_to_footer(self):
        self.body.send_keys(Keys.END)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.footer))
        self.body.send_keys(Keys.END)
