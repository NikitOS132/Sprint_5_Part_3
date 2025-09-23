import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credential

@pytest.mark.usefixtures("start_from_register_page")
class TestCheckNewRegister:
    def test_something(self, driver, new_user):

        driver.find_element(*Locators.field_name).send_keys(new_user["name"])

        driver.find_element(*Locators.field_email).send_keys(new_user["email"])

        driver.find_element(*Locators.field_password).send_keys(new_user["password"])

        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, 60).until(EC.url_to_be(login_site))

@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingCreationExistingAccount:
    def test_something(self, driver):
        
        driver.find_element(*Locators.inscription_login).click()

        driver.find_element(*Locators.field_name).send_keys(Credential.name)

        driver.find_element(*Locators.field_email).send_keys(Credential.email)

        driver.find_element(*Locators.field_password).send_keys(Credential.password)

        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, 60).until(EC.visibility_of_element_located(Locators.ERROR_TEXT_DUPLICATE))

@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckRegisterNoName:
    def test_something(self, driver):

        driver.find_element(*Locators.inscription_login).click()

        driver.find_element(*Locators.field_email).send_keys(Credential.email)

        driver.find_element(*Locators.field_password).send_keys(Credential.password)

        driver.find_element(*Locators.button_register).click()

        assert driver.current_url == register_site

@pytest.mark.usefixtures("start_from_register_page")
class TestCheckingErrorPassword:
    def test_something(self, driver):

        driver.find_element(*Locators.field_email).send_keys(Credential.email)

        driver.find_element(*Locators.field_password).send_keys(Credential.incorrect_password)

        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, 60).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))

@pytest.mark.usefixtures("start_from_login_page")
class TestCheckingRestoredPassword:
    def test_something(self, driver):

        driver.find_element(*Locators.FORGOT_LINK).click()

        driver.find_element(*Locators.field_email).send_keys(Credential.email)

        driver.find_element(*Locators.button_restore).click()

        WebDriverWait(driver, 60).until(EC.url_to_be(reset_site))

        assert driver.current_url == reset_site