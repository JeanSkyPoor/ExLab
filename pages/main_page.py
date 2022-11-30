from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    def check_background_color(self, theme_type:str) -> None:
        """Checking background color

        theme_type: there are two options: 'dark' and 'white'. 
        """
        with allure.step("Checking background color..."):            
            color = self.get_background_color()
            if theme_type == 'dark':
                assert color == '#111111', f"Theme's color is not black, have to be #111111, but have {color}"
            if theme_type == 'white':
                assert color == '#ffffff', f"Theme's color is not white, have to be #ffffff, but have {color}"


    def check_item_src(self, correct_src: str, item_locator: tuple) -> None:
        """Matching correct_src and current src from element by 'webelement.get_attribute(src)

        correct_src: str like 'http://test.exlab.team/gif/logo.gif'
        item_locator: tuple like (By.CSS_SECELTOR, 'random selector'). Not unzipped 
        '"""
        with allure.step("Checking src from item..."):
            item_src = self.browser.find_element(*item_locator).get_attribute('src')
            assert item_src == correct_src, f"SRC is not correct. Have to be {correct_src}, but have {item_src}"


    def check_element_is_present(self, button_name: str, button_locator: tuple) -> None:
        """
        Checking if an element exists on the page

        button_name: how you wanna see button's name on report and assert error
        button_locator: tuple like (By.CSS_SECELTOR, 'random selector'). Not unzipped 
        """
        with allure.step(f"Checking {button_name} on page..."):
            assert self.is_element_present(*button_locator), f"{button_name} is not founded"

    
    def check_anchor_element_after_shifting(self, anchor_element_name: str, anchor_locator: tuple) -> None:
        """
        Checking anchor element after shifting

        anchor_element_name: how you wanna see anchor's name on report and assert error
        anchor_locator: tuple like (By.CSS_SECELTOR, 'random selector'). Not unzipped 
        """
        with allure.step(f"Checking {anchor_element_name} after shifting..."):
            assert self.checking_visibility_of_element_located(*anchor_locator), f"{anchor_element_name} anchor is not founded after shifting"
            

    def check_join_opened_correct_url(self, currect_url: str) -> None:
        """Switch to the last window handless and check current URL and currect URL"""
        with allure.step(f"Checking url, have to be... {currect_url}"):
            self.browser.switch_to.window(self.browser.window_handles[-1])
            assert self.checking_url_to_be(currect_url), f'URL is not correct. Have to be {currect_url}, but {self.browser.current_url}'