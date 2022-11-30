from pages.locators import MainPageLocators
from pages.main_page import MainPage
import pytest

def test_checking_url_and_theme_color(browser):
    """Checking current URL and theme's color. [1] test"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.check_current_url('http://test.exlab.team/')
    page.check_background_color('black')


@pytest.mark.skip(reason="Refresh method is not added")
def test_checking_logo_and_refresh_page(browser):
    """Checking logo is present and clicking refreshes the page. [2] test"""
    pass


def test_check_about_us_header(browser):
    """Checking About Us button and shift to About Us block. [3] test"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.check_item_is_present('About Us', MainPageLocators.ABOUT_US_BUTTON_HEADER)    
    page.click_on_button(*MainPageLocators.ABOUT_US_BUTTON_HEADER)
    page.check_anchor_element_after_shifting('About Us', MainPageLocators.ABOUT_US_ANCHOR)


def test_check_project_header(browser):
    """Checking Project button and shift to Project block. [4] test"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.check_item_is_present('Project', MainPageLocators.PROJECTS_BUTTON_HEADER)
    page.click_on_button(*MainPageLocators.PROJECTS_BUTTON_HEADER)
    page.check_anchor_element_after_shifting('Project', MainPageLocators.PROJECT_ANCHOR)


def test_check_mentors_header(browser):
    """Checking Mentors button and shift to Mentors block. [5] test"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.check_item_is_present('Mentors', MainPageLocators.MENTORS_BUTTON_HEADER)
    page.click_on_button(*MainPageLocators.MENTORS_BUTTON_HEADER)
    page.check_anchor_element_after_shifting('Mentors', MainPageLocators.MENTORS_ANCHOR)


def test_check_startup_for_header(browser):
    """Checking StartUp For button and shift to StartUp For block. [6] test"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.check_item_is_present('Mentors', MainPageLocators.STARTUP_FOR_BUTTON_HEADER)
    page.click_on_button(*MainPageLocators.STARTUP_FOR_BUTTON_HEADER)
    page.check_anchor_element_after_shifting('Mentors', MainPageLocators.STARTUP_FOR_ANCHOR)


def test_click_sun_icon(browser):
    """Checking Sun Icon and theme's color. Have to be white. [7] test"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.check_item_is_present('Sun Icon', MainPageLocators.SUN_ICON)
    page.click_on_button(*MainPageLocators.SUN_ICON)
    page.check_background_color('white')


def test_check_join_header(browser):
    """Checking Join button open registration TG-bot. [9] test"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.check_item_is_present('Join', MainPageLocators.JOIN_BUTTON_HEADER)
    page.click_on_button(*MainPageLocators.JOIN_BUTTON_HEADER)
    page.check_join_opened_correct_url('https://t.me/ExLab_registration_bot')