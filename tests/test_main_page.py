# pytest -v tests\test_main_page.py

import pytest
from pages.main_page import MainPage
from selenium.webdriver.common.by import By


@pytest.mark.skip
def test_search_form_visible(driver):
    page = MainPage(driver)
    assert page.search_form.is_displayed()

@pytest.mark.skip
@pytest.mark.parametrize('name', ['Акции', 'Бренды', 'Магазины'], ids = ['actions','brends','shops'])
def test_main_menu_visible(driver, name):
    page = MainPage(driver)
    menu = []
    for i in range(len(page.main_menu)):
        menu.append(page.main_menu[i].text)
    assert name in menu

@pytest.mark.skip
def test_catalog_visible(driver):
        page = MainPage(driver)
        assert page.catalog_button.is_displayed()

@pytest.mark.skip
@pytest.mark.parametrize('name', ['Электроника','Обувь','Спорт и отдых'], ids=['Electronics', 'Shoes', 'Sport'])
def test_catalog_menu(driver, name):
    page = MainPage(driver)
    page.catalog_button.click()
    catalog = []
    for i in range(len(page.catalog_menu)):
        catalog.append(page.catalog_menu[i].text)
    assert name in catalog

#@pytest.mark.skip
def test_catalog_menu_clickable(driver):
    page = MainPage(driver)
    page.catalog_button.click()
    page.catalog_menu[1].click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Одежда"
    assert page.get_relative_link() == '/category/odezhda-obuv-i-aksessuary-7500/'

@pytest.mark.skip
def test_advbanner_is_clickable(driver):
    page = MainPage(driver)
    assert page.advbanner.is_displayed()
    slide = page.slide_button
    slide.click()
    slide.click()
    page.advbanner.click()

@pytest.mark.skip
@pytest.mark.parametrize('name', ['Ozon для бизнеса', 'Мобильное приложение', 'Подарочные сертификаты'], \
                         ids=['Business', 'Mobile', 'Sertificates'])
def test_topbar(driver, name):
    page = MainPage(driver)
    topbar =[]
    for i in range(len(page.topbar)):
        topbar.append(page.topbar[i].text)
    assert name in topbar
