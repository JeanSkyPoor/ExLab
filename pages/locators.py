from selenium.webdriver.common.by import By
import pytest

class MainPageLocators():
    
    LINK = 'http://test.exlab.team/'
    BACKGROUND_FOR_THEME = (By.CSS_SELECTOR, '#root > div')

    #Block HEADERS
    LIGHT_ICON_WHILE_DARK_MODE = (By.CSS_SELECTOR, 'div.sc-fnykZs.fEkGUM')
    LOGO_ICON = (By.CSS_SELECTOR, 'div.sc-gKXOVf >div.sc-jqUVSM.EnPDN')
    ABOUT_US_BUTTON_HEADER = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(1)')
    PROJECTS_BUTTON_HEADER = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(2)')
    MENTORS_BUTTON_HEADER = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(3)')
    STARTUP_FOR_BUTTON_HEADER = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(4)')
    JOIN_BUTTON_HEADER = (By.CSS_SELECTOR, 'div.sc-hAZoDl.hrEelO')
    SUN_ICON = (By.CSS_SELECTOR, 'div.sc-fnykZs.fEkGUM')
    

    ABOUT_US_ANCHOR = (By.CSS_SELECTOR, '#about')
    PROJECT_ANCHOR = (By.CSS_SELECTOR, '#projects')
    MENTORS_ANCHOR = (By.CSS_SELECTOR, '#mentors')
    STARTUP_FOR_ANCHOR = (By.CSS_SELECTOR, '#startup')