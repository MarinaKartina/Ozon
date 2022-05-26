# pytest -v tests\test_main_page.py

import pytest
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_search_form_visible(driver):
    """Проверяем наличие формы поиска на странице"""
    page = MainPage(driver)
    assert page.search_form.is_displayed()


@pytest.mark.parametrize('name', ['Кофе', 'Стул'], ids=['Coffee', 'Chair'])
def test_check_main_search(driver, name):
    """Проверяем корректность работы формы поиска"""
    page = MainPage(driver)
    assert page.search_field.is_displayed()
    page.main_search_field(name)
    results = page.result_table
    assert len(results) > 0
    product_list = driver.find_elements(By.XPATH, '//a[contains(@href, "/product/")]')[15]
    action = ActionChains(driver)
    action.move_to_element(product_list).click(product_list).perform()
    title = driver.find_element(By.TAG_NAME, 'h1')
    assert name.lower() in title.text.lower()


@pytest.mark.parametrize('name', ['Акции', 'Бренды', 'Магазины'], ids=['actions', 'brends', 'shops'])
def test_main_menu_visible(driver, name):
    """Проверяем корректность отображения основного меню"""
    page = MainPage(driver)
    menu = []
    for i in range(len(page.main_menu)):
        menu.append(page.main_menu[i].text)
    assert name in menu


def test_catalog_visible(driver):
    """Проверяем наличие каталога"""
    page = MainPage(driver)
    assert page.catalog_button.is_displayed()


@pytest.mark.parametrize('name', ['Электроника', 'Обувь', 'Спорт и отдых'], ids=['Electronics', 'Shoes', 'Sport'])
def test_catalog_menu(driver, name):
    """Проверяем наличие категорий товаров в каталоге"""
    page = MainPage(driver)
    page.catalog_button.click()
    catalog = []
    for i in range(len(page.catalog_menu)):
        catalog.append(page.catalog_menu[i].text)
    assert name in catalog


def test_catalog_menu_clickable(driver):
    """Проверяем корректность работы каталога"""
    page = MainPage(driver)
    page.catalog_button.click()
    page.catalog_menu[1].click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Одежда"
    assert page.get_relative_link() == '/category/odezhda-obuv-i-aksessuary-7500/'


@pytest.mark.parametrize('name', ['Ozon для бизнеса', 'Мобильное приложение', 'Подарочные сертификаты'], \
                         ids=['Business', 'Mobile', 'Sertificates'])
def test_topbar(driver, name):
    """Проверяем корректность работы ссылок верхней плашки меню"""
    page = MainPage(driver)
    topbar_links = page.topbar
    topbar = []
    for i in range(len(topbar_links)):
        topbar.append(topbar_links[i].text)
    assert name in topbar
    for i in range(len(topbar_links)):
        action = ActionChains(driver)
        action.context_click(topbar_links[i]).perform()
        driver.switch_to.window(driver.window_handles[1])
        assert 'ozon' in page.get_url()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


def test_banner(driver):
    """Проверяем кликабельность рекламного баннера"""
    page = MainPage(driver)
    page.banner.click()
    assert '/highlight/' in page.get_relative_link()
