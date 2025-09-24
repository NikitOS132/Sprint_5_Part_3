import pytest
import uuid
from selenium import webdriver
from curl import *
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from generation_ep import EmailPasswordGenerator
from data import Credential
import time, os
from utils import _rand_str


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    if os.getenv("DEBUG_PAUSE") == "1":
        WebDriverWait(driver, 10)
    d.quit()

@pytest.fixture
def start_from_login_page(driver):
    driver.get(login_site)
    yield

@pytest.fixture
def start_from_forgot_page(driver):
    forgot_page = forgot_site
    driver.get(forgot_page)

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(Locators.button_restore))

    driver.find_element(*Locators.field_email).send_keys(Credential.email)

    driver.find_element(*Locators.inscription_button_entrance).click()

    return driver

@pytest.fixture
def start_from_main_page(driver):
    main_page = main_site
    driver.get(main_page)

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(Locators.button_entrance))

    driver.find_element(*Locators.button_entrance).click()

    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver

@pytest.fixture
def start_from_register_page(driver):
    driver.get(register_site)
    yield

@pytest.fixture
def start_from_main_not_login(driver):
    login_page = login_site
    driver.get(login_page)

    return driver

@pytest.fixture
def start_from_site_not_login(driver):
    login_page = main_site
    driver.get(login_page)

    return driver

@pytest.fixture
def new_user():
    name = f"user_{_rand_str()}_{uuid.uuid4().hex[:4]}"
    email = f"qa_{_rand_str()}_{uuid.uuid4().hex[:6]}@example.test"
    password = f"P@ss_{_rand_str()}_{uuid.uuid4().hex[:6]}"
    return {"name": name, "email": email, "password": password}