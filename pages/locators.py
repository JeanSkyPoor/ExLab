from selenium.webdriver.common.by import By

class MainPageLocators():
    
    LINK = 'http://test.exlab.team/'
    THEME = (By.CSS_SELECTOR, 'div.sc-bczRLJ')
    SELECTOR_FOR_SCROLL = (By.CSS_SELECTOR, 'div.sc-fEOsli.iema-Dv') #находит элементы для прыжков-скролов

    #Block HEADER
    EXLAB_LOGO_HEADER = (By.CSS_SELECTOR, 'div.sc-gKXOVf.hXUcbs > [id=logo_mobile]')
    ABOUT_US_HEADER_BUTTON = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(1)')
    PROJECTS_HEADER_BUTTON = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(2)')
    MENTORS_HEADER_BUTTON = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(3)')
    STARTUP_FOR_HEADER_BUTTON = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(4)') 
    SUN_ICON_HEADER_BUTTON = (By.CSS_SELECTOR, 'div.sc-fnykZs.fEkGUM')
    JOIN_HEADER_BUTTON = (By.CSS_SELECTOR, 'div.sc-hAZoDl.hrEelO')

    #Anchor to blocks
    ABOUT_US_ANCHOR = (By.CSS_SELECTOR, '[id=about]')
    PROJECTS_ANCHOR = (By.CSS_SELECTOR, '[id=projects]')
    MENTORS_ANCHOR = (By.CSS_SELECTOR, '[id=mentors]')
    STARTUP_FOR_ANCHOR = (By.CSS_SELECTOR, '[id=startup]')
    HELP_PROJECT_ANCHOR = (By.CSS_SELECTOR, 'div.sc-jTYCaT.coDMnK')
    FOOTER_ANCHOR = (By.CSS_SELECTOR, '[id=footer]')

    #Block YOUR OPPORTUNITY 
    LOGO_YOUR_OPPORTUNITY = (By.CSS_SELECTOR, 'div.sc-dIouRR.gWQVjR > img')
    MAIN_TITLE_YOUR_OPPROTUNITY = (By.CSS_SELECTOR, 'div.sc-dmRaPn.ljhwJa')
    BLOCK_TEXT_YOUR_OPPORTUNITY = (By.CSS_SELECTOR, 'div.sc-kgflAQ.gUFAgN')




    # BACKGROUND_FOR_THEME = (By.CSS_SELECTOR, '#root > div')

    
    # LIGHT_ICON_WHILE_DARK_MODE = (By.CSS_SELECTOR, 'div.sc-fnykZs.fEkGUM')
    # LOGO_ICON = (By.CSS_SELECTOR, 'div.sc-gKXOVf >div.sc-jqUVSM.EnPDN')
    # ABOUT_US_BUTTON_HEADER = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(1)')
    # PROJECTS_BUTTON_HEADER = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(2)')
    # MENTORS_BUTTON_HEADER = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(3)')
    # STARTUP_FOR_BUTTON_HEADER = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(4)')
    # JOIN_BUTTON_HEADER = (By.CSS_SELECTOR, 'div.sc-hAZoDl.hrEelO')
    # SUN_ICON = (By.CSS_SELECTOR, 'div.sc-fnykZs.fEkGUM')
    
        

   # #Block YOUR OPPORTUNITY
    # LOGO_GIF = (By.CSS_SELECTOR, 'div.sc-idiyUo.jKIKBm > img')
    # YOUR_OPPORTUNITY = (By.CSS_SELECTOR, 'div.sc-kgflAQ.gupdxc')
    # TEXT_UNDER_YOUR_OPPORTUNITY = (By.CSS_SELECTOR, 'div.sc-bBrHrO.lmeoyY')

    # #Block ABOUT US
    # ABOUT_US_MAIN = (By.CSS_SELECTOR, '#about > div.sc-eCYdqJ.koNCEH.is-inview')
    # ABOUT_US_BLOCK_TEXT = (By.CSS_SELECTOR, 'p.sc-cCsOjp.cdaqyF')
    # WHY_EXLAB_MAIN = (By.CSS_SELECTOR, 'div.sc-bZnhIo.CLhmH.is-inview')
    # WHY_EXLAB_BLOCK_TEXT = (By.CSS_SELECTOR, 'ol.sc-iAvgwm.fQGFrP.is-inview')
    # WHY_EXLAB_JOIN = (By.CSS_SELECTOR, 'a.sc-dkzDqf.gpYSxm.is-inview')