# pytest -v tests\test_shoes_page.py

import pytest, time
from pages.shoes_page import ShoesPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(driver):
    """Проверяем правильность открытия страницы"""
    page = ShoesPage(driver)
    assert page.title.is_displayed()
    assert 'Обувь' in page.title.text


def test_products_count(driver):
    """Проверяем наличие товаров в категории"""
    page = ShoesPage(driver)
    count = page.count.text
    count = count.split(' ')[0]
    count = int(count[-3:])
    assert count > 0


def test_price_sorting(driver):
    """Проверяем корректность сортировки товаров по цене"""
    page = ShoesPage(driver)
    action = ActionChains(driver)
    action.move_to_element(page.sort).click(page.sort).send_keys(Keys.ARROW_DOWN).\
        send_keys(Keys.ARROW_DOWN).pause(1).send_keys(Keys.ENTER).perform()
    assert 'price' in page.get_query()
    all_prices = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(page.prices))
    assert len(all_prices) > 0

    price_list = []
    for i in range(len(all_prices)):
        price_text = all_prices[i].text.replace(' ', '')
        price_text = float(price_text[:-1])
        price_list.append(price_text)

    if price_list != sorted(price_list):
        driver.execute_script("window.scrollTo(0, 0.09*document.body.scrollHeight);")
        driver.save_screenshot('test_price_sorting_result.png')
    assert price_list == sorted(price_list), "Sort by price doesn't work"


def test_filter_man_cross(driver):
    """Проверяем корректность работы бокового фильтра по подкатегориям обуви"""
    page = ShoesPage(driver)
    page.man_shoes.click()
    cross_shoes = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.cross_shoes))
    cross_shoes.click()
    assert "kedy-i-slipony-muzhskie" in page.get_relative_link()
    shoes_type = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.shoes_type))
    assert "Кеды и слипоны мужские" in shoes_type.text


@pytest.mark.parametrize('name', ['Express — за час!', 'Сегодня', 'Сегодня или завтра', 'До 2 дней', 'До 5 дней'], \
                         ids=['Express', 'Today', 'Tomorrow', '2 days', '5 days'])
def test_delivery(driver, name):
    """Проверяем корректность работы фильтра по времени доставки"""
    page = ShoesPage(driver)
    del_filter, del_type_loc = page.delivery_time(name)
    del_filter.click()
    del_type = WebDriverWait(driver, 10).until(EC.presence_of_element_located(del_type_loc))
    assert name in del_type.text


def test_advbanner(driver):
    """Проверяем кликабельность рекламного баннера"""
    page = ShoesPage(driver)
    banner_list = page.banner
    assert len(banner_list) == 3
    banner_list[1].click()
    assert 'highlight' in page.get_relative_link()


def test_all_filters(driver):
    """Проверяем корректность работы расширенного фильтра"""
    page = ShoesPage(driver)
    filter_button, season, demiseason, submit_button = page.all_filters()
    action = ActionChains(driver)
    action.move_to_element(filter_button).click(filter_button).perform()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(season)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(demiseason)).click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(submit_button)).click()
    filter_param = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.demiseason))
    assert filter_param.is_displayed()


def test_paginator(driver):
    """Проверяем правильность работы пагинатора"""
    page = ShoesPage(driver)
    current_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.current_page))
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", current_page)
    assert current_page.text == '1'
    pages_count = len(page.page_numbers)
    for i in range(pages_count - 3):
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.next_button))
        button.click()
        current_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.current_page))
        driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", current_page)
        assert int(current_page.text) == i + 2
        assert f'page={current_page.text}' in page.get_query()
