import pytest
import allure
from pages.landing_page import LandingPage


@allure.feature("non-functional")
def test_black_theme_on_by_default(browser):
    """Test landing URL and black theme on default. [1] test from check-list"""

    LandingPage(browser).\
        checking_dark_mode_on()


@allure.feature("functional")
def test_expected_result_logo_exlab_header(browser):
    """Test logo ExLab in HEADER. [2] test from check-list. Without refresh method in test"""

    LandingPage(browser).\
        checking_logo_header_is_present_and_displayed()
    #TO DO: доделать, когда добавят функцию рефреша страницы


@allure.feature("functional")
def test_expected_result_about_us_header(browser):
    """Test 'About_Us' button in HEADER. [3] test from check-list"""

    LandingPage(browser).\
        click_on_about_us_header()


@allure.feature("functional")
def test_expected_result_projects_header(browser):
    """Test 'Projects' button in HEADER. [4] test from check-list"""

    LandingPage(browser).\
        click_on_projects_header()


@pytest.mark.skip(reason="Auto-Scroll to mentor's block works wrong")
@allure.feature("functional")
def test_expected_result_mentors_header(browser):
    """Test 'Mentors' button in HEADER. [5] test from check-list"""

    LandingPage(browser).\
        click_on_mentors_header()


@pytest.mark.skip(reason="Auto-Scroll to StartUp_For block works wrong")
@allure.feature("functional")
def test_expected_result_startup_for_header(browser):
    """Test 'StartUp_For' button in HEADER. [6] test from check-list"""

    LandingPage(browser).\
        click_on_startup_for_header()


@allure.feature("functional")
def test_expected_result_sun_icon_header(browser):
    """Test 'Sun_Icon' button in HEADER. [7] test from check-list"""
    
    LandingPage(browser).\
        click_on_sun_icon_header()


@allure.feature("functional")
def test_expected_result_join_header(browser):
    """Test 'Join' button in HEADER. [9] test from check-list"""

    LandingPage(browser).\
        click_on_join_header()


@allure.feature("non-functional")
def test_logo_gif_your_opportunity_block(browser):
    """Test 'Logo_Gif' in block YOUR_OPPORTYNITY is present and displayed. [11] test from check-list"""

    LandingPage(browser).\
        checking_logo_gif_in_your_opportunity_block_is_present_and_displayed()


@allure.feature("non-functional")
def test_text_your_opportunity_block(browser):
    """Test 'Main_Title' and 'Description' in YOUR OPPORTUNITY block is present and displayed. [12] test from check-list"""

    LandingPage(browser).\
        checking_main_title_in_your_opportunity_block_is_present_and_displayed().\
        checking_description_in_your_opportunity_block_is_present_and_displayed()


@allure.feature("non-functional")
def test_about_us_block(browser):
    """Test About_Us title and description is present and displayed. [13] test from check-list"""
    
    LandingPage(browser).\
        scroll_to_about_us().\
        checking_main_title_about_us_is_present_and_displayed().\
        checking_description_about_us_is_present_and_displayed()


@allure.feature("non-functional")
def test_why_exlab_block(browser):
    """Test Why_Exlab title and description is present and displayed. [14] test from check-list"""

    LandingPage(browser).\
        scroll_to_why_exlab().\
        checking_why_exlab_title_why_exlab_is_present_and_displayed().\
        checking_description_why_exlab_is_present_and_displayed()


@allure.feature("functional")
def test_join_why_exlab_block(browser):
    """Test 'Join' button in Why Exlab block. [15] test from check-list"""

    LandingPage(browser).\
        click_on_join_why_exlab()


@allure.feature("non-functional")
def test_title_projects_block(browser):
    """Test 'Projects' title in Projects block is present and displayed. [16] test from check-list"""

    LandingPage(browser).\
        scroll_to_project().\
        checking_projects_title_is_present_and_displayed()


@allure.feature("non-functional")
def test_logos_and_descriptions_projects_block(browser):
    """Test logos and descriptions of projects in Projects block are present and displayed. [17] test from check-list"""

    LandingPage(browser).\
        scroll_to_project().\
        checking_logos_and_descriptions_projects_block()


@allure.feature("non-functional")
def test_title_mentors_block(browser):
    """Test Mentors_Title in Mentors block are present and displayed. [18] test from check-list"""

    LandingPage(browser).\
        scroll_to_mentors().\
        checking_title_mentors_is_present_and_displayed()


@allure.feature("functional")
def test_mentors_spoilers(browser):
    """Test spoilers of mentors in mentors block. [20] test from check-list"""

    LandingPage(browser).\
        scroll_to_mentors().\
        check_all_mentors_spoilers()
        #To Do: подумать об объединении 

@allure.feature("non-functional")
def test_title_startup_for_block(browser):
    """Test StartUp_For_Title in StartUp_For block are present and displayed. [24] test from check-list"""

    LandingPage(browser).\
        scroll_to_startup_for().\
        checking_title_startup_for_is_present_and_displayed()


@allure.feature("non-functional")
def test_descriptions_startup_for_block(browser):
    """Test Descriptions in StartUp_For block are present and displayed. [28] test from check-list"""

    LandingPage(browser).\
        scroll_to_startup_for().\
        checking_descriptions_startup_for_is_present_and_displayed()


@allure.feature("non-functional")
def test_title_help_project_block(browser):
    """Test Help_Project_Title in Help_Project block are present and displayed. [30] test from check-list"""

    LandingPage(browser).\
        scroll_to_help_project().\
        checking_title_help_project_is_present_and_displayed()


@allure.feature("non-functional")
def test_description_help_project_block(browser):
    """Test Description in Help_Project block are present and displayed. [31] test from check-list"""

    LandingPage(browser).\
        scroll_to_help_project().\
        checking_description_help_project_is_present_and_displayed()
    

@allure.feature("functional")
def test_expected_result_boosty_button_help_project(browser):
    """Test Boosty button in Help Project block. [32] test from check-list"""

    LandingPage(browser).\
        click_on_boosty_help_project()


@allure.feature("functional")
def test_expected_result_patreon_button_help_project(browser):
    """Test Patreon button in Help Project block. [33] test from check-list. Without Patreon page checking"""
    
    LandingPage(browser).\
        scroll_to_help_project().\
        checking_patreon_help_project_button_is_present_and_displayed()
        #To Do: написать реализацию кнопки Patreon, когда добавят функционал


@allure.feature("non-functional")
def test_title_stay_connected_block(browser):
    """Test Title_Stay_Connected in FOOTER block are present and displayed. [34] test from check-list"""

    LandingPage(browser).\
        scroll_to_footer().\
        checking_title_stay_connected_is_present_and_displayed()


@allure.feature("non-functional")
def test_description_stay_connected_block(browser):
    """Test description in FOOTER block are present and displayed. [35] test from check-list"""

    LandingPage(browser).\
        scroll_to_footer().\
        checking_description_stay_connected_is_present_and_displayed()


@allure.feature("non-functional")
def test_logo_footer_block(browser):
    """Test Logo in FOOTER block are present and displayed. [36] test from check-list"""

    LandingPage(browser).\
        scroll_to_footer().\
        checking_logo_footer_is_present_and_displayed()


@allure.feature("non-functional")
def test_text_under_logo_footer_block(browser):
    """Test Text_Under_Logo in FOOTER block are present and displayed. [37] test from check-list"""

    LandingPage(browser).\
        scroll_to_footer().\
        checking_text_under_logo_footer_is_present_and_displayed()


@allure.feature('functional')
def test_expected_result_linkedin_footer(browser):
    """Test 'Linkedin' button in FOOTER. [38] test from check-list"""

    LandingPage(browser).\
        click_on_linkedin_footer()


@allure.feature('functional')
def test_expected_result_instagram_footer(browser):
    """Test 'Instagram' button in FOOTER. [39] test from check-list"""

    LandingPage(browser).\
        click_on_instagram_footer()


@allure.feature('functional')
def test_expected_result_telegram_footer(browser):
    """Test 'Telegram' button in FOOTER. [40] test from check-list"""

    LandingPage(browser).\
        click_on_telegram_footer()


@allure.feature('functional')
def test_expected_result_youtube_footer(browser):
    """Test 'Youtube' button in FOOTER. [41] test from check-list"""

    LandingPage(browser).\
        click_on_youtube_footer()


@allure.feature("non-functional")
def test_mail_address_footer_block(browser):
    """Test Mail_Address in FOOTER block are present and displayed. [42] test from check-list"""

    LandingPage(browser).\
        scroll_to_footer().\
        checking_mail_address_footer_is_present_and_displayed()