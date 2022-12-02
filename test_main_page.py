from pages.locators import MainPageLocators
from pages.main_page import MainPage
import pytest
import time
import allure


def test_landing_url_and_black_theme(browser):
    """Test landing URL and black theme on default. [1] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Checking dark theme on"):
        page.checking_dark_mode_on()


#@pytest.mark.skip(reason="Refresh functioan is not created")
def test_display_logo_ExLab(browser):
    """Test logo ExLab. [2] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()


def test_about_us_header(browser):
    """Test 'About Us' button in HEADER. [3] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Сhecking if 'About Us' HEADER element present and displayed"):
        page.checking_about_us_header_is_present_and_displayed()

    with allure.step("Step 3. Click on 'About us' in HEADER"):
        page.click_on_about_us_header()

    with allure.step("Step 4. Checking 'About Us' anchor element after shifting"):
        page.checking_about_us_anchor_after_shifting()


def test_projects_header(browser):
    """Test 'Projects' button in HEADER. [4] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Сhecking if 'Projects' HEADER element present and displayed"):
        page.checking_projects_header_is_present_and_displayed()

    with allure.step("Step 3. Click on 'Projects' in HEADER"):
        page.click_on_projects_header() 

    with allure.step("Step 4. Checking 'Projects' anchor element after shifting"):
        page.checking_projects_anchor_after_shifting()


def test_mentors_header(browser):
    """Test 'Mentors' button in HEADER. [5] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Сhecking if 'Mentors' HEADER element present and displayed"):
        page.checking_mentors_header_is_present_and_displayed()

    with allure.step("Step 3. Click on 'Mentors' in HEADER"):
        page.click_on_mentors_header() 

    with allure.step("Step 4. Checking 'Mentors' anchor element after shifting"):
        page.checking_mentors_anchor_after_shifting()


@pytest.mark.skip(reason='Button behaves strangely')
def test_startup_for_header(browser):
    """Test 'StartUp for' button in HEADER. [6] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Сhecking if 'StartUp for' HEADER element present and displayed"):
        page.checking_startup_for_header_is_present_and_displayed()

    with allure.step("Step 3. Click on 'StartUp for' in HEADER"):
        page.click_on_startup_for_header() 

    with allure.step("Step 4. Checking 'StartUp for' anchor element after shifting"):
        page.checking_startup_for_anchor_after_shifting()


def test_sun_icon_header(browser):
    """Test 'Sun icon' button in HEADER. [7] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Сhecking if 'Sun icon' HEADER element present and displayed"):
        page.checking_sun_icon_header_is_present_and_displayed()

    with allure.step("Step 3. Click on 'Sun icon' in HEADER"):
        page.click_on_sun_icon_header()

    with allure.step("Step 4. Checking light theme on"):
        page.checking_light_mode_on()
    

def test_join_header(browser):
    """Test 'Join' button in HEADER. [9] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Сhecking if 'Join' HEADER element present and displayed"):
        page.checking_join_header_is_present_and_displayed()

    with allure.step("Step 3. Click on 'Join' in HEADER"):
        page.click_on_join_header()

    with allure.step("Step 4. Checking URL opened page"):
        page.checking_url_after_click_on_join_header()










































# def test_checking_url_and_theme_color(browser):
#     """Checking current URL and theme's color. [1] test"""
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.match_current_url('http://test.exlab.team/')
#     page.check_background_color('black')
#     page.matching_item_attribute('http://test.exlab.team/gif/logo.gif', 'src', MainPageLocators.LOGO_GIF)
#     page.check_element_is_present('Sun Icon', MainPageLocators.SUN_ICON)


# @pytest.mark.skip(reason="Refresh method is not added")
# def test_checking_logo_and_refresh_page(browser):
#     """Checking logo is present and clicking refreshes the page. [2] test"""
#     pass


# def test_check_about_us_header(browser):
#     """Checking About Us button and shift to About Us block. [3] test"""
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.check_element_is_present('About Us', MainPageLocators.ABOUT_US_BUTTON_HEADER)    
#     page.click_on_button(*MainPageLocators.ABOUT_US_BUTTON_HEADER)
#     page.check_anchor_element_after_shifting('About Us', MainPageLocators.ABOUT_US_ANCHOR)


# def test_check_project_header(browser):
#     """Checking Project button and shift to Project block. [4] test"""
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.check_element_is_present('Project', MainPageLocators.PROJECTS_BUTTON_HEADER)
#     page.click_on_button(*MainPageLocators.PROJECTS_BUTTON_HEADER)
#     page.check_anchor_element_after_shifting('Project', MainPageLocators.PROJECT_ANCHOR)


# def test_check_mentors_header(browser):
#     """Checking Mentors button and shift to Mentors block. [5] test"""
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.check_element_is_present('Mentors', MainPageLocators.MENTORS_BUTTON_HEADER)
#     page.click_on_button(*MainPageLocators.MENTORS_BUTTON_HEADER)
#     page.check_anchor_element_after_shifting('Mentors', MainPageLocators.MENTORS_ANCHOR)


# def test_check_startup_for_header(browser):
#     """Checking StartUp For button and shift to StartUp For block. [6] test"""
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.check_element_is_present('StartUp For', MainPageLocators.STARTUP_FOR_BUTTON_HEADER)
#     page.click_on_button(*MainPageLocators.STARTUP_FOR_BUTTON_HEADER)
#     page.check_anchor_element_after_shifting('StartUp For', MainPageLocators.STARTUP_FOR_ANCHOR)


# def test_click_sun_icon(browser):
#     """Checking Sun Icon and theme's color. Have to be white. [7] test"""
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.check_element_is_present('Sun Icon', MainPageLocators.SUN_ICON)
#     page.click_on_button(*MainPageLocators.SUN_ICON)
#     page.check_background_color('white')


# def test_check_join_header(browser):
#     """Checking Join button open registration TG-bot. [9] test"""
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.check_element_is_present('Join', MainPageLocators.JOIN_BUTTON_HEADER)
#     page.click_on_button(*MainPageLocators.JOIN_BUTTON_HEADER)
#     page.check_join_opened_correct_url('https://t.me/ExLab_registration_bot')


# def test_check_is_logo_gif_present(browser):
#     """Checking if logo_gif is present on page. [11] test"""
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.check_element_is_present('Logo_gif', MainPageLocators.LOGO_GIF)
#     page.matching_item_attribute('http://test.exlab.team/gif/logo.gif', 'src', MainPageLocators.LOGO_GIF)


# def test_is_your_opportunity_block_present(browser):
#     """Checking if your opportunity is present on page and check text under your opportunity. [12] test"""
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.check_element_is_present('Your opportunity', MainPageLocators.YOUR_OPPORTUNITY)
#     page.matching_text_from_element('Твоя возможность:', MainPageLocators.YOUR_OPPORTUNITY)
#     page.check_element_is_present('Text under your opportunity', MainPageLocators.TEXT_UNDER_YOUR_OPPORTUNITY)
#     page.checking_if_matching_text_in_element(['ПОЛУЧИТЬ ТОТ САМЫЙ ОПЫТ', 'ПОРАБОТАТЬ В КОМАНДЕ', 'СОЗДАТЬ ПРОЕКТ С НУЛЯ', 'ПОПОЛНИТЬ ПОРТФОЛИО'],\
#          MainPageLocators.TEXT_UNDER_YOUR_OPPORTUNITY)


# def test_is_about_us_block_present(browser):
#     """Checking if About Us block is present on page and check text under About Us. [13] test"""
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.scroll_down_to_element(MainPageLocators.ABOUT_US_ANCHOR)
#     page.check_element_is_present('About Us', MainPageLocators.ABOUT_US_MAIN)
#     page.matching_text_from_element('О нас', MainPageLocators.ABOUT_US_MAIN)
#     page.check_element_is_present('About Us text', MainPageLocators.ABOUT_US_BLOCK_TEXT)
#     page.checking_if_matching_text_in_element(['каждый', 'выделится', 'подготовленного'], MainPageLocators.ABOUT_US_BLOCK_TEXT)


# def test_is_why_exlab_present(browser):
#     """Checking if Why ExLab block is present on page and check text under Whe ExLab. [14] test"""
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.scroll_down_to_element(MainPageLocators.WHY_EXLAB_ANCHOR) # Have to scroll to anchor and after second time to top text. without it's not working 
#     page.scroll_down_to_element(MainPageLocators.WHY_EXLAB_MAIN)
#     page.check_element_is_present('Why ExLab', MainPageLocators.WHY_EXLAB_MAIN)
#     page.matching_text_from_element('Почему ExLab?', MainPageLocators.WHY_EXLAB_MAIN)
#     page.check_element_is_present('Why ExLab block text', MainPageLocators.WHY_EXLAB_BLOCK_TEXT)
#     page.checking_if_matching_text_in_element(['Участие', 'Поддержка', 'рекрутеры', 'оригинальные'], MainPageLocators.WHY_EXLAB_BLOCK_TEXT)


# def test_is_why_exlab_join_present(browser):
#     """Checking if Join button on why exlab block is present and click it. [15] test"""
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.scroll_down_to_element(MainPageLocators.WHY_EXLAB_ANCHOR)
#     page.check_element_is_present('Присоединиться', MainPageLocators.WHY_EXLAB_JOIN)
#     page.matching_text_from_element('Присоединиться', MainPageLocators.WHY_EXLAB_JOIN)
#     page.click_on_button(*MainPageLocators.WHY_EXLAB_JOIN)
#     page.check_join_opened_correct_url('https://t.me/ExLab_registration_bot')



