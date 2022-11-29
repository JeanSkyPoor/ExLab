import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# получает значения из консоли
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox or yandex")
    parser.addoption('--width_window', action='store', default='1920')
    parser.addoption('--height_window', action='store', default='700')

    parser.addoption('--language', action='store', default='en',
                     help="Choose language: 'ru' or 'en'")
    parser.addoption('--headless', action='store', default='None',
                     help="Open a browser invisible, without GUI is used by default")

@pytest.fixture(scope="function")
def browser(request):
    # Значения переменных user_language / browser_name / headless принимаются из консоли.
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption('headless')
    width_window = request.config.getoption('width_window')
    height_window = request.config.getoption('height_window')

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # Чтобы указать язык браузера, использую класс Options и метод add_experimental_option
        # Без браузерный режим для 'Chrome'
        options = Options()
        if headless == 'true':
            options.add_argument('headless')

        # // Отключение сообщений в консоли типа: USB: usb_device_handle...
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # // Выбор языка страницы
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)


        browser.set_window_size(width_window, height_window)
        browser.implicitly_wait(10) # Не явное ожидание элементов 10 сек.

    elif browser_name == "firefox":

        print("\nstart firefox browser for test..")
        # Без браузерный режим для 'Firefox', через импорт библиотеки 'os'
        if headless == 'true':
            os.environ['MOZ_HEADLESS'] = '1'

        # Чтобы указать язык браузера, использую класс Options и метод add_experimental_option
        # Для Firefox  браузера
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.set_window_size(width_window, height_window)
        browser.implicitly_wait(10)  # Не явное ожидание элементов 10 сек.


    elif browser_name == "yandex":
        options = Options()
        if headless == 'true':
            options.add_argument('headless')

        service = Service("C:\chromedriver\chromedriver_104.exe")
        options.binary_location = "C:/Users/User/AppData/Local/Yandex/YandexBrowser/Application/browser.exe"

        # // Отключение сообщений в консоли типа: USB: usb_device_handle...
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options, service=service)
        browser.set_window_size(width_window, height_window)
        browser.implicitly_wait(10)


    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox or yandex")
    yield browser
    print("\nquit browser..")
    browser.quit()


# Supports console options (pytest):
# --browser_name= (firefox or chrome or yandex)
# --language=ru (default='en')
# --headless=true (default='None')
# --width_window=(default='1920')
# --height_window=(default='1080')

'''
 
pytest -v -s  --tb=line --reruns 1  --browser_name=chrome --width_window=1024 --height_window=768
--language=ru --headless=true   test_product_page.py
