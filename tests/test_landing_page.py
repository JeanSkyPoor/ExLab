from pages.landing_page import LandingPage
import pytest
import allure


@allure.feature("Unfunctional")
def test_landing_url_and_black_theme(browser):
    """Test landing URL and black theme on default. [1] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.checking_dark_mode_on()


@allure.feature("Functional")
def test_logo_exlab_header(browser):
    """Test logo ExLab in HEADER. [2] test from check-list. Without refresh method in test"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.checking_logo_header_is_present_and_displayed()
    #TO DO: доделать, когда добавят функцию рефреша страницы


@allure.feature("Functional")
def test_about_us_header(browser):
    """Test 'About_Us' button in HEADER. [3] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()  

    page.checking_about_us_header_is_present_and_displayed()
    page.click_on_about_us_header() 
    page.checking_about_us_anchor_after_shifting() 


@allure.feature("Functional")
def test_projects_header(browser):
    """Test 'Projects' button in HEADER. [4] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.checking_projects_header_is_present_and_displayed()
    page.click_on_projects_header()   
    page.checking_projects_anchor_after_shifting()


@pytest.mark.skip(reason="Auto-Scroll to mentor's block works wrong")
@allure.feature("Functional")
def test_mentors_header(browser):
    """Test 'Mentors' button in HEADER. [5] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url() 

    page.checking_mentors_header_is_present_and_displayed()
    page.click_on_mentors_header()     
    page.checking_mentors_anchor_after_shifting()


@pytest.mark.skip(reason="Auto-Scroll to StartUp_For block works wrong")
@allure.feature("Functional")
def test_startup_for_header(browser):
    """Test 'StartUp_For' button in HEADER. [6] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.checking_startup_for_header_is_present_and_displayed()
    page.click_on_startup_for_header()
    page.checking_startup_for_anchor_after_shifting()


@allure.feature("Functional")
def test_sun_icon_header(browser):
    """Test 'Sun_Icon' button in HEADER. [7] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.checking_sun_icon_header_is_present_and_displayed()
    page.click_on_sun_icon_header()
    page.checking_light_mode_on()
    

@allure.feature("Functional")
def test_join_header(browser):
    """Test 'Join' button in HEADER. [9] test from check-list"""
    page = LandingPage(browser)
    page.open() 
    page.checking_landing_url()

    page.checking_join_header_is_present_and_displayed()
    page.click_on_join_header()
    page.checking_url_after_click_on_join_header()


@allure.feature("Unfunctional")
def test_logo_gif_your_opportunity_block(browser):
    """Test 'Logo_Gif' in block YOUR_OPPORTYNITY is present and displayed. [11] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.checking_logo_gif_in_your_opportunity_block_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_text_your_opportunity_block(browser):
    """Test 'Main_Title' and 'Description' in YOUR OPPORTUNITY block is present and displayed. [12] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.checking_main_title_in_your_opportunity_block_is_present_and_displayed()
    page.checking_description_in_your_opportunity_block_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_about_us_block(browser):
    """Test About_Us title and description is present and displayed. [13] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.scroll_to_about_us()    
    page.checking_main_title_about_us_is_present_and_displayed()
    page.checking_description_about_us_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_why_exlab_block(browser):
    """Test Why_Exlab title and description is present and displayed. [14] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.scroll_to_why_exlab()
    page.checking_why_exlab_title_why_exlab_is_present_and_displayed()
    page.checking_description_why_exlab_is_present_and_displayed()


@allure.feature("Functional")
def test_join_why_exlab_block(browser):
    """Test 'Join' button in Why Exlab block. [15] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.scroll_to_why_exlab()
    page.checking_join_why_exlab_is_present_and_displayed()
    page.click_on_join_why_exlab()
    page.checking_url_after_click_on_join_why_exlab()


@allure.feature("Unfunctional")
def test_title_projects_block(browser):
    """Test 'Projects' title in Projects block is present and displayed. [16] test from check-list"""
    page = LandingPage(browser)
    page.open()   
    page.checking_landing_url()
    
    page.scroll_to_project()
    page.checking_projects_title_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_logos_and_descriptions_projects_block(browser):
    """Test logos and descriptions of projects in Projects block are present and displayed. [17] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.scroll_to_project()
    page.checking_logos_and_descriptions_projects_block()


@allure.feature("Unfunctional")
def test_title_mentors_block(browser):
    """Test Mentors_Title in Mentors block are present and displayed. [18] test from check-list"""
    page = LandingPage(browser)
    page.open()    
    page.checking_landing_url()
    
    page.scroll_to_mentors()
    page.checking_title_mentors_is_present_and_displayed()


@allure.feature("Functional")
def test_mentors_spoilers(browser):
    """Test spoilers of mentors in mentors block. [20] test from check-list"""
    page = LandingPage(browser)
    page.open()    
    page.checking_landing_url()
    
    page.scroll_to_mentors()
    page.check_all_mentors_spoilers()


@allure.feature("Unfunctional")
def test_title_startup_for_block(browser):
    """Test StartUp_For_Title in StartUp_For block are present and displayed. [24] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.scroll_to_startup_for()
    page.checking_title_startup_for_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_descriptions_startup_for_block(browser):
    """Test Descriptions in StartUp_For block are present and displayed. [28] test from check-list"""
    page = LandingPage(browser)
    page.open()    
    page.checking_landing_url()

    page.scroll_to_startup_for()
    page.checking_descriptions_startup_for_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_title_help_project_block(browser):
    """Test Help_Project_Title in Help_Project block are present and displayed. [30] test from check-list"""
    page = LandingPage(browser)
    page.open()    
    page.checking_landing_url()

    page.scroll_to_help_project()
    page.checking_title_help_project_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_description_help_project_block(browser):
    """Test Description in Help_Project block are present and displayed. [31] test from check-list"""
    page = LandingPage(browser)
    page.open()    
    page.checking_landing_url()
   
    page.scroll_to_help_project()
    page.checking_description_help_project_is_present_and_displayed()
    

@allure.feature("Functional")
def test_boosty_button_help_project(browser):
    """Test Boosty button in Help Project block. [32] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()
    
    page.scroll_to_help_project()   
    page.checking_boosty_help_project_button_is_present_and_displayed()
    page.click_on_boosty_help_project()
    page.checking_url_after_click_on_boosty_help_project()


@allure.feature("Functional")
def test_patreon_button_help_project(browser):
    """Test Patreon button in Help Project block. [33] test from check-list. Without Patreon page checking"""
    page = LandingPage(browser)
    page.open()    
    page.checking_landing_url()
   
    page.scroll_to_help_project()
    page.checking_patreon_help_project_button_is_present_and_displayed()
    #To Do: написать реализацию кнопки Patreon, когда добавят функционал


@allure.feature("Unfunctional")
def test_title_stay_connected_block(browser):
    """Test Title_Stay_Connected in FOOTER block are present and displayed. [34] test from check-list"""
    page = LandingPage(browser)
    page.open()    
    page.checking_landing_url()
    
    page.scroll_to_footer()
    page.checking_title_stay_connected_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_description_stay_connected_block(browser):
    """Test description in FOOTER block are present and displayed. [35] test from check-list"""
    page = LandingPage(browser)
    page.open()   
    page.checking_landing_url()

    page.scroll_to_footer()    
    page.checking_description_stay_connected_is_present_and_displayed()   


@allure.feature("Unfunctional")
def test_logo_footer_block(browser):
    """Test Logo in FOOTER block are present and displayed. [36] test from check-list"""
    page = LandingPage(browser)
    page.open() 
    page.checking_landing_url()

    page.scroll_to_footer()
    page.checking_logo_footer_is_present_and_displayed()


@allure.feature("Unfunctional")
def test_text_under_logo_footer_block(browser):
    """Test Text_Under_Logo in FOOTER block are present and displayed. [37] test from check-list"""
    page = LandingPage(browser)
    page.open()   
    page.checking_landing_url()
    
    page.scroll_to_footer()
    page.checking_text_under_logo_footer_is_present_and_displayed()


@allure.feature('Functional')
def test_linkedin_footer(browser):
    """Test 'Linkedin' button in FOOTER. [38] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.scroll_to_footer()
    page.checking_linkedin_footer_is_present_and_displayed()
    page.click_on_linkedin_footer()
    page.checking_url_after_click_on_linkedin_footer()


@allure.feature('Functional')
def test_instagram_footer(browser):
    """Test 'Instagram' button in FOOTER. [39] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()

    page.scroll_to_footer()    
    page.checking_instagram_footer_is_present_and_displayed()    
    page.click_on_instagram_footer()
    page.checking_url_after_click_on_instagram_footer()    


@allure.feature('Functional')
def test_telegram_footer(browser):
    """Test 'Telegram' button in FOOTER. [40] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()
    
    page.scroll_to_footer()
    page.checking_telegram_footer_is_present_and_displayed()
    page.click_on_telegram_footer()
    page.checking_url_after_click_on_telegram_footer()    


@allure.feature('Functional')
def test_youtube_footer(browser):
    """Test 'Youtube' button in FOOTER. [41] test from check-list"""
    page = LandingPage(browser)
    page.open()
    page.checking_landing_url()
   
    page.scroll_to_footer()
    page.checking_youtube_footer_is_present_and_displayed()
    page.click_on_youtube_footer()
    page.checking_url_after_click_on_youtube_footer()    


@allure.feature("Unfunctional")
def test_mail_address_footer_block(browser):
    """Test Mail_Address in FOOTER block are present and displayed. [42] test from check-list"""
    page = LandingPage(browser)
    page.open()    
    page.checking_landing_url()

    page.scroll_to_footer()  
    page.checking_mail_address_footer_is_present_and_displayed()