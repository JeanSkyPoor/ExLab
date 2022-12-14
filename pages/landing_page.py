from pages.locators import LandingPageLocators
from pages.base_page import BasePage
import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class LandingPage(BasePage):
    
    def __init__(self, browser) -> None:
        link = 'http://test.exlab.team/'
        
        super().__init__(browser, link)


    def checking_landing_url(self):
        """Checking that landing URL is correct"""

        self.matching_current_and_correct_urls('http://test.exlab.team/')


    def checking_dark_mode_on(self):
        """Checking if dark mode on"""

        self.matching_attribute_value_with_correct_value(LandingPageLocators.THEME, 'class', 'sc-bczRLJ ckyTig')

    def checking_light_mode_on(self):
        """Checking if light mode on"""

        self.matching_attribute_value_with_correct_value(LandingPageLocators.THEME, 'class', 'sc-bczRLJ cxdoLY')


    def checking_logo_header_is_present_and_displayed(self):
        """Checking 'Logo' in HEADER is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.HEADER_EXLAB_LOGO, 'Logo', 'HEADER')
        self.checking_is_element_displayed(LandingPageLocators.HEADER_EXLAB_LOGO, 'Logo', 'HEADER')
        

    def checking_about_us_header_is_present_and_displayed(self):
        """Checking 'About_Us' button in HEADER is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.HEADER_ABOUT_US_BUTTON, 'About_Us', 'HEADER')
        self.checking_is_element_displayed(LandingPageLocators.HEADER_ABOUT_US_BUTTON, 'About_Us', 'HEADER')

    def click_on_about_us_header(self):
        """Click on 'About Us' button in HEADER"""

        self.click_on_element(LandingPageLocators.HEADER_ABOUT_US_BUTTON)


    def checking_projects_header_is_present_and_displayed(self):
        """Checking Project button in HEADER is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.HEADER_PROJECTS_BUTTON, 'Projects', 'HEADER')
        self.checking_is_element_displayed(LandingPageLocators.HEADER_PROJECTS_BUTTON, 'Projects', 'HEADER')

    def click_on_projects_header(self):
        """Click on 'Projects' button in HEADER"""

        self.click_on_element(LandingPageLocators.HEADER_PROJECTS_BUTTON)


    def checking_mentors_header_is_present_and_displayed(self):
        """Checking 'Mentors' button in HEADER is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.HEADER_MENTORS_BUTTON, 'Mentors', 'HEADER')
        self.checking_is_element_displayed(LandingPageLocators.HEADER_MENTORS_BUTTON, 'Mentors', 'HEADER')

    def click_on_mentors_header(self):
        """Click on 'Mentors' button in HEADER"""

        self.click_on_element(LandingPageLocators.HEADER_MENTORS_BUTTON)


    def checking_startup_for_header_is_present_and_displayed(self):
        """Checking 'StartUp_for' button in HEADER is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.HEADER_STARTUP_FOR_BUTTON, 'StartUp_For', 'HEADER')
        self.checking_is_element_displayed(LandingPageLocators.HEADER_STARTUP_FOR_BUTTON, 'StartUp_For', 'HEADER')

    def click_on_startup_for_header(self):
        """Click on 'Startup For' button in HEADER"""

        self.click_on_element(LandingPageLocators.HEADER_STARTUP_FOR_BUTTON)

 
    def checking_sun_icon_header_is_present_and_displayed(self):
        """Checking 'Sun_icon' button in HEADER is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.HEADER_SUN_ICON, 'Sun_Icon', 'HEADER')
        self.checking_is_element_displayed(LandingPageLocators.HEADER_SUN_ICON, 'Sun_Icon', 'HEADER')

    def click_on_sun_icon_header(self):
        """Click on 'Sun_Icon' button in HEADER"""

        self.click_on_element(LandingPageLocators.HEADER_SUN_ICON)


    def checking_join_header_is_present_and_displayed(self):
        """Checking 'Join' button in HEADER is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.HEADER_JOIN_BUTTON, 'Join', 'HEADER')
        self.checking_is_element_displayed(LandingPageLocators.HEADER_JOIN_BUTTON, 'Join', 'HEADER')

    def click_on_join_header(self):
        """Click on 'Join' button in HEADER"""

        self.click_on_element(LandingPageLocators.HEADER_JOIN_BUTTON)

    def checking_url_after_click_on_join_header(self):
        """Switch to the last opened window and check URL"""

        self.switch_to_the_last_opened_window()
        self.url_have_to_contain('https://t.me')


    def checking_logo_gif_in_your_opportunity_block_is_present_and_displayed(self):
        """Checking 'Logo_Gif' in block YOUR OPPORTUNITY is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.YOUR_OPPORTUNITY_LOGO, 'Logo_Gif', 'YOUR_OPPORTUNITY')
        self.checking_is_element_displayed(LandingPageLocators.YOUR_OPPORTUNITY_LOGO, 'Logo_Gif', 'YOUR_OPPORTUNITY')

    def checking_main_title_in_your_opportunity_block_is_present_and_displayed(self):
        """Checking 'Main_Title' in your opportynity block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.YOUR_OPPORTUNITY_MAIN_TITLE, 'Main_Title', 'YOUR_OPPORTUNITY')
        self.checking_is_element_displayed(LandingPageLocators.YOUR_OPPORTUNITY_MAIN_TITLE, 'Main_Title', 'YOUR_OPPORTUNITY')

    def checking_description_in_your_opportunity_block_is_present_and_displayed(self):
        """Checking 'Description' in your opportunity block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.YOUR_OPPORTUNITY_DESCRIPTION, 'Description', 'YOUR_OPPORTUNITY')
        self.checking_is_element_displayed(LandingPageLocators.YOUR_OPPORTUNITY_DESCRIPTION, 'Description', 'YOUR_OPPORTUNITY')


    def checking_about_us_anchor_after_shifting(self):
        """Checking anchor element in 'About Us' block"""

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_ABOUT_US, 'About_Us')

    def checking_why_exlab_anchor_after_shifting(self):
        """Checking anchor element in 'Why Exlab' block"""

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_WHY_EXLAB, 'Why_Exlab')

    def checking_projects_anchor_after_shifting(self):
        """Checking anchor element in 'Projects' block"""

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_PROJECTS, 'Project')

    def checking_mentors_anchor_after_shifting(self):
        """Checking anchor element in 'Mentors' block"""

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_MENTORS, 'Mentors')

    def checking_startup_for_anchor_after_shifting(self):
        """Checking anchor element in 'StartUp for' block"""

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_STARTUP_FOR, 'StartUp_For')

    def checking_help_project_anchor_after_shifting(self):
        """Checking anchor element in 'Help project' block"""

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_HELP_PROJECT, 'Help_Project')

    def checking_footer_anchor_after_shifting(self):
        """Checking anchor element in 'Footer' block"""

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_FOOTER, 'Footer')


    def scroll_to_about_us(self):
        """Scroll from top to 'About us' block and check anchor element"""

        elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:2])
        self.checking_about_us_anchor_after_shifting()

    def scroll_to_why_exlab(self):
        """Scroll from top to 'Why Exlab' block and check anchor element"""

        elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:2]) 
        self.scroll_down_element_to_element([self.browser.find_element(*LandingPageLocators.ANCHOR_WHY_EXLAB)]) #Костыль!
        self.checking_why_exlab_anchor_after_shifting()

    def scroll_to_project(self):
        """Scroll from top to 'Project' block and check anchor element"""

        elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:3])
        self.checking_projects_anchor_after_shifting()

    def scroll_to_mentors(self):
        """Scroll from top to 'Mentors' block and check anchor element"""

        elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:4])
        self.checking_mentors_anchor_after_shifting()

    def scroll_to_startup_for(self):
        """Scroll from top to 'StartUp for' block and check anchor element"""

        elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:5])
        self.checking_startup_for_anchor_after_shifting()

    def scroll_to_help_project(self):
        """Scroll from top to 'Help project' block and check anchor element"""

        elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:6])
        self.checking_help_project_anchor_after_shifting()
     
    def scroll_to_footer(self):
        """Scroll from top to 'Footer' block and check anchor element"""

        elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:7])
        self.checking_footer_anchor_after_shifting()


    def checking_linkedin_footer_is_present_and_displayed(self):
        """Checking 'Linkedin' button in FOOTER is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.FOOTER_LINKEDIN, 'Linkedin', 'FOOTER')
        self.checking_is_element_displayed(LandingPageLocators.FOOTER_LINKEDIN, 'Linkedin', 'FOOTER')

    def click_on_linkedin_footer(self):
        """Click on 'Linkedin' button in FOOTER"""

        self.click_on_element(LandingPageLocators.FOOTER_LINKEDIN)

    def checking_url_after_click_on_linkedin_footer(self):
        """Switch to the last opened window and check URL"""

        self.switch_to_the_last_opened_window()
        self.url_have_to_contain('https://www.linkedin.com')


    def checking_instagram_footer_is_present_and_displayed(self):
        """Checking 'Instagram' button in FOOTER is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.FOOTER_INSTAGRAM, 'Instagram', 'FOOTER')
        self.checking_is_element_displayed(LandingPageLocators.FOOTER_INSTAGRAM, 'Instagram', 'FOOTER')

    def click_on_instagram_footer(self):
        """Click on 'Instagram' button in FOOTER"""

        self.click_on_element(LandingPageLocators.FOOTER_INSTAGRAM)

    def checking_url_after_click_on_instagram_footer(self):
        """Switch to the last opened window and check URL"""

        self.switch_to_the_last_opened_window()
        self.url_have_to_contain('https://www.instagram.com')


    def checking_telegram_footer_is_present_and_displayed(self):
        """Checking 'Telegram' button in FOOTER is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.FOOTER_TELEGRAM, 'Telegram', 'FOOTER')
        self.checking_is_element_displayed(LandingPageLocators.FOOTER_TELEGRAM, 'Telegram', 'FOOTER')

    def click_on_telegram_footer(self):
        """Click on 'Telegram' button in FOOTER"""

        self.click_on_element(LandingPageLocators.FOOTER_TELEGRAM)

    def checking_url_after_click_on_telegram_footer(self):
        """Switch to the last opened window and check URL"""
 
        self.switch_to_the_last_opened_window()
        self.url_have_to_contain('https://t.me')


    def checking_youtube_footer_is_present_and_displayed(self):
        """Checking 'Youtube' button in FOOTER is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.FOOTER_YOUTUBE, 'Youtube', 'FOOTER')
        self.checking_is_element_displayed(LandingPageLocators.FOOTER_YOUTUBE, 'Youtube', 'FOOTER')

    def click_on_youtube_footer(self):
        """Click on 'Youtube' button in FOOTER"""

        self.click_on_element(LandingPageLocators.FOOTER_YOUTUBE)

    def checking_url_after_click_on_youtube_footer(self):
        """Switch to the last opened window and check URL"""

        self.switch_to_the_last_opened_window()
        self.url_have_to_contain('https://www.youtube.com')


    def checking_join_why_exlab_is_present_and_displayed(self):
        """Checking 'Join' button in 'Why Exlab' is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.WHY_EXLAB_JOIN_BUTTON, 'Join', 'Why_Exlab')
        self.checking_is_element_displayed(LandingPageLocators.WHY_EXLAB_JOIN_BUTTON, 'Join', 'Why_Exlab')

    def click_on_join_why_exlab(self):
        """Click on 'Join' button in Why Exlab block"""

        self.click_on_element(LandingPageLocators.WHY_EXLAB_JOIN_BUTTON)

    def checking_url_after_click_on_join_why_exlab(self):
        """Switch to the last opened window and check URL"""

        self.switch_to_the_last_opened_window()
        self.url_have_to_contain('https://t.me')


    def check_all_mentors_spoilers(self):
        """One by one checking mentor's spoilers in mentors block"""

        try:
            spoilers = self.browser.find_elements(*LandingPageLocators.MENTORS_ALL_SPOILERS_BLOCK)
        except NoSuchElementException:
            raise NoSuchElementException("Mentor's spoilers is not found")
            
        for index, spoiler in enumerate(spoilers):
            with allure.step(f"Checking {index+1} spoiler of mentors"):
                locator = (By.CSS_SELECTOR, f'div:nth-child({index+1}) > div.sc-bUbCnL.gFhhBm') #локатор закрытого спойлера

                spoiler.click()

                if self.is_visibility_of_element_located(LandingPageLocators.MENTORS_BLOCK_WITH_DATA_OPENED_SPOILER, checking_time=0.5) != True: 
                    self.attach_screenshot('Block_with_data_of_mentor_is_not_displayed')           
                    raise AssertionError(f"Block with data of mentor is not displayed. {index+1} spoiler")

                if self.is_visibility_of_element_located(LandingPageLocators.MENTOR_IMAGE, checking_time=0.5) != True:
                    self.attach_screenshot('Image_of_mentor_is_not_displayed') 
                    raise AssertionError(f"Image of mentor is not displayed. {index+1} spoiler")    

                if self.is_visibility_of_element_located(LandingPageLocators.MENTOR_DESCRIPTION, checking_time=0.5) != True:
                    self.attach_screenshot('Description_info_of_mentor_is_not_displayed') 
                    raise AssertionError(f"Description info of mentor is not displayed. {index+1} spoiler")

                spoiler.click()
    
                if self.is_element_present(locator) != True: #При закрытом спойлере появляется объект с локатором locator, если спойлер не закрыть, объекта не будет и тест упадет
                    self.attach_screenshot('Spoiler_is_not_closed') 
                    raise AssertionError(f"Spoiler is not closed. {index+1} spoiler")
                    #TO DO: по возможности переделать этот метод

    
    def checking_boosty_help_project_button_is_present_and_displayed(self):
        """Checking 'Boosty' button in Help Project block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.HELP_PROJECT_BOOSTY_BUTTON, 'Boosty', 'Help_Project')
        self.checking_is_element_displayed(LandingPageLocators.HELP_PROJECT_BOOSTY_BUTTON, 'Boosty', 'Help_Project')

    def checking_patreon_help_project_button_is_present_and_displayed(self):
        """Checking 'Patreon' button in Help Project block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.HELP_PROJECT_PATREON_BUTTON, 'Patreon', 'Help_Project')
        self.checking_is_element_displayed(LandingPageLocators.HELP_PROJECT_PATREON_BUTTON, 'Patreon', 'Help_Project')

                
    def click_on_boosty_help_project(self):
        """Click on 'Boosty' button in Help Project block"""

        self.click_on_element(LandingPageLocators.HELP_PROJECT_BOOSTY_BUTTON)
            
    def checking_url_after_click_on_boosty_help_project(self):
        """Switch to the last opened window and check URL"""

        self.switch_to_the_last_opened_window()
        self.url_have_to_contain('https://boosty.to')
        

    def checking_main_title_about_us_is_present_and_displayed(self):
        """Checking About_Us title in About_Us block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.ABOUT_US_MAIN_TITLE, 'About_Us_Title', 'About_Us')
        self.checking_is_element_displayed(LandingPageLocators.ABOUT_US_MAIN_TITLE, 'About_Us_Title', 'About_Us')

    def checking_description_about_us_is_present_and_displayed(self):
        """Checking description in About_Us block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.ABOUT_US_DESCRIPTION, 'Description_About_Us', 'About_Us')
        self.checking_is_element_displayed(LandingPageLocators.ABOUT_US_DESCRIPTION, 'Description_About_Us', 'About_Us')


    def checking_why_exlab_title_why_exlab_is_present_and_displayed(self):
        """Checking Why_Exlab_Title in Why_Exlab block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.WHY_EXLAB_MAIN_TITLE, 'Why_Exlab_Title', 'Why_Exlab')
        self.checking_is_element_displayed(LandingPageLocators.WHY_EXLAB_MAIN_TITLE, 'Why_Exlab_Title', 'Why_Exlab')

    def checking_description_why_exlab_is_present_and_displayed(self):
        """Checking description in Why_Exlab block is present and displayed"""  

        self.checking_is_element_present(LandingPageLocators.WHY_EXLAB_DESCRIPTION, 'Description_Why_Exlab', 'Why_Exlab')
        self.checking_is_element_displayed(LandingPageLocators.WHY_EXLAB_DESCRIPTION, 'Description_Why_Exlab', 'Why_Exlab')

    
    def checking_projects_title_is_present_and_displayed(self):
        """Checking Projects_Title in Projects block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.PROJECTS_MAIN_TITLE, 'Projects_Title', 'Projects')
        self.checking_is_element_displayed(LandingPageLocators.PROJECTS_MAIN_TITLE, 'Projects_Title', 'Projects')


    def checking_logos_and_descriptions_projects_block(self):
        """One by One checking logos and descriptions of projects in Projects block"""

        try:
            projects = self.browser.find_elements(*LandingPageLocators.PROJECTS_ALL_PROJECTS_BLOCK)
        except NoSuchElementException:
            raise NoSuchElementException("Projects is not found")

        for index, project in enumerate(projects):
            img_locator = (By.CSS_SELECTOR, f'div.sc-hTtwUo.dfmShq > div:nth-child({index+1}) > img')
            description_locator = (By.CSS_SELECTOR, f'div.sc-hTtwUo.dfmShq > div:nth-child({index+1}) > p')

            self.browser.execute_script("arguments[0].scrollIntoView();", project)

            self.checking_is_element_present(img_locator, 'Logo', f'{index+1} project')
            self.checking_is_element_displayed(img_locator, 'Logo', f'{index+1} project')

            self.checking_is_element_present(description_locator, 'Description', f'{index+1} project')
            self.checking_is_element_displayed(description_locator, 'Description', f'{index+1} project')
            time.sleep(0.5)
        

    def checking_title_mentors_is_present_and_displayed(self):
        """Checking Mentors_Title in Mentors block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.MENTORS_TITLE, 'Mentors_Title', 'Mentors')
        self.checking_is_element_displayed(LandingPageLocators.MENTORS_TITLE, 'Mentors_Title', 'Mentors')

    
    def checking_title_startup_for_is_present_and_displayed(self):
        """Checking StartUp_For_Title in StartUp_For block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.STARTUP_FOR_MAIN_TITLE, 'StartUp_For_Title', 'StartUp_For')
        self.checking_is_element_displayed(LandingPageLocators.STARTUP_FOR_MAIN_TITLE, 'StartUp_For_Title', 'StartUp_For')

    def checking_descriptions_startup_for_is_present_and_displayed(self):
        """Checking Descriptions in StartUp_For block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.STARTUP_FOR_JUNIORS_DESCRIPTION, 'Junior_Description', 'StartUp_For')
        self.checking_is_element_displayed(LandingPageLocators.STARTUP_FOR_JUNIORS_DESCRIPTION, 'Junior_Description', 'StartUp_For')

        self.scroll_down_element_to_element([self.browser.find_element(*LandingPageLocators.STARTUP_FOR_RECRUTER_DESCRIPTION)]) #Костыль!

        self.checking_is_element_present(LandingPageLocators.STARTUP_FOR_RECRUTER_DESCRIPTION, 'Recruter_Description', 'StartUp_For')
        self.checking_is_element_displayed(LandingPageLocators.STARTUP_FOR_RECRUTER_DESCRIPTION, 'Recruter_Description', 'StartUp_For')
 
        
    def checking_title_help_project_is_present_and_displayed(self):
        """Checking Help_Project_Title in Help_Project block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.HELP_PROJECT_TITLE, 'Help_Project_Title', 'Help_Project')
        self.checking_is_element_displayed(LandingPageLocators.HELP_PROJECT_TITLE, 'Help_Project_Title', 'Help_Project')

    def checking_description_help_project_is_present_and_displayed(self):
        """Checking Description in Help_Project block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.HELP_PROJECT_DESCRIPTION, 'Description_Help_Project', 'Help_Project')
        self.checking_is_element_displayed(LandingPageLocators.HELP_PROJECT_DESCRIPTION, 'Description_Help_Project', 'Help_Project')


    def checking_title_stay_connected_is_present_and_displayed(self):
        """Checking Title_Stay_Connected in Stay_Connected block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.FOOTER_STAY_CONNECTED_TITLE, 'Title_Stay_Connected', 'FOOTER')
        self.checking_is_element_displayed(LandingPageLocators.FOOTER_STAY_CONNECTED_TITLE, 'Title_Stay_Connected', 'FOOTER')

    def checking_description_stay_connected_is_present_and_displayed(self):
        """Checking Description in Stay_Connected block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.FOOTER_DESCRIPTION_STAY_CONNECTED, 'Description_Stay_Connected', 'FOOTER')
        self.checking_is_element_displayed(LandingPageLocators.FOOTER_DESCRIPTION_STAY_CONNECTED, 'Description_Stay_Connected', 'FOOTER')

    
    def checking_logo_footer_is_present_and_displayed(self):
        """Checking Logo in FOOTER block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.FOOTER_LOGO, 'Logo', 'FOOTER')
        self.checking_is_element_displayed(LandingPageLocators.FOOTER_LOGO, 'Logo', 'FOOTER')

    def checking_text_under_logo_footer_is_present_and_displayed(self):
        """Checking Text_Under_Logo in FOOTER block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.FOOTER_UNDER_LOGO_TEXT, 'Text_Under_Logo', 'FOOTER')
        self.checking_is_element_displayed(LandingPageLocators.FOOTER_UNDER_LOGO_TEXT, 'Text_Under_Logo', 'FOOTER')
    
    def checking_mail_address_footer_is_present_and_displayed(self):
        """Checking Mail_Address in FOOTER block is present and displayed"""

        self.checking_is_element_present(LandingPageLocators.FOOTER_MAIL_ADDRESS, 'Mail_Address', 'FOOTER')
        self.checking_is_element_displayed(LandingPageLocators.FOOTER_MAIL_ADDRESS, 'Mail_Address', 'FOOTER')