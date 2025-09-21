from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Locators:
    
    BIG_LOGIN_BTN = (By.XPATH, "//button[.='Войти в аккаунт']")

    logo = (By.XPATH, '//header/nav/div')

    PROFILE_EXIT_BTN = (By.XPATH, "//button[.='Выход']")

    inscription_profile = (By.XPATH, './/a[@href="/account/profile"]')

    TAB_BUNS = (By.XPATH, ".//span[contains(text(),'Булки')]")

    # Проблемный локатор
    button_personal_area = (By.XPATH, "//a[contains(@href,'account')]")

    TAB_SAUCES = (By.XPATH, ".//span[contains(text(),'Соусы')]")

    # Проблемный локатор
    inscription_login = (By.XPATH, "//a[contains(@href,'register')]")

    TAB_FILLINGS = (By.XPATH, ".//span[contains(text(),'Начинки')]")

    LOGO = (By.XPATH, "//*[contains(@class,'AppHeader_header__linkText') and contains(@class,'ml-2')]")

    ERROR_TEXT_DUPLICATE = (By.XPATH, ".//p[contains(text(),'Такой пользователь уже существует')]")

    ERROR_TEXT = (By.XPATH, "//*[contains(@class,'input__error') and contains(.,'Некорректный пароль')]")

    FORGOT_LINK = (By.XPATH, "//a[contains(@href,'forgot-password')]")
    
    # Проблемный локатор
    inscription_button_entrance = (By.XPATH, './/a[@href="/login"]')

    button_entrance = (By.XPATH, ".//button[contains(text(),'Войти')]")

    button_arrange_order = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]")

    button_register = (By.XPATH, ".//button[.='Зарегистрироваться']")

    button_constaction = (By.XPATH, ".//a[@href='/']")

    field_name = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")

    field_email = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")

    field_password = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input")

    button_restore = (By.XPATH, ".//button[contains(text(),'Восстановить')]")

    ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]")