from pages.locators import MainPageLocators
from pages.base_page import BasePage
import allure
import re




class MainPage(BasePage):

    def checking_landing_url(self,):
        """Checking that landing URL is correct"""
        self.matching_current_and_correct_urls('https://exlab.team/')


    def checking_dark_mode_on(self):
        """Checking if dark mode on"""
        self.matching_attribute_value_with_correct_value(MainPageLocators.THEME, 'class', 'sc-bczRLJ ckyTig')
    
    def checking_light_mode_on(self):
        """Checking if light mode on"""
        self.matching_attribute_value_with_correct_value(MainPageLocators.THEME, 'class', 'sc-bczRLJ cxdoLY')


    def checking_about_us_header_is_present_and_displayed(self):
        """Checking 'About Us' button in HEADER is present and displayed"""
        assert self.is_element_present(MainPageLocators.ABOUT_US_HEADER_BUTTON), "About Us button in HEADER is not found"
        assert self.is_element_displayed(MainPageLocators.ABOUT_US_HEADER_BUTTON), "About Us button in HEADER is not displayed"    

    def click_on_about_us_header(self):
        """Click on 'About Us' button in HEADER"""
        self.click_on_element(MainPageLocators.ABOUT_US_HEADER_BUTTON)

    def checking_about_us_anchor_after_shifting(self):
        """Checking anchor element after 'About Us' button in HEADER was clicked"""
        self.checking_anchor_element_after_shifting('About Us', MainPageLocators.ABOUT_US_ANCHOR)


    def checking_projects_header_is_present_and_displayed(self):
        """Checking Project button in HEADER is present and displayed"""
        assert self.is_element_present(MainPageLocators.PROJECTS_HEADER_BUTTON), "Projects button in HEADER is not found"
        assert self.is_element_displayed(MainPageLocators.PROJECTS_HEADER_BUTTON), "Projects button in HEADER is not displayed"

    def click_on_projects_header(self):
        """Click on 'Projects' button in HEADER"""
        self.click_on_element(MainPageLocators.PROJECTS_HEADER_BUTTON)

    def checking_projects_anchor_after_shifting(self):
        """Checking anchor element after 'Project' button in HEADER was clicked"""
        self.checking_anchor_element_after_shifting('Project', MainPageLocators.PROJECTS_ANCHOR)


    def checking_mentors_header_is_present_and_displayed(self):
        """Checking 'Mentors' button in HEADER is present and displayed"""
        assert self.is_element_present(MainPageLocators.MENTORS_HEADER_BUTTON), "Mentors button in HEADER is not found"
        assert self.is_element_displayed(MainPageLocators.MENTORS_HEADER_BUTTON), "Mentors button in HEADER is not displayed"        

    def click_on_mentors_header(self):
        """Click on 'Mentors' button in HEADER"""
        self.click_on_element(MainPageLocators.MENTORS_HEADER_BUTTON)

    def checking_mentors_anchor_after_shifting(self):
        """Checking anchor element after 'Mentors' button in HEADER was clicked"""
        self.checking_anchor_element_after_shifting('Mentors', MainPageLocators.MENTORS_ANCHOR)


    def checking_startup_for_header_is_present_and_displayed(self):
        """Checking 'StartUp for' button in HEADER is present and displayed"""
        assert self.is_element_present(MainPageLocators.STARTUP_FOR_HEADER_BUTTON), "StartUp for button in HEADER is not found"
        assert self.is_element_displayed(MainPageLocators.STARTUP_FOR_HEADER_BUTTON), "StartUp for button in HEADER is not displayed"

    def click_on_startup_for_header(self):
        """Click on 'StartUp for' button in HEADER"""
        self.click_on_element(MainPageLocators.STARTUP_FOR_HEADER_BUTTON)

    def checking_startup_for_anchor_after_shifting(self):
        """Checking anchor element after 'StartUp for' button in HEADER was clicked"""
        self.checking_anchor_element_after_shifting('StartUp for', MainPageLocators.STARTUP_FOR_ANCHOR)

    
    def checking_sun_icon_header_is_present_and_displayed(self):
        """Checking 'Sun icon' button in HEADER is present and displayed"""
        assert self.is_element_present(MainPageLocators.SUN_ICON_HEADER_BUTTON), "Sun icon button in HEADER is not found"
        assert self.is_element_displayed(MainPageLocators.SUN_ICON_HEADER_BUTTON), "Sun icon button in HEADER is not displayed"

    def click_on_sun_icon_header(self):
        """Click on 'Sun icon' button in HEADER"""
        self.click_on_element(MainPageLocators.SUN_ICON_HEADER_BUTTON)


    def checking_join_header_is_present_and_displayed(self):
        """Checking 'Join' button in HEADER is present and displayed"""
        assert self.is_element_present(MainPageLocators.JOIN_HEADER_BUTTON), "Join button in HEADER is not found"
        assert self.is_element_displayed(MainPageLocators.JOIN_HEADER_BUTTON), "Join button in HEADER is not displayed"

    def click_on_join_header(self):
        """Click on 'Join' button in HEADER"""
        self.click_on_element(MainPageLocators.JOIN_HEADER_BUTTON)

    def checking_url_after_click_on_join_header(self):
        """Switch to the last opened window and check URL"""
        with allure.step(f"Checking url opened page"):
            self.browser.switch_to.window(self.browser.window_handles[-1])
            current_url = self.get_current_url()
            assert self.checking_url_to_be('https://t.me/ExLab_registration_bot'), f"URL is not correct. Have to be 'https://t.me/ExLab_registration_bot',\
                but have {current_url}"

































    # def check_background_color(self, theme_type:str) -> None:
    #     """Checking background color

    #     theme_type: there are two options: 'dark' and 'white'. 
    #     """

    #     with allure.step("Checking background color..."):            
    #         color = self.get_background_color()
    #         if theme_type == 'dark':
    #             assert color == '#111111', f"Theme's color is not black, have to be #111111, but have {color}"
    #         if theme_type == 'white':
    #             assert color == '#ffffff', f"Theme's color is not white, have to be #ffffff, but have {color}"


    # def matching_item_attribute(self, correct_src: str, attribute: str, locator: tuple) -> None:
    #     """Matching correct_src and current src from element by 'webelement.get_attribute(src)

    #     correct_src: str like 'http://test.exlab.team/gif/logo.gif'\n
    #     attribute: str like 'src' \n
    #     locator: tuple like (By.CSS_SELECTOR, 'random selector'). Not unzipped         
    #     '"""

    #     with allure.step(f"Checking item's {attribute} ..."):
    #         srs = self.get_element_attribute(locator, attribute)
    #         assert srs == correct_src, f"SRC is not correct. Have to be {correct_src}, but have {srs}"


    # def matching_text_from_element(self, correct_text: str, locator: tuple):
    #     """Matching correct text and text from 'webelement.text
        
    #     correct_text: str like 'Твоя возможность' \n
    #     locator: tuple like (By.CSS_SELECTOR, 'random selector'). Not unzipped
    #     '"""
    #     with allure.step(f"Matching text from item and correct_text..."):
    #         text = self.get_element_text(locator)
    #         assert text == correct_text, f"text is wrong. Have to be {correct_text}, but have {text}"


    # def check_element_is_present(self, button_name: str, button_locator: tuple) -> None:
    #     """Checking if an element exists on the page

    #     button_name: how you wanna see button's name on report and assert error \n
    #     button_locator: tuple like (By.CSS_SELECTOR, 'random selector'). Not unzipped 
    #     """

    #     with allure.step(f"Checking {button_name} on page..."):
    #         assert self.is_element_present(*button_locator), f"{button_name} is not founded"

    
    # def check_anchor_element_after_shifting(self, anchor_element_name: str, anchor_locator: tuple) -> None:
    #     """Checking anchor element after shifting

    #     anchor_element_name: how you wanna see anchor's name on report and assert error \n
    #     anchor_locator: tuple like (By.CSS_SELECTOR, 'random selector'). Not unzipped 
    #     """

    #     with allure.step(f"Checking {anchor_element_name} after shifting..."):
    #         assert self.checking_visibility_of_element_located(*anchor_locator), f"{anchor_element_name} anchor is not founded after shifting"
            

    # def check_join_opened_correct_url(self, currect_url: str) -> None:
    #     """Switch to the last window handless and check current URL and currect URL"""

    #     with allure.step(f"Checking url, have to be... {currect_url}"):
    #         self.browser.switch_to.window(self.browser.window_handles[-1])
    #         assert self.checking_url_to_be(currect_url), f'URL is not correct. Have to be {currect_url}, but {self.browser.current_url}'

    # def iterator_mathcing_list(self, matching_list: list, text: str):
    #     with allure.step("Start itereting..."):
    #         for item in matching_list:
    #             if item in text:
    #                     continue
    #             else:
    #                     return False
    #         return True
    
    # def checking_if_matching_text_in_element(self, matching_list: list,  locator: tuple):
    #     """Checking if items from matching_list in text by iterator
        
    #     match_list: list like ['ПОЛУЧИТЬ ТОТ САМЫЙ ОПЫТ', 'ПОРАБОТАТЬ В КОМАНДЕ'] \n
    #     locator: tuple like (By.CSS_SELECTOR, 'random selector'). Not unzipped
    #     """
    #     with allure.step("Getting text and check in matching_list"):
    #         text = self.get_element_text(locator)
    #         assert self.iterator_mathcing_list(matching_list, text), f"Text is wrong. Not found one or more elements from {matching_list} in {text}"
            

