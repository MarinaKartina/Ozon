# pytest -v tests\test_footers.py

import time
import pytest

from pages.footers import FirstFooter, SecondFooter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.xfail
def test_safety_icon_clickable(driver):
    """Проверяем кликабельность изображения-ссылки в нижней плашке футера"""
    page = SecondFooter(driver)
    page.scroll_to_footer()
    safety_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.safety_service))
    safety_icon.click()
    driver.switch_to.window(driver.window_handles[1])
    assert page.get_url() == 'https://ecomvscovid.ru/'


@pytest.mark.xfail
def test_vacancy_link_clickable(driver):
    """Проверяем кликабельность ссылки в нижней плашке футера"""
    page = SecondFooter(driver)
    page.scroll_to_footer()
    page.vacancy.click()
    assert page.get_url() == 'https://job.ozon.ru/'


@pytest.mark.xfail
def test_travel_link_clickable(driver):
    """Проверяем кликабельность ссылки в нижней плашке футера"""
    page = SecondFooter(driver)
    page.scroll_to_footer()
    page.travel.click()
    assert page.get_url() == 'https://www.ozon.ru/travel/?perehod=mainpagebottom'


@pytest.mark.xfail
def test_it_courses_link_clickable(driver):
    """Проверяем кликабельность ссылки в нижней плашке футера"""
    page = SecondFooter(driver)
    page.scroll_to_footer()
    page.it_course.click()
    assert page.get_url() == 'https://route256.ozon.ru/'


@pytest.mark.xfail
def test_litres_link_clickable(driver):
    """Проверяем кликабельность ссылки в нижней плашке футера"""
    page = SecondFooter(driver)
    page.scroll_to_footer()
    page.litres.click()
    assert page.get_url() == 'https://www.litres.ru/'


def test_ozon_links_clickable_your_goods(driver):
    """Проверяем кликабельность ссылки в футере в разделе 'Зарабатывайте с Ozon'"""
    page = FirstFooter(driver)
    page.scroll_to_footer()
    link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.your_goods))
    link.click()
    assert page.get_url() == 'https://seller.ozon.ru/'


def test_ozon_links_clickable_sell_on_ozon(driver):
    """Проверяем кликабельность ссылки в футере в разделе 'Зарабатывайте с Ozon'"""
    page = FirstFooter(driver)
    page.scroll_to_footer()
    link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.sell_on_ozon))
    link.click()
    assert 'https://seller.ozon.ru/' in page.get_url()


def test_ozon_links_clickable_ozon_box(driver):
    """Проверяем кликабельность ссылки в футере в разделе 'Зарабатывайте с Ozon'"""
    page = FirstFooter(driver)
    page.scroll_to_footer()
    link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.ozon_box))
    link.click()
    assert '/ozon-box/' in page.get_url()


def test_ozon_links_clickable_new_point(driver):
    """Проверяем кликабельность ссылки в футере в разделе 'Зарабатывайте с Ozon'"""
    page = FirstFooter(driver)
    page.scroll_to_footer()
    link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.new_point))
    link.click()
    assert 'https://business.ozon.ru/' in page.get_url()


def test_ozon_links_clickable_supplier(driver):
    """Проверяем кликабельность ссылки в футере в разделе 'Зарабатывайте с Ozon'"""
    page = FirstFooter(driver)
    page.scroll_to_footer()
    links = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.supplier))
    links.click()
    assert 'https://business.ozon.ru/' in page.get_url()


def test_ozon_links_clickable_what_to_sell(driver):
    """Проверяем кликабельность ссылки в футере в разделе 'Зарабатывайте с Ozon'"""
    page = FirstFooter(driver)
    page.scroll_to_footer()
    link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.what_to_sell))
    link.click()
    assert 'https://seller.ozon.ru/' in page.get_url()


def test_ozon_links_clickable_ozon_global(driver):
    """Проверяем кликабельность ссылки в футере в разделе 'Зарабатывайте с Ozon'"""
    page = FirstFooter(driver)
    page.scroll_to_footer()
    link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.ozon_global))
    link.click()
    assert page.get_url() == 'https://global.ozon.com/'


def test_help_links(driver):
    """Проверяем кликабельность ссылок в футере в разделе 'Помощь'"""
    page = FirstFooter(driver)
    page.scroll_to_footer()
    help_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(page.help_links))
    time.sleep(3)
    for i in range(len(help_links)):
        action = ActionChains(driver)
        action.context_click(help_links[i]).perform()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.page_title))
        assert 'docs.ozon.ru/common' in page.get_url()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
