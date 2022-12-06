from selenium.common.exceptions import NoSuchElementException
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.color import Color
from pages.locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType
import requests
import time


class BasePage():    
    def __init__(self, browser, link) -> None:
        """Creating BasePage class\n
        
        Args:
         - browser: fixture or browser driver
         - link: URL address 
        """
        self.browser = browser
        self.link = link


    def open(self) -> None:
        """Open Page using added browser and link using self.browser and self.link"""
        with allure.step("Opening page"):
            self.browser.get(self.link)


    def attach_screenshot(self, file_name: str) -> None:
        """Create screenshot of current window and attach it in allure report
        
        Args:
         - file_name: str like 'Linkedin_button_not_found'
        """
        allure.attach(self.browser.get_screenshot_as_png(), name = file_name, attachment_type=AttachmentType.PNG)


    def is_element_present(self, locator: tuple) -> bool:
        """Сhecking for the presence of an element on the page. doesn't mean element is visible on screen \n

        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
        """ 
        with allure.step(f"Checking if element is present with {locator}"):
            try:
                self.browser.find_element(*locator)
            except NoSuchElementException:
                return False
            return True

    
    def is_element_displayed(self, locator: tuple) -> bool:
        """Checking for element is displayed on screen. Have to use after self.is_element_present
        
        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
        """
        with allure.step(f"Checking if element is displayed with {locator}"):
            return self.browser.find_element(*locator).is_displayed()


    def get_text_from_element(self, locator: tuple) -> str:
        """Getting text from element and return it\n
        
        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
        """
        with allure.step(f"Getting text from {locator} element"):
            return self.browser.find_element(*locator).text


    def matching_element_text_with_correct_text(self, locator: tuple, correct_text: str) -> None:
        """Matching text from element and correct text\n
        
        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
         - correct_text: str value
        """
        with allure.step("Matching element text and correct text"):
            element_text = self.get_text_from_element(locator)
            if element_text != correct_text:
                raise AssertionError(f"Text is wrong. Have to be {correct_text}, but have {element_text}")


    def get_attribute_value(self, locator: tuple, attribute_name: str) -> str:
        """Getting specified attribute value from element and return it\n
        
        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
         - attribute_name: attribute's name what we want to get like 'src'
        """
        with allure.step(f"Getting {attribute_name} attribute from {locator} element"):
            return self.browser.find_element(*locator).get_attribute(attribute_name)
            

    def matching_attribute_value_with_correct_value(self, locator: tuple, attribute_name: str, correct_value: str) -> None:
        """Matching attribute value and correct attribute value\n
        
        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
         - attribute_name: str attribute's name what we want to get like 'src'
         - correct_value: str value
        """
        with allure.step("Matching attribute value and correct value"):
            attribute_value = self.get_attribute_value(locator, attribute_name)
            if attribute_value != correct_value:
                raise AssertionError(f"Wrong attribute value. Have to be {correct_value}, but have {attribute_value}")


    def get_current_url(self) -> str:
        """Getting current URL"""
        with allure.step("Getting current URL"):
            return self.browser.current_url


    def matching_current_and_correct_urls(self, correct_url: str) -> None:
        """Matching current URL and correct URL letter to letter\n
        
        Args:
         - correct_url: str like 'https://www.google.ru/'
        """
        with allure.step("Matching current URL and correct URL"):
            current_url = self.get_current_url()            
            if current_url != correct_url:
                raise AssertionError(f"URL is wrong. Have to be {correct_url}, but have {current_url}")


    def click_on_element(self, locator) -> None:
        """Click on element using locator\n

        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
        """
        with allure.step(f"Cliking on {locator}"):
           self.browser.find_element(*locator).click() 


    def checking_visibility_of_element_located(self, locator: tuple, timeout=5, checking_time=2) -> bool:
        """Wait while element will be visible and return True. If element is not vilible, return False
        
        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
         - timeout: int. How long wait while element will be visible
         - checking_time: int or float. How offen create visibility request 
        """

        try:
            WebDriverWait(self.browser, timeout, checking_time).until(EC.visibility_of_element_located((locator)))
        except TimeoutException:
            return False
        return True


    def checking_anchor_element_after_shifting(self, anchor_element_name: str, anchor_locator: tuple) -> None:
        """Checking anchor element after shifting\n

        Args:
         - anchor_element_name: how you wanna see anchor's name on report and assert error
         - anchor_locator: tuple like (By.CSS_SELECTOR, '#about')
        """

        with allure.step(f"Checking {anchor_element_name} anchor after shifting"):
            if self.checking_visibility_of_element_located(anchor_locator) != True:
                self.attach_screenshot(f"{anchor_element_name} anchor_is_not_founded_after_shifting")
                raise AssertionError(f"{anchor_element_name} anchor is not founded after shifting")


    def switch_to_the_last_opened_window(self) -> None:
        """Switch accent to the last opened window"""
        self.browser.switch_to.window(self.browser.window_handles[-1])


    def scroll_down_element_to_element(self, list_of_element: list) -> None:
        """Лютый костыль. В цикле скролит по элементам
        
        Args:
         - list_of_element: list with elements from find_elements
        """
        for element in list_of_element:
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(0.5)


    def is_url_contain(self, fragment_url: str, timeout=5) -> bool:
        """Wait while current url will be contrain fragment_url in address
        
        Args:
         - fragment_url: str like 'https://www.m-translate.ru'
        """
        try:
            WebDriverWait(self.browser, timeout, 1).until(EC.url_contains(fragment_url))
        except TimeoutException:
            return False
        return True


    def url_have_to_contain(self, fragment_url: str) -> None:
        """Checking if current url will contain fragment_url 
        
        Args:
         - fragment_url: str like 'https://www.m-translate.ru'
        """
        if self.is_url_contain(fragment_url) != True:
            raise AssertionError(f"URL is wrong. Have to contain {fragment_url} in address, but have {self.get_current_url()}")

















































    # def get_element_attribute(self, element_locator: tuple, attribute_element=None):
    #     """Get element's attribute and return it"""

    #     return self.browser.find_element(*element_locator).get_attribute(attribute_element)


    # def get_element_attribute(self, locator: tuple, attribute: str):
    #     """Get attribute from item

    #     locator: tuple like (By.CSS_SELECTOR, 'random selector'). Not unzipped \n
    #     attribute: str like 'src'
    #     """
    #     with allure.step(f"Getting {attribute} from {locator} item..."):
    #         return self.browser.find_element(*locator).get_attribute(attribute)

    
    # def get_element_text(self, locator: tuple) -> str:
    #     """Get text from item
        
    #     locator: tuple like (By.CSS_SELECTOR, 'random selector'). Not unzipped
    #     """
    #     with allure.step(f"Getting text from {locator} item..."):
    #         try:                
    #             return self.browser.find_element(*locator).text
    #         except:
    #             return None


    # def is_element_present(self, how, what) -> bool:
    #     """Сhecking for the presence of an element on the page""" 

    #     with allure.step("Checking present of element"):
    #         try:
    #             self.browser.find_element(how, what)
    #         except NoSuchElementException:
    #             return False
    #         return True


    # def match_current_url(self, correct_link: str):
    #     """Matching current URL with correct URL
        
    #     correct_link like  'https://www.google.ru/'
    #     """
    #     with allure.step(f"Checking URL link... Have to be {correct_link}"):
    #         assert self.browser.current_url == correct_link, f"URL is not correct, have to be {correct_link}, but is {self.browser.current_url}"


    # def get_background_color(self) -> str:
    #     try:
    #         background_color = self.browser.find_element(*MainPageLocators.BACKGROUND_FOR_THEME).value_of_css_property('background-color')
    #         color = Color.from_string(background_color).hex
    #         return color
    #     except NoSuchElementException:
    #         return 'Cannot get background color'


    # def click_on_button(self, how, what) -> None:
    #     with allure.step(f"Clicking on button...{how} {what}"):
    #         self.browser.find_element(how, what).click()


    # def checking_visibility_of_element_located(self, how, what, timeout=4) -> None:
    #     try:
    #         WebDriverWait(self.browser, timeout, 1).until(EC.visibility_of_element_located((how, what)))
    #     except TimeoutException:
    #         return False
    #     return True


    # def checking_url_to_be(self, correct_url: str, timeout=4) ->bool:
    #     try:
    #         WebDriverWait(self.browser, timeout, 1).until(EC.url_to_be(correct_url))
    #     except TimeoutException:
    #         return False
    #     return True
        

    # def scroll_down_to_element(self, locator: tuple):
    #     """Scroll down to element with locator
        
    #     locator: tuple like (By.CSS_SELECTOR, 'random selector'). Not unzipped
    #     """
    #     with allure.step(f"Searching element with {locator} and scroll to him..."):
    #         element = self.browser.find_element(*locator)
    #         self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
