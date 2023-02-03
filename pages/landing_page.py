import allure
import time
from pages.locators import LandingPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    
    def __init__(self, browser, open_page: bool = True) -> None:
        link = 'http://test.exlab.team/'
        
        super().__init__(browser, link)
        
        if open_page == True:
            self.open()
            self.checking_landing_url()

    
    def checking_landing_url(self):
        """Checking that landing URL is correct"""
        
        with allure.step("Checking landing URL"):
            self.matching_current_and_correct_urls('http://test.exlab.team/')
            return self


    def checking_dark_mode_on(self):
        """ Checking if dark mode on """

        with allure.step("Checking dark mode on"):
            self.matching_attribute_value_with_correct_value(LandingPageLocators.THEME, 'class', 'sc-bczRLJ ckyTig')
            return self

    def checking_light_mode_on(self):
        """ Checking if light mode on """

        with allure.step("Checking light mode on"):
            self.matching_attribute_value_with_correct_value(LandingPageLocators.THEME, 'class', 'sc-bczRLJ cxdoLY')
            return self
    
    def checking_logo_header_is_present_and_displayed(self):
        """ Checking 'Logo' in HEADER is present and displayed """

        with allure.step("Checking Logo in HEADER is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.HEADER_EXLAB_LOGO, 'Logo', 'HEADER')
            self.checking_is_element_displayed(LandingPageLocators.HEADER_EXLAB_LOGO, 'Logo', 'HEADER')
            return self
        
    def checking_about_us_header_is_present_and_displayed(self):
        """ Checking 'About_Us' button in HEADER is present and displayed """

        with allure.step("Checking if 'About_Us' HEADER present and displayed"):
            self.checking_is_element_present(LandingPageLocators.HEADER_ABOUT_US_BUTTON, 'About_Us', 'HEADER')
            self.checking_is_element_displayed(LandingPageLocators.HEADER_ABOUT_US_BUTTON, 'About_Us', 'HEADER')
            return self
    
    def click_on_about_us_header(self):
        """ Click on 'About Us' button in HEADER """

        self.checking_about_us_header_is_present_and_displayed()
        self.click_on_element(LandingPageLocators.HEADER_ABOUT_US_BUTTON, 'About_Us', 'HEADER')
        self.checking_about_us_anchor_after_shifting()
        return self


    def checking_projects_header_is_present_and_displayed(self):
        """ Checking Project button in HEADER is present and displayed """

        with allure.step("Сhecking if 'Projects' HEADER present and displayed"):
            self.checking_is_element_present(LandingPageLocators.HEADER_PROJECTS_BUTTON, 'Projects', 'HEADER')
            self.checking_is_element_displayed(LandingPageLocators.HEADER_PROJECTS_BUTTON, 'Projects', 'HEADER')
            return self
    
    def click_on_projects_header(self):
        """ Click on 'Projects' button in HEADER """

        self.checking_projects_header_is_present_and_displayed()
        self.click_on_element(LandingPageLocators.HEADER_PROJECTS_BUTTON, 'Projects', 'HEADER')
        self.checking_projects_anchor_after_shifting()
        return self
    
    def checking_mentors_header_is_present_and_displayed(self):
        """ Checking 'Mentors' button in HEADER is present and displayed """

        with allure.step("Сhecking if 'Mentors' HEADER present and displayed"):
            self.checking_is_element_present(LandingPageLocators.HEADER_MENTORS_BUTTON, 'Mentors', 'HEADER')
            self.checking_is_element_displayed(LandingPageLocators.HEADER_MENTORS_BUTTON, 'Mentors', 'HEADER')
            return self
    
    def click_on_mentors_header(self):
        """ Click on 'Mentors' button in HEADER """

        self.checking_mentors_header_is_present_and_displayed()
        self.click_on_element(LandingPageLocators.HEADER_MENTORS_BUTTON, 'Mentors', 'HEADER')
        self.checking_mentors_anchor_after_shifting()
        return self
 
    def checking_startup_for_header_is_present_and_displayed(self):
        """ Checking 'StartUp_for' button in HEADER is present and displayed """

        with allure.step("Сhecking if 'StartUp_For' HEADER present and displayed"):
            self.checking_is_element_present(LandingPageLocators.HEADER_STARTUP_FOR_BUTTON, 'StartUp_For', 'HEADER')
            self.checking_is_element_displayed(LandingPageLocators.HEADER_STARTUP_FOR_BUTTON, 'StartUp_For', 'HEADER')
            return self
    
    def click_on_startup_for_header(self):
        """ Click on 'Startup For' button in HEADER """

        self.checking_startup_for_header_is_present_and_displayed()
        self.click_on_element(LandingPageLocators.HEADER_STARTUP_FOR_BUTTON, 'StartUp_For', 'HEADER')
        self.checking_startup_for_anchor_after_shifting()
        return self
    
    def checking_sun_icon_header_is_present_and_displayed(self):
        """ Checking 'Sun_icon' button in HEADER is present and displayed """

        with allure.step("Сhecking if 'Sun_Icon' HEADER present and displayed"):
            self.checking_is_element_present(LandingPageLocators.HEADER_SUN_ICON, 'Sun_Icon', 'HEADER')
            self.checking_is_element_displayed(LandingPageLocators.HEADER_SUN_ICON, 'Sun_Icon', 'HEADER')
            return self
    
    def click_on_sun_icon_header(self):
        """ Click on 'Sun_Icon' button in HEADER """

        self.checking_sun_icon_header_is_present_and_displayed()
        self.click_on_element(LandingPageLocators.HEADER_SUN_ICON, 'Sun_Icon', 'HEADER')
        self.checking_light_mode_on()
        return self
    
    def checking_join_header_is_present_and_displayed(self):
        """ Checking 'Join' button in HEADER is present and displayed """

        with allure.step("Сhecking if 'Join' HEADER present and displayed"):
            self.checking_is_element_present(LandingPageLocators.HEADER_JOIN_BUTTON, 'Join', 'HEADER')
            self.checking_is_element_displayed(LandingPageLocators.HEADER_JOIN_BUTTON, 'Join', 'HEADER')
            return self
    
    def click_on_join_header(self):
        """ Click on 'Join' button in HEADER """

        self.checking_join_header_is_present_and_displayed()
        self.click_on_element(LandingPageLocators.HEADER_JOIN_BUTTON, 'Join', 'HEADER')
        self.checking_url_after_click_on_join_header()
        return self
    
    def checking_url_after_click_on_join_header(self):
        """ Switch to the last opened window and check URL """

        with allure.step("Checking URL of opened page after click on 'Join' in HEADER"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://t.me')
            return self
    
    def checking_logo_gif_in_your_opportunity_block_is_present_and_displayed(self):
        """ Checking 'Logo_Gif' in block YOUR OPPORTUNITY is present and displayed """

        with allure.step("Checking if 'Logo_Gif' in block 'Your_Opportunity' is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.YOUR_OPPORTUNITY_LOGO, 'Logo_Gif', 'YOUR_OPPORTUNITY')
            self.checking_is_element_displayed(LandingPageLocators.YOUR_OPPORTUNITY_LOGO, 'Logo_Gif', 'YOUR_OPPORTUNITY')
            return self
    
    def checking_main_title_in_your_opportunity_block_is_present_and_displayed(self):
        """ Checking 'Main_Title' in your opportynity block is present and displayed """

        with allure.step("Checking if 'Main_Title' in block Your_Opportunity is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.YOUR_OPPORTUNITY_MAIN_TITLE, 'Main_Title', 'YOUR_OPPORTUNITY')
            self.checking_is_element_displayed(LandingPageLocators.YOUR_OPPORTUNITY_MAIN_TITLE, 'Main_Title', 'YOUR_OPPORTUNITY')
            return self
    
    def checking_description_in_your_opportunity_block_is_present_and_displayed(self):
        """ Checking 'Description' in your opportunity block is present and displayed """

        with allure.step("Checking if 'Description' in block Your_Opportunity is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.YOUR_OPPORTUNITY_DESCRIPTION, 'Description', 'YOUR_OPPORTUNITY')
            self.checking_is_element_displayed(LandingPageLocators.YOUR_OPPORTUNITY_DESCRIPTION, 'Description', 'YOUR_OPPORTUNITY')
            return self

    def checking_about_us_anchor_after_shifting(self):
        """ Checking anchor element in 'About Us' block """

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_ABOUT_US, 'About_Us')
        return self

    def checking_why_exlab_anchor_after_shifting(self):
        """ Checking anchor element in 'Why Exlab' block """

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_WHY_EXLAB, 'Why_Exlab')
        return self

    def checking_projects_anchor_after_shifting(self):
        """ Checking anchor element in 'Projects' block """

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_PROJECTS, 'Project')
        return self

    def checking_mentors_anchor_after_shifting(self):
        """ Checking anchor element in 'Mentors' block """

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_MENTORS, 'Mentors')
        return self

    def checking_startup_for_anchor_after_shifting(self):
        """ Checking anchor element in 'StartUp for' block """

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_STARTUP_FOR, 'StartUp_For')
        return self

    def checking_help_project_anchor_after_shifting(self):
        """ Checking anchor element in 'Help project' block """

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_HELP_PROJECT, 'Help_Project')
        return self

    def checking_footer_anchor_after_shifting(self):
        """ Checking anchor element in 'Footer' block """

        self.checking_visibility_of_element_located(LandingPageLocators.ANCHOR_FOOTER, 'Footer')
        return self
    
    def scroll_to_about_us(self):
        """ Scroll from top to 'About us' block and check anchor element """

        with allure.step("Scrolling to About_Us block and check anchor element"):
            elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
            self.scroll_down_element_to_element(elements[:2])
            self.checking_about_us_anchor_after_shifting()
            return self
    
    def scroll_to_why_exlab(self):
        """ Scroll from top to 'Why Exlab' block and check anchor element """

        with allure.step("Scrolling to Why_Exlab block and check anchor element"):
            elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
            self.scroll_down_element_to_element(elements[:2]) 
            self.scroll_down_element_to_element([self.browser.find_element(*LandingPageLocators.ANCHOR_WHY_EXLAB)]) #Костыль!
            self.checking_why_exlab_anchor_after_shifting()
            return self

    def scroll_to_project(self):
        """ Scroll from top to 'Project' block and check anchor element """

        with allure.step("Scrolling to Projects block and check anchor element"):
            elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
            self.scroll_down_element_to_element(elements[:3])
            self.checking_projects_anchor_after_shifting()
            return self
    
    def scroll_to_mentors(self):
        """ Scroll from top to 'Mentors' block and check anchor element """

        with allure.step("Scrolling to Mentors block and check anchor element"):
            elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
            self.scroll_down_element_to_element(elements[:4])
            self.checking_mentors_anchor_after_shifting()
            return self
    
    def scroll_to_startup_for(self):
        """ Scroll from top to 'StartUp for' block and check anchor element """

        with allure.step("Scrolling to StartUp_For block and check anchor element"):
            elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
            self.scroll_down_element_to_element(elements[:5])
            self.checking_startup_for_anchor_after_shifting()
            return self
    
    def scroll_to_help_project(self):
        """ Scroll from top to 'Help project' block and check anchor element """

        with allure.step("Scrolling to Help_Project block and check anchor element"):
            elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
            self.scroll_down_element_to_element(elements[:6])
            self.checking_help_project_anchor_after_shifting()
            return self
    
    def scroll_to_footer(self):
        """ Scroll from top to 'Footer' block and check anchor element """

        with allure.step("Scrolling to FOOTER block and check anchor element"):
            elements = self.browser.find_elements(*LandingPageLocators.SELECTOR_FOR_SCROLL)
            self.scroll_down_element_to_element(elements[:7])
            self.checking_footer_anchor_after_shifting()
            return self

    def checking_linkedin_footer_is_present_and_displayed(self):
        """ Checking 'Linkedin' button in FOOTER is present and displayed """

        with allure.step("Checking if 'Linkedin' button in FOOTER is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.FOOTER_LINKEDIN, 'Linkedin', 'FOOTER')
            self.checking_is_element_displayed(LandingPageLocators.FOOTER_LINKEDIN, 'Linkedin', 'FOOTER')
            return self
    
    def click_on_linkedin_footer(self):
        """ Click on 'Linkedin' button in FOOTER """

        self.scroll_to_footer()
        self.checking_linkedin_footer_is_present_and_displayed()
        self.click_on_element(LandingPageLocators.FOOTER_LINKEDIN, 'Linkedin', 'FOOTER')
        self.checking_url_after_click_on_linkedin_footer()
        return self
    
    def checking_url_after_click_on_linkedin_footer(self):
        """ Switch to the last opened window and check URL """

        with allure.step("Checking URL of opened page after click on 'Linkedin' in FOOTER"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://www.linkedin.com')
            return self
    
    def checking_instagram_footer_is_present_and_displayed(self):
        """ Checking 'Instagram' button in FOOTER is present and displayed """

        with allure.step("Checking if 'Instagram' button in FOOTER is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.FOOTER_INSTAGRAM, 'Instagram', 'FOOTER')
            self.checking_is_element_displayed(LandingPageLocators.FOOTER_INSTAGRAM, 'Instagram', 'FOOTER')
            return self
    
    def click_on_instagram_footer(self):
        """ Click on 'Instagram' button in FOOTER """

        self.scroll_to_footer()
        self.checking_instagram_footer_is_present_and_displayed()
        self.click_on_element(LandingPageLocators.FOOTER_INSTAGRAM, 'Instagram', 'FOOTER')
        self.checking_url_after_click_on_instagram_footer()
        return self
    
    def checking_url_after_click_on_instagram_footer(self):
        """ Switch to the last opened window and check URL """

        with allure.step("Checking URL of opened page after click on 'Instagram' in FOOTER"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://www.instagram.com')
            return self
    
    def checking_telegram_footer_is_present_and_displayed(self):
        """ Checking 'Telegram' button in FOOTER is present and displayed """

        with allure.step("Checking if 'Telegram' button in FOOTER is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.FOOTER_TELEGRAM, 'Telegram', 'FOOTER')
            self.checking_is_element_displayed(LandingPageLocators.FOOTER_TELEGRAM, 'Telegram', 'FOOTER')
            return self
    
    def click_on_telegram_footer(self):
        """ Click on 'Telegram' button in FOOTER """

        self.scroll_to_footer()
        self.checking_telegram_footer_is_present_and_displayed()
        self.click_on_element(LandingPageLocators.FOOTER_TELEGRAM, 'Telegram', 'FOOTER')
        self.checking_url_after_click_on_telegram_footer()
        return self
    
    def checking_url_after_click_on_telegram_footer(self):
        """ Switch to the last opened window and check URL """

        with allure.step("Checking URL of opened page after click on 'Telegram' in FOOTER"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://t.me')
            return self
    
    def checking_youtube_footer_is_present_and_displayed(self):
        """ Checking 'Youtube' button in FOOTER is present and displayed """

        with allure.step("Checking if 'Youtube' button in FOOTER is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.FOOTER_YOUTUBE, 'Youtube', 'FOOTER')
            self.checking_is_element_displayed(LandingPageLocators.FOOTER_YOUTUBE, 'Youtube', 'FOOTER')
            return self
    
    def click_on_youtube_footer(self):
        """ Click on 'Youtube' button in FOOTER """
        
        self.scroll_to_footer()
        self.checking_youtube_footer_is_present_and_displayed()
        self.click_on_element(LandingPageLocators.FOOTER_YOUTUBE, 'Youtube', 'FOOTER')
        self.checking_url_after_click_on_youtube_footer()
        return self
    
    def checking_url_after_click_on_youtube_footer(self):
        """ Switch to the last opened window and check URL """

        with allure.step("Checking URL of opened page after click on 'Youtube' in FOOTER"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://www.youtube.com')
            return self
    
    def checking_join_why_exlab_is_present_and_displayed(self):
        """ Checking 'Join' button in 'Why Exlab' is present and displayed """

        with allure.step("Checking if 'Join' button in 'Why Exlab' block is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.WHY_EXLAB_JOIN_BUTTON, 'Join', 'Why_Exlab')
            self.checking_is_element_displayed(LandingPageLocators.WHY_EXLAB_JOIN_BUTTON, 'Join', 'Why_Exlab')
            return self
    
    def click_on_join_why_exlab(self):
        """ Click on 'Join' button in Why Exlab block """

        self.scroll_to_why_exlab()
        self.checking_join_why_exlab_is_present_and_displayed()
        self.click_on_element(LandingPageLocators.WHY_EXLAB_JOIN_BUTTON, 'Join', 'Why_Exlab')
        self.checking_url_after_click_on_join_why_exlab()
        return self

    def checking_url_after_click_on_join_why_exlab(self):
        """ Switch to the last opened window and check URL """

        with allure.step("Checking URL of opened page after click on 'Join' in Why_Exlab block"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://t.me')
            return self
    
    def check_all_mentors_spoilers(self):
        """ One by one checking mentor's spoilers in mentors block """

        with allure.step("Checking all mentor's spoilers"):
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
            return self
    
    def checking_boosty_help_project_button_is_present_and_displayed(self):
        """ Checking 'Boosty' button in Help Project block is present and displayed """
        
        with allure.step("Checking if 'Boosty' button in Help Project block is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.HELP_PROJECT_BOOSTY_BUTTON, 'Boosty', 'Help_Project')
            self.checking_is_element_displayed(LandingPageLocators.HELP_PROJECT_BOOSTY_BUTTON, 'Boosty', 'Help_Project')
            return self
    
    def checking_patreon_help_project_button_is_present_and_displayed(self):
        """ Checking 'Patreon' button in Help Project block is present and displayed """

        with allure.step("Checking if 'Patreon' button in Help Project block is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.HELP_PROJECT_PATREON_BUTTON, 'Patreon', 'Help_Project')
            self.checking_is_element_displayed(LandingPageLocators.HELP_PROJECT_PATREON_BUTTON, 'Patreon', 'Help_Project')
            return self
                    
    def click_on_boosty_help_project(self):
        """ Click on 'Boosty' button in Help Project block """

        self.scroll_to_help_project()
        self.checking_boosty_help_project_button_is_present_and_displayed()
        self.click_on_element(LandingPageLocators.HELP_PROJECT_BOOSTY_BUTTON, 'Boosty', 'Help_Project')
        self.checking_url_after_click_on_boosty_help_project()
        return self
         
    def checking_url_after_click_on_boosty_help_project(self):
        """ Switch to the last opened window and check URL """

        with allure.step("Checking URL of opened page after click on 'Boosty' in Help_Project block"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://boosty.to') 
            return self
    
    def checking_main_title_about_us_is_present_and_displayed(self):
        """ Checking About_Us title in About_Us block is present and displayed """

        with allure.step("Checking if 'About_Us' main title in block About_Us is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.ABOUT_US_MAIN_TITLE, 'About_Us_Title', 'About_Us')
            self.checking_is_element_displayed(LandingPageLocators.ABOUT_US_MAIN_TITLE, 'About_Us_Title', 'About_Us')
            return self
   
    def checking_description_about_us_is_present_and_displayed(self):
        """ Checking description in About_Us block is present and displayed """

        with allure.step("Checking if description in block About_Us is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.ABOUT_US_DESCRIPTION, 'Description_About_Us', 'About_Us')
            self.checking_is_element_displayed(LandingPageLocators.ABOUT_US_DESCRIPTION, 'Description_About_Us', 'About_Us')
            return self
    
    def checking_why_exlab_title_why_exlab_is_present_and_displayed(self):
        """ Checking Why_Exlab_Title in Why_Exlab block is present and displayed """

        with allure.step("Checking if Why_Exlab title in block Why_Exlab is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.WHY_EXLAB_MAIN_TITLE, 'Why_Exlab_Title', 'Why_Exlab')
            self.checking_is_element_displayed(LandingPageLocators.WHY_EXLAB_MAIN_TITLE, 'Why_Exlab_Title', 'Why_Exlab')
            return self
    
    def checking_description_why_exlab_is_present_and_displayed(self):
        """ Checking description in Why_Exlab block is present and displayed """  

        with allure.step("Checking if description in block Why_Exlab is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.WHY_EXLAB_DESCRIPTION, 'Description_Why_Exlab', 'Why_Exlab')
            self.checking_is_element_displayed(LandingPageLocators.WHY_EXLAB_DESCRIPTION, 'Description_Why_Exlab', 'Why_Exlab')
            return self
    
    def checking_projects_title_is_present_and_displayed(self):
        """ Checking Projects_Title in Projects block is present and displayed """

        with allure.step("Checking if 'Project_Title' in 'Projects' block is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.PROJECTS_MAIN_TITLE, 'Projects_Title', 'Projects')
            self.checking_is_element_displayed(LandingPageLocators.PROJECTS_MAIN_TITLE, 'Projects_Title', 'Projects')
            return self
    
    def checking_logos_and_descriptions_projects_block(self):
        """ One by One checking logos and descriptions of projects in Projects block """

        with allure.step("Checking logos and descriptions of projects in Projects block"):
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
            return self
    
    def checking_title_mentors_is_present_and_displayed(self):
        """ Checking Mentors_Title in Mentors block is present and displayed """

        with allure.step("Checking if Mentors_Title in Mentors block is presend and displayed"):
            self.checking_is_element_present(LandingPageLocators.MENTORS_TITLE, 'Mentors_Title', 'Mentors')
            self.checking_is_element_displayed(LandingPageLocators.MENTORS_TITLE, 'Mentors_Title', 'Mentors')
            return self
    
    def checking_title_startup_for_is_present_and_displayed(self):
        """ Checking StartUp_For_Title in StartUp_For block is present and displayed """

        with allure.step("Checking if StartUp_For_Title in StartUp_For block is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.STARTUP_FOR_MAIN_TITLE, 'StartUp_For_Title', 'StartUp_For')
            self.checking_is_element_displayed(LandingPageLocators.STARTUP_FOR_MAIN_TITLE, 'StartUp_For_Title', 'StartUp_For')
            return self
    
    def checking_descriptions_startup_for_is_present_and_displayed(self):
        """ Checking Descriptions in StartUp_For block is present and displayed """

        with allure.step("Checking descriptions in block 'StartUp_For' is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.STARTUP_FOR_JUNIORS_DESCRIPTION, 'Junior_Description', 'StartUp_For')
            self.checking_is_element_displayed(LandingPageLocators.STARTUP_FOR_JUNIORS_DESCRIPTION, 'Junior_Description', 'StartUp_For')

            self.scroll_down_element_to_element([self.browser.find_element(*LandingPageLocators.STARTUP_FOR_RECRUTER_DESCRIPTION)]) #Костыль!

            self.checking_is_element_present(LandingPageLocators.STARTUP_FOR_RECRUTER_DESCRIPTION, 'Recruter_Description', 'StartUp_For')
            self.checking_is_element_displayed(LandingPageLocators.STARTUP_FOR_RECRUTER_DESCRIPTION, 'Recruter_Description', 'StartUp_For')
            return self
       
    def checking_title_help_project_is_present_and_displayed(self):
        """ Checking Help_Project_Title in Help_Project block is present and displayed """

        with allure.step("Checking if 'Help_Project_Title' in Help_Project block is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.HELP_PROJECT_TITLE, 'Help_Project_Title', 'Help_Project')
            self.checking_is_element_displayed(LandingPageLocators.HELP_PROJECT_TITLE, 'Help_Project_Title', 'Help_Project')
            return self
    
    def checking_description_help_project_is_present_and_displayed(self):
        """ Checking Description in Help_Project block is present and displayed """

        with allure.step("Checking descriptions in block 'Help_Project' is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.HELP_PROJECT_DESCRIPTION, 'Description_Help_Project', 'Help_Project')
            self.checking_is_element_displayed(LandingPageLocators.HELP_PROJECT_DESCRIPTION, 'Description_Help_Project', 'Help_Project')
            return self
    
    def checking_title_stay_connected_is_present_and_displayed(self):
        """ Checking Title_Stay_Connected in Stay_Connected block is present and displayed """

        with allure.step("Checking 'Title_Stay_Connected' in Stay_Connected is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.FOOTER_STAY_CONNECTED_TITLE, 'Title_Stay_Connected', 'FOOTER')
            self.checking_is_element_displayed(LandingPageLocators.FOOTER_STAY_CONNECTED_TITLE, 'Title_Stay_Connected', 'FOOTER')
            return self
    
    def checking_description_stay_connected_is_present_and_displayed(self):
        """ Checking Description in Stay_Connected block is present and displayed """

        with allure.step("Checking description in Stay_Connected is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.FOOTER_DESCRIPTION_STAY_CONNECTED, 'Description_Stay_Connected', 'FOOTER')
            self.checking_is_element_displayed(LandingPageLocators.FOOTER_DESCRIPTION_STAY_CONNECTED, 'Description_Stay_Connected', 'FOOTER')
            return self
    
    def checking_logo_footer_is_present_and_displayed(self):
        """ Checking Logo in FOOTER block is present and displayed """

        with allure.step("Checking Logo in FOOTER is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.FOOTER_LOGO, 'Logo', 'FOOTER')
            self.checking_is_element_displayed(LandingPageLocators.FOOTER_LOGO, 'Logo', 'FOOTER')
            return self
    
    def checking_text_under_logo_footer_is_present_and_displayed(self):
        """ Checking Text_Under_Logo in FOOTER block is present and displayed """

        with allure.step("Checking Text_Under_Logo in FOOTER is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.FOOTER_UNDER_LOGO_TEXT, 'Text_Under_Logo', 'FOOTER')
            self.checking_is_element_displayed(LandingPageLocators.FOOTER_UNDER_LOGO_TEXT, 'Text_Under_Logo', 'FOOTER')
            return self
    
    def checking_mail_address_footer_is_present_and_displayed(self):
        """ Checking Mail_Address in FOOTER block is present and displayed """

        with allure.step("Checking Mail_Address in FOOTER is present and displayed"):
            self.checking_is_element_present(LandingPageLocators.FOOTER_MAIL_ADDRESS, 'Mail_Address', 'FOOTER')
            self.checking_is_element_displayed(LandingPageLocators.FOOTER_MAIL_ADDRESS, 'Mail_Address', 'FOOTER')
            return self