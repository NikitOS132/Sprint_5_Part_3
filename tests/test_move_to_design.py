import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestCheckChapterBread:
    def test_check_chapter_bread(self, start_from_main_page):
        driver = start_from_main_page

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.TAB_SAUCES)).click()

        buns = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.TAB_BUNS))

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buns)
        buns.click()

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Булки"))

        active_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))
        assert "Булки" in active_text.text

class TestCheckChapterFillings:
    def test_check_chapter_fillings(self, start_from_main_page):
        driver = start_from_main_page

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TAB_FILLINGS)).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_TAB)).is_displayed()
        
        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))
        assert "Начинки" in active_tab.text

class TestCheckChapterSauce:
    def test_check_chapter_sauce(self, start_from_main_page):
        driver = start_from_main_page

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TAB_SAUCES)).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_TAB)).is_displayed()

        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))
        assert "Соусы" in active_tab.text