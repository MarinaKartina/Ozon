# pytest -v tests\test_shoes_page.py
import pytest
from pages.shoes_page import ShoesPage

def test_title(driver):
    page = ShoesPage(driver)
    assert page.title.is_displayed()