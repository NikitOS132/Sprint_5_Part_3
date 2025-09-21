import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credential

class TestEntranceAndExit:
    def test_check_entrance_and_exit(self, start_from_site_not_login):
        driver = start_from_site_not_login

        driver.find_element(*Locators.BIG_LOGIN_BTN).click()

        driver.find_element(*Locators.inscription_login).click()

        driver.find_element(*Locators.inscription_button_entrance).click()

        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_entrance).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TAB_BUNS))

        driver.find_element(*Locators.button_personal_area).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_profile))

        driver.find_element(*Locators.PROFILE_EXIT_BTN).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(login_site))

        assert driver.current_url == login_site