from pages.locators import MainPageLocators
from pages.main_page import MainPage
import pytest
import time
import allure
from selenium.webdriver.common.by import By


def test_landing_url_and_black_theme(browser):
    """Test landing URL and black theme on default. [1] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Checking dark theme on"):
        page.checking_dark_mode_on()


@allure.feature("Functional")
@pytest.mark.skip(reason="Refresh functioan is not created")
def test_display_logo_ExLab(browser):
    """Test logo ExLab. [2] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()


@allure.feature("Functional")
@allure.feature("HEADER buttons")
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


@allure.feature("Functional")
@allure.feature("HEADER buttons")
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


@allure.feature("Functional")
@allure.feature("HEADER buttons")
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


@allure.feature("Functional")
@allure.feature("HEADER buttons")
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


@allure.feature("Functional")
@allure.feature("HEADER buttons")
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
    

@allure.feature("Functional")
@allure.feature("HEADER buttons")
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


def test_logo_in_block_your_opportunity(browser):
    """Test Logo in block YOUR OPPORTYNITY is present and displayed. [11] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Checking if logo in block 'Your opportunity' is present and displayed"):
        page.checking_logo_in_your_opportunity_block_is_present_and_displayed()


def test_text_your_opportunity_block(browser):
    """Test text in block YOUR OPPORTUNITY is present and displayed. [12] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Checking if Main title in block 'Your opportunity' is present and displayed"):
        page.checking_main_title_in_your_opportunity_block_is_present_and_displayed()

    with allure.step("Step 3. Checking if text in block ''Your opportunity' under Main title is present and displayed"):
        page.checking_text_under_main_title_in_your_opportunity_block_is_present_and_displayed()


@allure.feature("Functional")
@allure.feature('FOOTER buttons')
def test_linkedin_footer(browser):
    """Test 'Linkedin' button in FOOTER. [38] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to FOOTER block"):
        page.scroll_to_footer()

    with allure.step("Step 3. Checking if 'Linkedin' button in FOOTER is present and displayed"):
        page.checking_linkedin_footer_is_present_and_displayed()

    with allure.step("Step 4. Click on 'Linkedin' in FOOTER"):
        page.click_on_linkedin_footer()

    with allure.step("Step 5. Checking URL opened page"):
        page.checking_url_after_click_on_linkedin_footer()


@allure.feature("Functional")
@allure.feature('FOOTER buttons')
def test_instagram_footer(browser):
    """Test 'Instagram' button in FOOTER. [39] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to FOOTER block"):
        page.scroll_to_footer()

    with allure.step("Step 3. Checking if 'Instagram' button in FOOTER is present and displayed"):
        page.checking_instagram_footer_is_present_and_displayed()

    with allure.step("Step 4. Click on 'Instagram' in FOOTER"):
        page.click_on_instagram_footer()

    with allure.step("Step 5. Checking URL opened page"):
        page.checking_url_after_click_on_instagram_footer()    


@allure.feature("Functional")
@allure.feature('FOOTER buttons')
def test_telegram_footer(browser):
    """Test 'Telegram' button in FOOTER. [40] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to FOOTER block"):
        page.scroll_to_footer()

    with allure.step("Step 3. Checking if 'Telegram' button in FOOTER is present and displayed"):
        page.checking_telegram_footer_is_present_and_displayed()

    with allure.step("Step 4. Click on 'Telegram' in FOOTER"):
        page.click_on_telegram_footer()

    with allure.step("Step 5. Checking URL opened page"):
        page.checking_url_after_click_on_telegram_footer()    


@allure.feature("Functional")
@allure.feature('FOOTER buttons')
def test_youtube_footer(browser):
    """Test 'Youtube' button in FOOTER. [41] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to FOOTER block"):
        page.scroll_to_footer()

    with allure.step("Step 3. Checking if 'Youtube' button in FOOTER is present and displayed"):
        page.checking_youtube_footer_is_present_and_displayed()

    with allure.step("Step 4. Click on 'Youtube' in FOOTER"):
        page.click_on_youtube_footer()

    with allure.step("Step 5. Checking URL opened page"):
        page.checking_url_after_click_on_youtube_footer()    


@allure.feature("Functional")
def test_join_why_exlab_block(browser):
    """Test 'Join' button in Why Exlab block. [15] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'Why Exlab'"):
        page.scroll_to_why_exlab()

    with allure.step("Step 3. Checking if 'Join' button in 'Why Exlab' block is present and displayed"):
        page.checking_join_why_exlab_is_present_and_displayed()

    with allure.step("Step 4. Click on 'Join' in Why Exlab block"):
        page.click_on_join_why_exlab()

    with allure.step("Step 5. Checking URL opened page"):
        page.checking_url_after_click_on_join_why_exlab()


@allure.feature("Functional")
def test_mentors_spoilers(browser):
    """Test spoilers of mentors in mentors block. [20] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'Mentors'"):
        page.scroll_to_mentors()

    with allure.step("Step 3. Checking all mentor's spoilers"):
        page.check_all_mentors_spoilers()








# def test_test(browser):
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     page.scroll_to_why_exlab()
#     time.sleep(5)








# def test_footer(browser):
#     page = MainPage(browser, MainPageLocators.LINK)
#     page.open()
#     #elements = page.browser.find_elements(By.CSS_SELECTOR, 'div.sc-fEOsli.iema-Dv')

#     page.scroll_to_footer()
#     page.checking_help_project_anchor_after_shifting()
#     time.sleep(5)

    # for i in elements:
    #     page.browser.execute_script("arguments[0].scrollIntoView();", i)
    #     time.sleep(1)
    # time.sleep(4)





# def test_scroll(browser):
#     page = MainPage(browser, MainPageLocators.TEST_LINK)
#     page.open()
#     page.scroll_to_footer()
#     # page.scroll_down_certain_distance(3000)
#     time.sleep(5)






































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



