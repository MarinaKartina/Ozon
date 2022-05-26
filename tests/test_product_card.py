# pytest -v tests\test_product_card.py

import pytest
from pages.product_card_page import ProductCard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sorting_new(driver):
    """Проверяем правильность сортировки по признаку 'Новинки'"""
    page = ProductCard(driver)
    page.sort_new()
    assert 'new' in page.get_query()
    products = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(page.products))
    assert len(products) > 0
    new_count = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(page.new))
    assert len(new_count) > 0
    for i in range(len(new_count)):
        act = ActionChains(driver)
        act.move_to_element(products[i]).key_down(Keys.CONTROL).click(products[i]).key_up(Keys.CONTROL).perform()
        driver.switch_to.window(driver.window_handles[1])
        new_mark = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.mark_as_new))
        assert new_mark.is_displayed()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


@pytest.mark.parametrize('number', [0, 7, 15], ids=['First card', 'Seventh card', 'Fifteen card'])
def test_product_info_correctly(driver, number):
    """Проверяем, что информация о товаре на странице поиска и на странице товара совпадает"""
    page = ProductCard(driver)
    price1, name1, delivery_date1, seller1 = page.card_inform_common(number)
    page.open_card(number)
    price2, name2, delivery_date2, seller2 = page.product_info()
    assert price1 == price2.text, "Different prices"
    assert name1 == name2.text, "Different names"
    assert delivery_date1 == delivery_date2.text, "Different dates"
    assert seller2.text in seller1, "Different sellers"


def test_photo_gallery(driver, number=1):
    """Проверяем фотогалерею товара на корректность отображения фото и его соответствие миниатюре"""
    page = ProductCard(driver)
    page.open_card(number)
    all_img = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(page.img_gallery))
    for i in range(len(all_img)):
        name = all_img[i].get_attribute('src')
        name = name.split('/')[-1]
        all_img[i].click()
        current_img = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.current_img))
        current_name = current_img.get_attribute('src')
        current_name = current_name.split('/')[-1]
        assert name == current_name


def test_add_in_cart(driver, number=2):
    """Проверяем, что счетчик товаров в корзине корректно работает при добавлении товаров в корзину со страницы поиска"""
    page = ProductCard(driver)
    cart_buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(page.cart_button))
    button1 = cart_buttons[number]
    button2 = cart_buttons[number + 2]
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", button1)
    button1.click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element(button1))
    in_cart = page.in_cart[0]
    assert in_cart.text == '1'
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", button2)
    button2.click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element(button2))
    assert in_cart.text == '2'


def test_product_in_cart(driver):
    """Проверяем, что товар корректно добавляется в корзину со страницы карточки товара"""
    page = ProductCard(driver)
    number = 0
    page.open_card(number)
    while not page.product_in_cart_displayed():
        driver.back()
        number += 1
        page.open_card(number)
    cart_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.add_in_cart))
    cart_button.click()
    cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.product_in_cart))
    assert cart.is_displayed()


def test_favorite(driver, number=0):
    """Проверяем корректность добавления товара в избранное"""
    page = ProductCard(driver)
    page.open_card(number)
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.title)).text
    favorite_count = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(page.favorite_count))[0].text
    favorite = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.favorite))
    favorite.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.in_favorite))
    favorite_count_new = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(page.favorite_count))[0]
    assert int(favorite_count_new.text) == int(favorite_count) + 1
    favorite_count_new.click()
    titles_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(page.favorite_list_names))
    titles = []
    for i in range(len(titles_list)):
        titles.append(titles_list[i].text)
    assert title in titles


@pytest.mark.parametrize('number', [0, 3, 7], ids=['First card', 'Third card', 'Seventh card'])
def test_review_visible(driver, number):
    """Проверяем видимость отзывов о товаре и корректность отображения их количества"""
    page = ProductCard(driver)
    page.open_card(number)
    review = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.review))
    review_count = review.text.split(' ')[0]
    review.click()
    all_reviews = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.review_texts))
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", all_reviews)
    all_reviews_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.review_count)).text
    assert all_reviews_count == review_count


def test_add_to_compare_function(driver, first=0, second=3):
    """Проверяем корректность добавления товаров к сравнению и открытие таблицы сравнения товаров"""
    page = ProductCard(driver)
    page.open_card(first)
    page.add_to_comparison()
    driver.back()
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(page.products))
    page.open_card(second)
    compare_link = page.add_to_comparison()
    compare_link.click()
    compare_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.compare_title))
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", compare_title)
    count = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(page.product_count))
    compare_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.compare_count)).text
    assert int(compare_count) == len(count)
