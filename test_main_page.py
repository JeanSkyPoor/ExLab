from pages.locators import MainPageLocators
from pages.main_page import MainPage
import pytest
import allure

@allure.feature("Unfunctional")
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


@allure.feature("Functional")
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


@allure.feature("Functional")
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
    

@allure.feature("Functional")
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


@allure.feature("Unfunctional")
def test_logo_your_opportunity_block(browser):
    """Test 'Logo_Gif' in block YOUR_OPPORTYNITY is present and displayed. [11] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Checking if 'Logo_Gif' in block 'Your_Opportunity' is present and displayed"):
        page.checking_logo_gif_in_your_opportunity_block_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_text_your_opportunity_block(browser):
    """Test 'Text_Under_Main_Title' block YOUR OPPORTUNITY is present and displayed. [12] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Checking if 'Text_Under_Main_Title' in block Your_Opportunity is present and displayed"):
        page.checking_main_title_in_your_opportunity_block_is_present_and_displayed()

    with allure.step("Step 3. Checking if 'Text_Under_Main_Title' in block ' in Your_Opportunity under Main title is present and displayed"):
        page.checking_text_under_main_title_in_your_opportunity_block_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_about_us_block(browser):
    """Test About_Us title and description is present and displayed. [13] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to About_Us block"):
        page.scroll_to_about_us()

    with allure.step("Step 3. Checking if 'About_Us' title in block About_Us is present and displayed"):
        page.checking_main_title_about_us_is_present_and_displayed()

    with allure.step("Step 4. Checking if description in block About_Us is present and displayed"):
        page.checking_description_about_us_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_why_exlab_block(browser):
    """Test Why_Exlab title and description is present and displayed. [14] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to Why_Exlab block"):
        page.scroll_to_why_exlab()
        
    with allure.step("Step 3. Checking if Why_Exlab title in block Why_Exlab is present and displayed"):
        page.checking_why_exlab_title_why_exlab_is_present_and_displayed()

    with allure.step("Step 4. Checking if description in block Why_Exlab is present and displayed"):
        page.checking_description_why_exlab_is_present_and_displayed()


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


@allure.feature("Unfunctional")
def test_title_projects_block(browser):
    """Test 'Projects' title in Projects block is present and displayed. [16] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'Projects'"):
        page.scroll_to_project()

    with allure.step("Step 3. Checking if 'Project_Title' in 'Projects' block is present and displayed"):
        page.checking_projects_title_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_logos_and_descriptions_projects_block(browser):
    """Test logos and descriptions of projects in Projects block are present and displayed. [17] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'Projects'"):
        page.scroll_to_project()

    with allure.step("Step 3. Checking logo and description of projects"):
        page.checking_logos_and_descriptions_projects_block()


@allure.feature("Unfunctional")
def test_title_mentors_block(browser):
    """Test Mentors_Title in Mentors block are present and displayed. [18] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'Mentors'"):
        page.scroll_to_mentors()

    with allure.step("Step 3. Checking if Mentors_Title in Mentors block is presend and displayed"):
        page.checking_title_mentors_is_present_and_displayed()


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


@allure.feature("Unfunctional")
def test_title_startup_for_block(browser):
    """Test StartUp_For_Title in StartUp_For block are present and displayed. [24] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'StartUp_For'"):
        page.scroll_to_startup_for()

    with allure.step("Step 3. Checking if StartUp_For_Title in StartUp_For block is present and displayed"):
        page.checking_title_startup_for_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_descriptions_startup_for_block(browser):
    """Test Descriptions in StartUp_For block are present and displayed. [28] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'StartUp_For'"):
        page.scroll_to_startup_for()

    with allure.step("Step 3. Checking descriptions in block 'StartUp_For' is present and displayed"):
        page.checking_descriptions_startup_for_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_title_help_project_block(browser):
    """Test Help_Project_Title in Help_Project block are present and displayed. [30] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'Help_Project'"):
        page.scroll_to_help_project()

    with allure.step("Step 3. Checking if 'Help_Project_Title' in Help_Project block is present and displayed"):
        page.checking_title_help_project_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_description_help_project_block(browser):
    """Test Description in Help_Project block are present and displayed. [31] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'Help_Project'"):
        page.scroll_to_help_project()

    with allure.step("Step 3. Checking descriptions in block 'Help_Project' is present and displayed"):
        page.checking_description_help_project_is_present_and_displayed()
    

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


@pytest.mark.skip(reason="Patreon page is not created")
@allure.feature("Functional")
def test_patreon_button_help_project(browser):
    """Test Patreon button in Help Project block. [33] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to Help Project block"):
        page.scroll_to_help_project()

    with allure.step("Step 3. Checking if 'Patreon' button in Help Project block is present and displayed"):
        page.checking_patreon_help_project_button_is_present_and_displayed()

    #To Do: написать реализацию кнопки Patreon, когда добавят функционал


@allure.feature("Unfunctional")
def test_title_stay_connected_block(browser):
    """Test Title_Footer in FOOTER block are present and displayed. [34] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'FOOTER'"):
        page.scroll_to_footer()

    with allure.step("Step 3. Checking 'Title_Footer' in FOOTER is present and displayed"):
        page.checking_title_stay_connected_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_description_stay_connected_block(browser):
    """Test description in FOOTER block are present and displayed. [35] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'FOOTER'"):
        page.scroll_to_footer()

    with allure.step("Step 3. Checking desciption in FOOTER is present and displayed"):
        page.checking_description_stay_connected_is_present_and_displayed()   


@allure.feature("Unfunctional")
def test_logo_footer_block(browser):
    """Test Logo in FOOTER block are present and displayed. [36] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'FOOTER'"):
        page.scroll_to_footer()

    with allure.step("Step 3. Checking Logo in FOOTER is present and displayed"):
        page.checking_logo_footer_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_text_under_logo_footer_block(browser):
    """Test Text_Under_Logo in FOOTER block are present and displayed. [37] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'FOOTER'"):
        page.scroll_to_footer()
    
    with allure.step("Step 3. Checking Text_Under_Logo in FOOTER is present and displayed"):
        page.checking_text_under_logo_footer_is_present_and_displayed()


@allure.feature('Functional')
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


@allure.feature('Functional')
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


@allure.feature('Functional')
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


@allure.feature('Functional')
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


@allure.feature("Unfunctional")
def test_mail_address_footer_block(browser):
    """Test Mail_Address in FOOTER block are present and displayed. [42] test from check-list"""
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()

    with allure.step("Step 1. Checking landing URL"):
        page.checking_landing_url()

    with allure.step("Step 2. Scrolling to block 'FOOTER'"):
        page.scroll_to_footer()

    with allure.step("Step 3. Checking Mail_Address in FOOTER is present and displayed"):
        page.checking_mail_address_footer_is_present_and_displayed()