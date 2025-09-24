import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestCheckChapterSauce:
    def test_check_chapter_sauce(self, start_from_main_page):
        driver = start_from_main_page

        WebDriverWait(driver, 60).until(EC.visibility_of_element_located(Locators.TAB_SAUCES)).click()

        WebDriverWait(driver, 60).until(EC.presence_of_element_located(Locators.ACTIVE_TAB)).is_displayed()

        active_text = WebDriverWait(driver, 60).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))
        assert "Соусы" in active_text.text