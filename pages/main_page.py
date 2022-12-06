from pages.locators import MainPageLocators
from pages.base_page import BasePage
import allure
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class MainPage(BasePage):

    def checking_landing_url(self,):
        """Checking that landing URL is correct"""
        self.matching_current_and_correct_urls('http://test.exlab.team/')


    def checking_dark_mode_on(self):
        """Checking if dark mode on"""
        self.matching_attribute_value_with_correct_value(MainPageLocators.THEME, 'class', 'sc-bczRLJ ckyTig')

    def checking_light_mode_on(self):
        """Checking if light mode on"""
        self.matching_attribute_value_with_correct_value(MainPageLocators.THEME, 'class', 'sc-bczRLJ cxdoLY')


    def checking_about_us_header_is_present_and_displayed(self):
        """Checking 'About Us' button in HEADER is present and displayed"""
        if self.is_element_present(MainPageLocators.ABOUT_US_HEADER_BUTTON) != True:
            self.attach_screenshot('About_Us_button_in_HEADER_is_not_found')
            raise AssertionError("About Us button in HEADER is not found")

        if self.is_element_displayed(MainPageLocators.ABOUT_US_HEADER_BUTTON) != True:
            self.attach_screenshot('About_Us_button_in_HEADER_is_not_displayed')
            raise AssertionError("About Us button in HEADER is not displayed")    

    def click_on_about_us_header(self):
        """Click on 'About Us' button in HEADER"""
        self.click_on_element(MainPageLocators.ABOUT_US_HEADER_BUTTON)


    def checking_projects_header_is_present_and_displayed(self):
        """Checking Project button in HEADER is present and displayed"""
        if self.is_element_present(MainPageLocators.PROJECTS_HEADER_BUTTON) != True:
            self.attach_screenshot('Projects_button_in_HEADER_is_not_found')
            raise AssertionError("Projects button in HEADER is not found")

        if self.is_element_displayed(MainPageLocators.PROJECTS_HEADER_BUTTON) != True:
            self.attach_screenshot('Project_button_in_HEADER_is_not_displayed')
            raise AssertionError("Projects button in HEADER is not displayed")

    def click_on_projects_header(self):
        """Click on 'Projects' button in HEADER"""
        self.click_on_element(MainPageLocators.PROJECTS_HEADER_BUTTON)


    def checking_mentors_header_is_present_and_displayed(self):
        """Checking 'Mentors' button in HEADER is present and displayed"""
        if self.is_element_present(MainPageLocators.MENTORS_HEADER_BUTTON) != True:
            self.attach_screenshot('Mentors_button_in_HEADER_is_not_found')
            raise AssertionError("Mentors button in HEADER is not found")

        if self.is_element_displayed(MainPageLocators.MENTORS_HEADER_BUTTON) != True:
            self.attach_screenshot('Mentors_button_in_HEADER_is_not_displayed')
            raise AssertionError("Mentors button in HEADER is not displayed")

    def click_on_mentors_header(self):
        """Click on 'Mentors' button in HEADER"""
        self.click_on_element(MainPageLocators.MENTORS_HEADER_BUTTON)


    def checking_startup_for_header_is_present_and_displayed(self):
        """Checking 'StartUp for' button in HEADER is present and displayed"""
        if self.is_element_present(MainPageLocators.STARTUP_FOR_HEADER_BUTTON) != True:
            self.attach_screenshot('Startup_for_button_in_HEADER_is_not_found')
            raise AssertionError("StartUp for button in HEADER is not found")

        if self.is_element_displayed(MainPageLocators.STARTUP_FOR_HEADER_BUTTON) != True:
            self.attach_screenshot('Startup_for_button_in_HEADER_is_not_displayed')
            raise AssertionError("StartUp for button in HEADER is not displayed")

    def click_on_startup_for_header(self):
        """Click on 'StartUp for' button in HEADER"""
        self.click_on_element(MainPageLocators.STARTUP_FOR_HEADER_BUTTON)

 
    def checking_sun_icon_header_is_present_and_displayed(self):
        """Checking 'Sun icon' button in HEADER is present and displayed"""
        if self.is_element_present(MainPageLocators.SUN_ICON_HEADER_BUTTON) != True:
            self.attach_screenshot('Sun_icon_in_HEADER_is_not_found')
            raise AssertionError("Sun icon button in HEADER is not found")

        if self.is_element_displayed(MainPageLocators.SUN_ICON_HEADER_BUTTON) != True:
            self.attach_screenshot('Sun_icon_button_in_HEADER_is_not_displayed')
            raise AssertionError("Sun icon button in HEADER is not displayed")

    def click_on_sun_icon_header(self):
        """Click on 'Sun icon' button in HEADER"""
        self.click_on_element(MainPageLocators.SUN_ICON_HEADER_BUTTON)


    def checking_join_header_is_present_and_displayed(self):
        """Checking 'Join' button in HEADER is present and displayed"""
        if self.is_element_present(MainPageLocators.JOIN_HEADER_BUTTON) != True:
            self.attach_screenshot('Join_button_in_HEADER_is_not_found')
            raise AssertionError("Join button in HEADER is not found")

        if self.is_element_displayed(MainPageLocators.JOIN_HEADER_BUTTON) != True:
            self.attach_screenshot('Join_button_in_HEADER_is_not_displayed')
            raise AssertionError("Join button in HEADER is not displayed")

    def click_on_join_header(self):
        """Click on 'Join' button in HEADER"""
        self.click_on_element(MainPageLocators.JOIN_HEADER_BUTTON)

    def checking_url_after_click_on_join_header(self):
        """Switch to the last opened window and check URL"""
        with allure.step(f"Checking url opened page"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://t.me')


    def checking_logo_in_your_opportunity_block_is_present_and_displayed(self):
        """Checking Logo in block YOUR OPPORTUNITY is present and displayed"""
        if self.is_element_present(MainPageLocators.LOGO_YOUR_OPPORTUNITY) != True:
            self.attach_screenshot('Logo_in_your_opportunity_block_is_not_found')
            raise AssertionError("Logo in block YOUR OPPORTUNITY is not found")

        if self.is_element_displayed(MainPageLocators.LOGO_YOUR_OPPORTUNITY) != True:
            self.attach_screenshot('Logo_in_your_opportunity_block_is_not_displayed')
            raise AssertionError("Logo in block YOUR OPPORTUNITY is not displayed")

    def checking_main_title_in_your_opportunity_block_is_present_and_displayed(self):
        """Checking main title in your opportynity block is present and displayed"""
        if self.is_element_present(MainPageLocators.MAIN_TITLE_YOUR_OPPROTUNITY) != True:
            self.attach_screenshot('Main_title_in_your_opportunity_block_is_not_found')
            raise AssertionError("Main title in block YOUR OPPORTUNITY is not found")

        if self.is_element_displayed(MainPageLocators.MAIN_TITLE_YOUR_OPPROTUNITY) != True:
            self.attach_screenshot('Main_title_in_your_opportunity_block_is_not_displayed')
            raise AssertionError("Main title in block YOUR OPPORTUNITY is not displayed")

    def checking_text_under_main_title_in_your_opportunity_block_is_present_and_displayed(self):
        """Checking text under main title in your opportunity block is present and displayed"""
        if self.is_element_present(MainPageLocators.BLOCK_TEXT_YOUR_OPPORTUNITY) != True:
            self.attach_screenshot('Text_under_Main_title_in_your_opportunity_block_is_not_found')
            raise AssertionError("Text under Main title in block YOUR OPPORTUNITY is not found")

        if self.is_element_displayed(MainPageLocators.BLOCK_TEXT_YOUR_OPPORTUNITY) != True:
            self.attach_screenshot('Text_under_Main_title_in_your_opportunity_block_is_not_displayed')
            raise AssertionError("Text under Main title in block YOUR OPPORTUNITY is not displayed")


    def checking_about_us_anchor_after_shifting(self):
        """Checking anchor element in 'About Us' block"""
        self.checking_anchor_element_after_shifting('About Us', MainPageLocators.ABOUT_US_ANCHOR)

    def checking_why_exlab_anchor_after_shifting(self):
        """Checking anchor element in 'Why Exlab' block"""
        self.checking_anchor_element_after_shifting('Why Exlab', MainPageLocators.WHY_EXLAB_BLOCK)

    def checking_projects_anchor_after_shifting(self):
        """Checking anchor element in 'Projects' block"""
        self.checking_anchor_element_after_shifting('Project', MainPageLocators.PROJECTS_ANCHOR)

    def checking_mentors_anchor_after_shifting(self):
        """Checking anchor element in 'Mentors' block"""
        self.checking_anchor_element_after_shifting('Mentors', MainPageLocators.MENTORS_ANCHOR)

    def checking_startup_for_anchor_after_shifting(self):
        """Checking anchor element in 'StartUp for' block"""
        self.checking_anchor_element_after_shifting('StartUp for', MainPageLocators.STARTUP_FOR_ANCHOR)

    def checking_help_project_anchor_after_shifting(self):
        """Checking anchor element in 'Help project' block"""
        self.checking_anchor_element_after_shifting('Help Project', MainPageLocators.HELP_PROJECT_ANCHOR)

    def checking_footer_anchor_after_shifting(self):
        """Checking anchor element in 'Footer' block"""
        self.checking_anchor_element_after_shifting('Footer', MainPageLocators.FOOTER_ANCHOR)


    def scroll_to_about_us(self):
        """Scroll from top to 'About us' block and check anchor element"""
        elements = self.browser.find_elements(*MainPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:2])
        self.checking_about_us_anchor_after_shifting()

    def scroll_to_why_exlab(self):
        """Scroll from top to 'Why Exlab' block and check anchor element"""
        elements = self.browser.find_elements(*MainPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:2]) 
        self.scroll_down_element_to_element([self.browser.find_element(*MainPageLocators.WHY_EXLAB_BLOCK)]) #Костыль!
        self.checking_why_exlab_anchor_after_shifting()

    def scroll_to_project(self):
        """Scroll from top to 'Project' block and check anchor element"""
        elements = self.browser.find_elements(*MainPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:3])
        self.checking_projects_anchor_after_shifting()

    def scroll_to_mentors(self):
        """Scroll from top to 'Mentors' block and check anchor element"""
        elements = self.browser.find_elements(*MainPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:4])
        self.checking_mentors_anchor_after_shifting()

    def scroll_to_startup_for(self):
        """Scroll from top to 'StartUp for' block and check anchor element"""
        elements = self.browser.find_elements(*MainPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:5])
        self.checking_startup_for_anchor_after_shifting()

    def scroll_to_help_project(self):
        """Scroll from top to 'Help project' block and check anchor element"""
        elements = self.browser.find_elements(*MainPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:6])
        self.checking_help_project_anchor_after_shifting()
     
    def scroll_to_footer(self):
        """Scroll from top to 'Footer' block and check anchor element"""
        elements = self.browser.find_elements(*MainPageLocators.SELECTOR_FOR_SCROLL)
        self.scroll_down_element_to_element(elements[:7])
        self.checking_footer_anchor_after_shifting()


    def checking_linkedin_footer_is_present_and_displayed(self):
        """Checking 'Linkedin' button in FOOTER is present and displayed"""
        if self.is_element_present(MainPageLocators.LINKEDIN_FOOTER) != True:
            self.attach_screenshot('Linkedin_button_in_FOOTER_block_is_not_found')
            raise AssertionError('Linkedin button in FOOTER block is not found')

        if self.is_element_displayed(MainPageLocators.LINKEDIN_FOOTER) != True:
            self.attach_screenshot('Linkedin_button_in_FOOTER_block_is_not_displayed')
            raise AssertionError('Linkedin button in FOOTER block is not displayed')

    def click_on_linkedin_footer(self):
        """Click on 'Linkedin' button in FOOTER"""
        self.click_on_element(MainPageLocators.LINKEDIN_FOOTER)

    def checking_url_after_click_on_linkedin_footer(self):
        """Switch to the last opened window and check URL"""
        with allure.step(f"Checking url opened page"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://www.linkedin.com')


    def checking_instagram_footer_is_present_and_displayed(self):
        """Checking 'Instagram' button in FOOTER is present and displayed"""
        if self.is_element_present(MainPageLocators.INSTAGRAM_FOOTER) != True:
            self.attach_screenshot('Instagram_button_in_FOOTER_block_is_not_found')
            raise AssertionError('Instagram button in FOOTER block is not found')

        if self.is_element_displayed(MainPageLocators.INSTAGRAM_FOOTER) != True:
            self.attach_screenshot('Instagram_button_in_FOOTER_block_is_not_displayed')
            raise AssertionError('Instagram button in FOOTER block is not displayed')

    def click_on_instagram_footer(self):
        """Click on 'Instagram' button in FOOTER"""
        self.click_on_element(MainPageLocators.INSTAGRAM_FOOTER)

    def checking_url_after_click_on_instagram_footer(self):
        """Switch to the last opened window and check URL"""
        with allure.step(f"Checking url opened page"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://www.instagram.com')


    def checking_telegram_footer_is_present_and_displayed(self):
        """Checking 'Telegram' button in FOOTER is present and displayed"""
        if self.is_element_present(MainPageLocators.TELEGRAM_FOOTER) != True:
            self.attach_screenshot('Telegram_button_in_FOOTER_block_is_not_found')
            raise AssertionError('Telegram button in FOOTER block is not found')

        if self.is_element_displayed(MainPageLocators.TELEGRAM_FOOTER) != True:
            self.attach_screenshot('Telegram_button_in_FOOTER_block_is_not_displayed')
            raise AssertionError('Telegram button in FOOTER block is not displayed')

    def click_on_telegram_footer(self):
        """Click on 'Telegram' button in FOOTER"""
        self.click_on_element(MainPageLocators.TELEGRAM_FOOTER)

    def checking_url_after_click_on_telegram_footer(self):
        """Switch to the last opened window and check URL"""
        with allure.step(f"Checking url opened page"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://t.me')


    def checking_youtube_footer_is_present_and_displayed(self):
        """Checking 'Youtube' button in FOOTER is present and displayed"""
        if self.is_element_present(MainPageLocators.YOUTUBE_FOOTER) != True:
            self.attach_screenshot('Youtube_button_in_FOOTER_block_is_not_found')
            raise AssertionError('Youtube button in FOOTER block is not found')

        if self.is_element_displayed(MainPageLocators.YOUTUBE_FOOTER) != True:
            self.attach_screenshot('Youtube_button_in_FOOTER_block_is_not_displayed')
            raise AssertionError('Youtube button in FOOTER block is not displayed')

    def click_on_youtube_footer(self):
        """Click on 'Youtube' button in FOOTER"""
        self.click_on_element(MainPageLocators.YOUTUBE_FOOTER)

    def checking_url_after_click_on_youtube_footer(self):
        """Switch to the last opened window and check URL"""
        with allure.step(f"Checking url opened page"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://www.youtube.com')


    def checking_join_why_exlab_is_present_and_displayed(self):
        """Checking 'Join' button in 'Why Exlab' is present and displayed"""
        if self.is_element_present(MainPageLocators.JOIN_WHY_EXLAB_BLOCK) != True:
            self.attach_screenshot('Join_button_in_Why_Exlab_block_is_not_found')
            raise AssertionError('Join button in Why Exlab block is not found')

        if self.is_element_displayed(MainPageLocators.JOIN_WHY_EXLAB_BLOCK) != True:
            self.attach_screenshot('Join_button_in_Why_Exlab_block_is_not_displayed')
            raise AssertionError('Join button in Why Exlab block is not displayed')

    def click_on_join_why_exlab(self):
        """Click on 'Join' button in Why Exlab"""
        self.click_on_element(MainPageLocators.JOIN_WHY_EXLAB_BLOCK)

    def checking_url_after_click_on_join_why_exlab(self):
        """Switch to the last opened window and check URL"""
        with allure.step(f"Checking url opened page"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://t.me')


    def check_all_mentors_spoilers(self):
        """One by one checking mentor's spoilers in mentors block"""
        try:
            spoilers = self.browser.find_elements(*MainPageLocators.MENTORS_ALL_SPOILERS_BLOCK)
        except NoSuchElementException:
            raise NoSuchElementException("Mentor's spoilers is not found")
            
        for index, spoiler in enumerate(spoilers):
            with allure.step(f"Checking {index+1} spoiler of mentors"):
                locator = (By.CSS_SELECTOR, f'div:nth-child({index+1}) > div.sc-bUbCnL.gFhhBm') #локатор закрытого спойлера

                spoiler.click()

                if self.checking_visibility_of_element_located(MainPageLocators.MENTORS_BLOCK_WITH_DATA_OPENED_SPOILER, checking_time=0.5) != True: 
                    self.attach_screenshot('Block_with_data_of_mentor_is_not_displayed')           
                    raise AssertionError(f"Block with data of mentor is not displayed. {index+1} spoiler")

                if self.checking_visibility_of_element_located(MainPageLocators.MENTOR_IMAGE, checking_time=0.5) != True:
                    self.attach_screenshot('Image_of_mentor_is_not_displayed') 
                    raise AssertionError(f"Image of mentor is not displayed. {index+1} spoiler")    

                if self.checking_visibility_of_element_located(MainPageLocators.MENTOR_DESCRIPTION, checking_time=0.5) != True:
                    self.attach_screenshot('Description_info_of_mentor_is_not_displayed') 
                    raise AssertionError(f"Description info of mentor is not displayed. {index+1} spoiler")

                spoiler.click()

                if self.is_element_present(locator) != True: #При закрытом спойлере появляется объект с локатором locator, если спойлер не закрыть, объекта не будет и тест упадет
                    self.attach_screenshot('Spoiler_is_not_closed') 
                    raise AssertionError(f"Spoiler is not closed {index+1} spoiler")

    
    def checking_boosty_help_project_button_is_present_and_displayed(self):
        """Checking 'Boosty' button in Help Project block is present and displayed"""
        if self.is_element_present(MainPageLocators.BOOSTY_HELP_PROJECT_BUTTON) != True:
            self.attach_screenshot('Boosty_button_is_not_present')
            raise AssertionError('Boosty button in help project block is not present')

        if self.is_element_displayed(MainPageLocators.BOOSTY_HELP_PROJECT_BUTTON) != True:
            self.attach_screenshot('Boosty button is not displayed')
            raise AssertionError('Boosty button in help project block is not displayed')
                
    def click_on_boosty_help_project(self):
        """Click on 'Boosty' button in Help Project block"""
        self.click_on_element(MainPageLocators.BOOSTY_HELP_PROJECT_BUTTON)
            
    def checking_url_after_click_on_boosty_help_project(self):
        """Switch to the last opened window and check URL"""
        with allure.step(f"Checking url opened page"):
            self.switch_to_the_last_opened_window()
            self.url_have_to_contain('https://boosty.to')