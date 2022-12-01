from selenium.common.exceptions import NoSuchElementException
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.color import Color
from pages.locators import MainPageLocators
from selenium.webdriver.common.keys import Keys


class BasePage():    
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link


    def open(self) -> None:
        """Open Page using added browser and link using self.browser and self.link"""
        with allure.step("Opening page"):
            self.browser.get(self.link)

    
    def is_element_present(self, locator: tuple) -> bool:
        """Сhecking for the presence of an element on the page\n

        locator: tuple like (By.CSS_SELECTOR, '#about')
        """ 
        with allure.step(f"Checking if element is present with {locator}"):
            try:
                self.browser.find_element(*locator)
            except NoSuchElementException:
                return False
            return True


    def get_text_from_element(self, locator: tuple) -> str:
        """Getting text from element and return it\n
        
        locator: tuple like (By.CSS_SELECTOR, '#about')
        """
        with allure.step(f"Getting text from {locator} element"):
            return self.browser.find_element(*locator).text


    def matching_element_text_with_correct_text(self, locator: tuple, correct_text: str) -> None:
        """Matching text from element and correct text\n
        
        locator: tuple like (By.CSS_SELECTOR, '#about')
        correct_text: str value
        """
        with allure.step("Matching element text and correct text"):
            element_text = self.get_text_from_element(locator)
            assert element_text == correct_text, f"Text is wrong. Have to be {correct_text}, but have {element_text}"


    def get_attribute_value(self, locator: tuple, attribute_name: str) -> str:
        """Getting specified attribute value from element and return it\n
        
        locator: tuple like (By.CSS_SELECTOR, '#about')
        attribute_name: attribute's name what we want to get like 'src'
        """
        with allure.step(f"Getting {attribute_name} from {locator} element"):
            return self.browser.find_element(*locator).get_attribute(attribute_name)
            

    def matching_attribute_value_with_correct_value(self, locator: tuple, attribute_name: str, correct_value: str) -> None:
        """Matching attribute value and correct attribute value\n
        
        locator: tuple like (By.CSS_SELECTOR, '#about')
        attribute_name: str attribute's name what we want to get like 'src'
        correct_value: str value
        """
        with allure.step("Matching attribute value and correct value"):
            attribute_value = self.get_attribute_value(locator, attribute_name)
            assert attribute_value == correct_value, f"Wrong attribute value. Have to be {correct_value}, but have {attribute_value}"


    def get_current_url(self) -> str:
        """Getting current URL"""
        with allure.step("Getting current URL"):
            return self.browser.current_url


    def matching_current_and_correct_urls(self, correct_url: str) -> None:
        """Matching current URL and correct URL letter to letter\n
        
        correct_url: str like 'https://www.google.ru/'
        """
        with allure.step("Matching current URL and correct URL"):
            current_url = self.get_current_url()            
            assert current_url == correct_url, f"URL is wrong. Have to be {correct_url}, but have {current_url}"

    def click_on_element(self, locator) -> None:
        """Click on element using locator\n

        locator: tuple like (By.CSS_SELECTOR, '#about')
        """
        with allure.step(f"Cliking on {locator}"):
           self.browser.find_element(*locator).click() 


    def checking_visibility_of_element_located(self, locator: tuple, timeout=4) -> None:
        try:
            WebDriverWait(self.browser, timeout, 1).until(EC.visibility_of_element_located((locator)))
        except TimeoutException:
            return False
        return True


    def checking_anchor_element_after_shifting(self, anchor_element_name: str, anchor_locator: tuple) -> None:
        """Checking anchor element after shifting\n

        anchor_element_name: how you wanna see anchor's name on report and assert error
        anchor_locator: tuple like (By.CSS_SELECTOR, '#about')
        """

        with allure.step(f"Checking {anchor_element_name} after shifting"):
            assert self.checking_visibility_of_element_located(anchor_locator), f"{anchor_element_name} anchor is not founded after shifting"



























































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
