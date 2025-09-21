import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *

class TestTransitionByConstructor:
    def test_check_transition_by_constructor(self, start_from_main_page):
        driver = start_from_main_page

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        driver.find_element(*Locators.button_personal_area).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_constaction))

        driver.find_element(*Locators.button_constaction).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

class TestTransitionByLogo:
    def test_transition_by_logo(self, start_from_main_page):
        driver = start_from_main_page

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_personal_area))

        driver.find_element(*Locators.button_personal_area).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.inscription_profile))

        driver.find_element(*Locators.logo).click()
        
        WebDriverWait(driver,10).until(EC.url_to_be(main_site))

        assert driver.current_url == (main_site)

class TestCheckPageProfile:
    def test_transition_befor_profile(self, start_from_main_page):
        driver = start_from_main_page

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TAB_BUNS))

        driver.find_element(*Locators.button_personal_area).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(profile_site))

        assert driver.current_url == (profile_site)