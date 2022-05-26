from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductCard(BasePage):
    def __init__(self, driver):
        url = 'https://www.ozon.ru/category/nastolnye-igry-dlya-detey-7172/'
        super().__init__(driver, url)
        driver.get(url)
        self.title = (By.TAG_NAME, 'h1')
        self.sort = driver.find_element(By.XPATH, '//div[@role="listbox"]')
        self.products = (By.XPATH, '//a[@class="i2u tile-hover-target"]')
        self.new = (By.XPATH, '//span[@style="color: var(--ozAccentSecondary);"]')
        self.mark_as_new = (By.XPATH, '//span[@title="Впервые появившийся в продаже на OZON.ru товар"]')

        self.prices = (By.XPATH, '//div[@data-widget="searchResultsV2"]//span[@class="ui-u ui-u1 ui-u6"]')
        self.names = (By.XPATH, '//a[@class="tile-hover-target t4i"]/span/span')
        self.delivery_dates = (By.XPATH, '//span[contains(text(), "доставит")]/b/font')
        self.sellers = (By.XPATH, '//span[contains(text(), "доставит")]')

        self.img_gallery = (By.XPATH, '//div[@class="oj7"]//img')
        self.current_img = (By.XPATH, '//div[@class="j2o"]//img')

        self.cart_button = (By.XPATH, '//div[@class="iu6 u6i"]//span[contains(text(), "В корзину")]')
        self.in_cart = driver.find_elements(By.XPATH, '//a[@href="/cart"]/span')
        self.count_in_cart = (By.XPATH, '//span[contains(text(), "шт.")]')
        self.add_in_cart = (By.XPATH, '//span[contains(text(), "Добавить в корзину")]')
        self.product_in_cart = (By.XPATH, '//span[contains(text(), "В корзине")]')

        self.favorite = (By.XPATH, '//span[contains(text(), "В избранное")]')
        self.favorite_count = (By.XPATH, '//a[@href="/my/favorites"]/span')
        self.favorite_list_names = (By.XPATH, '//a[@class="tile-hover-target t4i"]/span/span')
        self.in_favorite = (By.XPATH, '//span[contains(text(), "В избранном")]')

        self.review = (By.XPATH, '//div[contains(text(), "отзыв")]')
        self.review_texts = (By.XPATH, '//a[contains(text(), "Отзывы и вопросы о товаре")]')
        self.review_count = (By.XPATH, '//div[@data-widget="webReviewsTitle"]/div')

        self.compare_title = (By.XPATH, '//div[contains(text(), "Сравнение товаров")]')
        self.product_count = (By.XPATH, '//div[@class="m8k ui-b0"]')
        self.compare_count = (By.XPATH, '//span[@class="ui-d6a ui-da7"]')

    def sort_new(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.sort).click(self.sort).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    def card_inform_common(self, number):
        price = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.prices))[number].text
        name = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.names))[number].text
        delivery_date = WebDriverWait(self.driver, 10). \
            until(EC.presence_of_all_elements_located(self.delivery_dates))[number].text.lower()
        seller = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.sellers))[number].text
        seller = seller.split(',')[-1]
        return price, name, delivery_date, seller

    def open_card(self, number):
        products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.products))
        assert len(products) >= number
        self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", products[number])
        products[number].click()

    def product_info(self):
        price = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                     ((By.XPATH, '//span[@class="ql3 q3l"]/span')))
        name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        delivery_date = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                     ((By.XPATH, '//span[contains(text(), "Доставка")]/../span[@class="jr2"]')))
        seller = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                     ((By.XPATH, '//div[@data-widget="webCurrentSeller"]//a[@title]')))
        return price, name, delivery_date, seller

    def product_in_cart_displayed(self):
        try:
            can_add_in_cart = self.driver.find_element(By.XPATH, '//span[contains(text(), "Добавить в корзину")]')
            return can_add_in_cart
        except:
            return False

    def add_to_comparison(self):
        add_to_comparison = self.driver.find_element(By.XPATH, '//span[contains(text(), "Добавить к сравнению")]')
        add_to_comparison.click()
        in_comparison = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                        ((By.XPATH, '//div[contains(text(), "Перейти в сравнение")]')))
        return in_comparison
