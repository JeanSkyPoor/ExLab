from pages.locators import MainPageLocators
from pages.main_page import MainPage
import pytest
import allure


def test_landing_url_and_black_theme(browser):
    """Test landing URL and black theme on default. [1] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Checking dark theme on"):
        page.checking_dark_mode_on()


@pytest.mark.skip(reason="Refresh functioan is not created")
def test_display_logo_ExLab(browser):
    """Test logo ExLab. [2] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()


@allure.feature("HEADER buttons")
def test_about_us_header(browser):
    """Test 'About_Us' button in HEADER. [3] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Сhecking if 'About_Us' HEADER element present, displayed and clickable"):
        page.checking_about_us_header_is_present_and_displayed()

    with allure.step("Step 3. Click on 'About_Us' in HEADER"):
        page.click_on_about_us_header()

    with allure.step("Step 4. Checking 'About_Us' anchor element after shifting"):
        page.checking_about_us_anchor_after_shifting()


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


@allure.feature("HEADER buttons")
@pytest.mark.skip(reason='Button behaves strangely')
def test_startup_for_header(browser):
    """Test 'StartUp_For' button in HEADER. [6] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Сhecking if 'StartUp_For' HEADER element present and displayed"):
        page.checking_startup_for_header_is_present_and_displayed()

    with allure.step("Step 3. Click on 'StartUp_For' in HEADER"):
        page.click_on_startup_for_header() 

    with allure.step("Step 4. Checking 'StartUp_For' anchor element after shifting"):
        page.checking_startup_for_anchor_after_shifting()


@allure.feature("HEADER buttons")
def test_sun_icon_header(browser):
    """Test 'Sun_Icon' button in HEADER. [7] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Сhecking if 'Sun_Icon' HEADER element present and displayed"):
        page.checking_sun_icon_header_is_present_and_displayed()

    with allure.step("Step 3. Click on 'Sun_Icon' in HEADER"):
        page.click_on_sun_icon_header()

    with allure.step("Step 4. Checking light theme on"):
        page.checking_light_mode_on()
    

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
    """Test 'Logo_Gif' in block YOUR OPPORTYNITY is present and displayed. [11] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Checking if 'Logo_Gif' in block 'Your opportunity' is present and displayed"):
        page.checking_logo_gif_in_your_opportunity_block_is_present_and_displayed()


def test_text_your_opportunity_block(browser):
    """Test 'Text_Under_Main_Title' block YOUR OPPORTUNITY is present and displayed. [12] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Checking if 'Text_Under_Main_Title' in block Your opportunity is present and displayed"):
        page.checking_main_title_in_your_opportunity_block_is_present_and_displayed()

    with allure.step("Step 3. Checking if 'Text_Under_Main_Title' in block ' in Your opportunity under Main title is present and displayed"):
        page.checking_text_under_main_title_in_your_opportunity_block_is_present_and_displayed()


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


@allure.feature("Functional")
def test_boosty_button_help_project(browser):
    """Test Boosty button in Help Project block. [32] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to Help Project block"):
        page.scroll_to_help_project()

    with allure.step("Step 3. Checking if 'Boosty' button in Help Project block is present and displayed"):
        page.checking_boosty_help_project_button_is_present_and_displayed()

    with allure.step("Step 4. Click on Boosty button in Help Project block"):
        page.click_on_boosty_help_project()
    
    with allure.step("Step 5. Checking URL opened page"):
        page.checking_url_after_click_on_boosty_help_project()
        