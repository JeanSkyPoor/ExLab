from selenium.common.exceptions import NoSuchElementException
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from allure_commons.types import AttachmentType
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
        
        try:
            self.browser.find_element(*locator)
            return True
        except NoSuchElementException:
            return False


    def checking_if_element_is_present(self, locator: tuple, element_name: str, block_name: str) -> None:
        """Checking if element is present. If not, create screenshot of visible window and raise AssertionError
        
        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
         - element_name: str like 'Join' or 'StartUp_for'
         - block_name: str like 'HEADER' or 'YOUR_OPPORTUNITY'

        Raise AssertionError like 'Join in HEADER is not present'
        """
        
        with allure.step(f"Checking if {element_name} is present in {block_name} block"):
            if self.is_element_present(locator) != True:
                self.attach_screenshot(f"{element_name}_in_{block_name}_is_not_present")
                raise AssertionError(f"{element_name} in {block_name} is not present.\n Type of searching: {locator[0]}\n Selector: {locator[1]}")


    def is_element_displayed(self, locator: tuple) -> bool:
        """Checking for element is displayed on screen. Have to use after self.is_element_present
        
        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
        """
        element = self.browser.find_element(*locator)
        return element.is_displayed()


    def checking_if_element_is_displayed(self, locator: tuple, element_name: str, block_name: str) -> None:
        """Checking if element is displayed. If not, create screenshot of visible window and raise AssertionError
        
        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
         - element_name: str like 'Join' or 'StartUp_for'
         - block_name: str like 'HEADER' or 'YOUR_OPPORTUNITY'
        
        Raise AssertionError like 'Join in HEADER is not displayed'
        """
        with allure.step(f"Checking if {element_name} is displayed in {block_name} block"):
            if self.is_element_displayed(locator) != True:
                self.attach_screenshot(f"{element_name}_in_{block_name}_is_not_displayed")
                raise AssertionError(f"{element_name} in {block_name} is not displayed.\n Type of searching: {locator[0]}\n Selector: {locator[1]}")


    def get_value_of_css_property(self, locator: tuple, property: str) -> str:
        """Get property from element and return it
        
        Args:
         - property: str like 'cursor'
        """
        try:
            return self.browser.find_element(*locator).value_of_css_property(property)
        except Exception as e:
            raise NoSuchElementException(f"Propery is not found. ERROR: {e}")


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


    def click_on_element(self, locator: tuple) -> None:
        """Click on element using locator\n

        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
        """

        self.browser.find_element(*locator).click() 


    def checking_visibility_of_element_located(self, locator: tuple, timeout=5, checking_time=2) -> bool:
        """Wait while element will be visible and return True. If element is not visible, return False
        
        Args:
         - locator: tuple like (By.CSS_SELECTOR, '#about')
         - timeout: int. How long wait while element will be visible
         - checking_time: int or float. How often create visibility request 
        """

        try:
            WebDriverWait(self.browser, timeout, checking_time).until(EC.visibility_of_element_located((locator)))
            return True
        except TimeoutException:
            return False


    def checking_anchor_element_after_shifting(self, anchor_locator: tuple, anchor_element_name: str) -> None:
        """Checking anchor element after shifting\n

        Args:
         - anchor_locator: tuple like (By.CSS_SELECTOR, '#about')
         - anchor_element_name: str like 'Join' or 'StartUp_for'
        
        Raise AssertionError like 'About_us anchor is not founded after shifting'
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
            return True
        except TimeoutException:
            return False


    def url_have_to_contain(self, fragment_url: str) -> None:
        """Checking if current url will contain fragment_url 
        
        Args:
         - fragment_url: str like 'https://www.m-translate.ru'
        """
        with allure.step("Checking if current URL contain framgent_url"):
            if self.is_url_contain(fragment_url) != True:
                raise AssertionError(f"URL is wrong. Have to contain {fragment_url} in address, but have {self.get_current_url()}")
                