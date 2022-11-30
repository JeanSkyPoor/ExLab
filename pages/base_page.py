from selenium.common.exceptions import NoSuchElementException
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.color import Color
from pages.locators import MainPageLocators

class BasePage():    
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link


    def open(self) -> None:
        """Open Page using added browser and link"""

        with allure.step('Open Page...'):
            self.browser.get(self.link)


    def get_element_attribute(self, element_locator: tuple, attribute_element=None):
        """Get element's attribute and return it"""

        return self.browser.find_element(*element_locator).get_attribute(attribute_element)


    def get_element_attribute(self, locator: tuple, attribute: str):
        """Get attribute from item

        locator: tuple like (By.CSS_SECELTOR, 'random selector'). Not unzipped \n
        attribute: str like 'src'
        """
        with allure.step(f"Getting {attribute} from {locator} item..."):
            return self.browser.find_element(*locator).get_attribute(attribute)
    

    def is_element_present(self, how, what) -> bool:
        """Сhecking for the presence of an element on the page""" 

        with allure.step("Checking present of element"):
            try:
                self.browser.find_element(how, what)
            except NoSuchElementException:
                return False
            return True


    def match_current_url(self, correct_link: str):
        """Matching current URL with correct URL
        
        correct_link like  'https://www.google.ru/'
        """
        with allure.step(f"Checking URL link... Have to be {correct_link}"):
            assert self.browser.current_url == correct_link, f"URL is not correct, have to be {correct_link}, but is {self.browser.current_url}"


    def get_background_color(self) -> str:
        try:
            background_color = self.browser.find_element(*MainPageLocators.BACKGROUND_FOR_THEME).value_of_css_property('background-color')
            color = Color.from_string(background_color).hex
            return color
        except NoSuchElementException:
            return 'Cannot get background color'


    def click_on_button(self, how, what) -> None:
        with allure.step(f"Clicking on button...{how} {what}"):
            self.browser.find_element(how, what).click()


    def checking_visibility_of_element_located(self, how, what, timeout=4) -> None:
        try:
            WebDriverWait(self.browser, timeout, 1).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def checking_url_to_be(self,correct_url, timeout=4) ->bool:
        try:
            WebDriverWait(self.browser, timeout, 1).until(EC.url_to_be(correct_url))
        except TimeoutException:
            return False
        return True
