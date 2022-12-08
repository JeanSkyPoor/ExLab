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
    parser.addoption('--height_window', action='store', default='1080')

    parser.addoption('--language', action='store', default='en',
                     help="Choose language: 'ru' or 'en'")
    parser.addoption('--headless', action='store', default='None',
                     help="Open a browser invisible, without GUI is used by default")

@pytest.fixture(scope="function")
def browser(request):
    try:
        # Значения переменных user_language / browser_name / headless принимаются из консоли.
        user_language = request.config.getoption("language")
        browser_name = request.config.getoption("browser_name")
        headless = request.config.getoption('headless')
        width_window = request.config.getoption('width_window')
        height_window = request.config.getoption('height_window')

        if browser_name == "chrome":
            # Чтобы указать язык браузера, использую класс Options и метод add_experimental_option
            # Без браузерный режим для 'Chrome'
            options = Options()
            if headless == 'True':
                options.add_argument('headless')

            # // Отключение сообщений в консоли типа: USB: usb_device_handle...
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            # // Выбор языка страницы
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            browser = webdriver.Chrome(options=options)

            #browser.maximize_window()
            browser.set_window_size(width_window, height_window) #Настройка размера открывающегося окна
            browser.implicitly_wait(5) # Не явное ожидание элементов 5 сек.

        elif browser_name == "firefox":

            # Без браузерный режим для 'Firefox', через импорт библиотеки 'os'
            if headless == 'True':
                os.environ['MOZ_HEADLESS'] = '1'

            # Чтобы указать язык браузера, использую класс Options и метод add_experimental_option
            # Для Firefox  браузера
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", user_language)
            browser = webdriver.Firefox(firefox_profile=fp)
            browser.set_window_size(width_window, height_window) #Настройка размера открывающегося окна
            browser.implicitly_wait(5)  # Не явное ожидание элементов 5 сек.


        elif browser_name == "yandex":
            options = Options()
            if headless == 'True':
                options.add_argument('headless')

            service = Service("C:\chromedriver\chromedriver_104.exe")
            options.binary_location = "C:/Users/User/AppData/Local/Yandex/YandexBrowser/Application/browser.exe"

            # // Отключение сообщений в консоли типа: USB: usb_device_handle...
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            browser = webdriver.Chrome(options=options, service=service)
            browser.set_window_size(width_window, height_window) #Настройка размера открывающегося окна
            browser.implicitly_wait(5) # Не явное ожидание элементов 5 сек.



        else:           
            raise pytest.UsageError("--browser_name should be chrome or firefox or yandex")
        yield browser
        browser.quit()
    except Exception as e:
        pytest.exit(f"Failed to setup fixture: {e}")


# Supports console options (pytest):
# --browser_name= (firefox or chrome or yandex)
# --language=ru (default='en')
# --headless=true (default='None')
# --width_window=(default='1920')
# --height_window=(default='1080')
 
