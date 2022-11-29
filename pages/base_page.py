import math
from selenium import webdriver
from .locators import BasePageLocators
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Родительский класс
class BasePage():
    # Создаем конструкцию взаимодействия передачи ссылки в браузер
    def __init__(self, browser: RemoteWebDriver, url):
        self.browser = browser
        self.url = url


    # Создаем метод открытия и перехода по ссылке page.open()
    def open(self):
        self.browser.get(self.url)


    # Если элемент найден, возвращаем True,
    # иначе - перехватываем ошибку 'NoSuchElementException'
    # и присваиваем False
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True


    # Кликаем по ссылке логин / регистрация
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()


    # Проверка того, что пользователь залогинен.
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"



