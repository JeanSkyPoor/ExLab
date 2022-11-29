from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    BASKET_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    INPUT_LOGIN = (By.XPATH, '//input[@name="login-username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="login-password"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')
    EMAIL = (By.XPATH, '//input[@name="registration-email"]')
    PASSWORD_1 =  (By.XPATH, '//input[@name="registration-password1"]')
    PASSWORD_2 = (By.XPATH, '//input[@name="registration-password2"]')
    CONFIRMATION_BUTTON_REGISTRATION = (By.XPATH, '//button[@name="registration_submit"]')



