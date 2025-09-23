import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestConstructorTabs:
    def test_check_chapter(self, start_from_main_page):
        driver = start_from_main_page

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable(Locators.TAB_SAUCES)).click()

        buns = WebDriverWait(driver, 60).until(EC.element_to_be_clickable(Locators.TAB_BUNS))

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buns)
        buns.click()

        WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Булки"))

        fillings = WebDriverWait(driver, 60).until(EC.element_to_be_clickable(Locators.TAB_FILLINGS))

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", fillings)
        fillings.click()

        WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Начинки"))

        sauces = WebDriverWait(driver, 60).until(EC.element_to_be_clickable(Locators.TAB_SAUCES))

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sauces)
        sauces.click()

        WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Соусы"))

        active_text = WebDriverWait(driver, 60).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))
        assert "Булки", "Начинки" and "Соусы" in active_text.text