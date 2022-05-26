# pytest -v tests\test_electronics_page.py

import pytest
from pages.electronics import ElectronicsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.parametrize('point', ['БЫТОВАЯ ТЕХНИКА', 'СМАРТ-ЧАСЫ', 'ТЕЛЕВИЗОРЫ', 'НОУТБУКИ', \
                         'КОМПЬЮТЕРЫ', 'АУДИОТЕХНИКА', 'ИГРЫ И КОНСОЛИ'], \
                         ids=['Home appliance', 'Smartphones', 'TV', 'Notebooks', 'Computers', 'Audio', 'Playstations'])
def test_main_menu_clickable(driver, point):
    """Проверяем кликабельность элементов основного меню и корректность ссылок на категории"""
    page = ElectronicsPage(driver)
    electr_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.title))
    assert 'Электроника' == electr_title.text
    menu = page.main_menu
    assert len(menu) == 7
    menu_points = []
    for i in range(len(menu)):
        menu_points.append(menu[i].text)
    for i in range(len(menu_points)):
        if point in menu_points[i]:
            assert menu[i].is_displayed()
            menu[i].click()
            title = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.title))
            assert point in title.text.upper()


def test_interest_vidget_clickable(driver):
    """Проверяем кликабельность виджета из раздела 'Вас может заинтересовать'"""
    page = ElectronicsPage(driver)
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", page.quadrocopter)
    page.quadrocopter.click()
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.title))
    assert "Квадрокоптеры" in title.text


def test_vidgets_clickable(driver):
    """Проверяем кликабельность всех виджетов с категориями товаров"""
    page = ElectronicsPage(driver)
    vidgets = page.vidgets
    assert len(vidgets) > 0
    vidget_link = []
    for i in range(len(vidgets)):
        vidget_link.append(vidgets[i].get_attribute('href'))
    for i in range(len(vidgets)):
        driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", vidgets[i])
        action = ActionChains(driver)
        action.context_click(vidgets[i]).perform()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.title))
        assert vidget_link[i] == driver.current_url
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
