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
    WHY_EXLAB_ANCHOR = (By.CSS_SELECTOR, 'div.sc-cCsOjp.bWNIcl')

    #Block YOUR OPPORTUNITY 
    LOGO_YOUR_OPPORTUNITY = (By.CSS_SELECTOR, 'div.sc-dIouRR.gWQVjR > img')
    MAIN_TITLE_YOUR_OPPROTUNITY = (By.CSS_SELECTOR, 'div.sc-dmRaPn.ljhwJa')
    BLOCK_TEXT_YOUR_OPPORTUNITY = (By.CSS_SELECTOR, 'div.sc-kgflAQ.gUFAgN')

    #block FOOTER
    LINKEDIN_FOOTER = (By.CSS_SELECTOR, 'li.sc-dkdnUF.fbGNMP:nth-of-type(1)')
    INSTAGRAM_FOOTER = (By.CSS_SELECTOR, 'li.sc-dkdnUF.fbGNMP:nth-of-type(2)')
    TELEGRAM_FOOTER = (By.CSS_SELECTOR, 'li.sc-dkdnUF.fbGNMP:nth-of-type(3)')
    YOUTUBE_FOOTER = (By.CSS_SELECTOR, 'li.sc-dkdnUF.fbGNMP:nth-of-type(4)')

    STAY_CONNECTED_TITLE = (By.CSS_SELECTOR, 'div.sc-bhVIhj.uaVnA')
    DESCRIPTION_STAY_CONNECTED = (By.CSS_SELECTOR, 'div.sc-eGAhfa.cacMWv')
    LOGO_FOOTER = (By.CSS_SELECTOR, 'div.sc-fIavCj.fEzmxG')
    TEXT_UNDER_LOGO_FOOTER = (By.CSS_SELECTOR, 'div.sc-gITdmR.hYaavu')
    MAIL_ADDRESS_FOOTER = (By.CSS_SELECTOR, 'div.sc-evrZIY.UwGJa > a')

    #block ABOUT US
    MAIN_TITLE_ABOUT_US = (By.CSS_SELECTOR, '[id=about] > div.sc-eCYdqJ.koNCEH')
    DESCRIPTION_ABOUT_US = (By.CSS_SELECTOR, 'p.sc-himrzO.bgsrpw')

    MAIN_TITLE_WHY_EXLAB = (By.CSS_SELECTOR, 'div.sc-ciZhAO.fBFmnR')
    DESCRIPTION_WHY_EXLAB = (By.CSS_SELECTOR, 'ol.sc-bZnhIo.fYGDkJ')
    JOIN_WHY_EXLAB_BLOCK = (By.CSS_SELECTOR, 'div.sc-jdAMXn.gLqyEH > a')

    #block PROJECTS
    MAIN_TITLE_PROJECTS = (By.CSS_SELECTOR, '[id=projects-title-wrapper]>div')
    ALL_PROJECTS_BLOCK = (By.CSS_SELECTOR, 'div.sc-bBXxYQ.iMLBAV')

    #block MENTORS
    MENTORS_ALL_SPOILERS_BLOCK = (By.CSS_SELECTOR, 'div.sc-jIAOiI.eSpxWu')
    MENTORS_BLOCK_WITH_DATA_OPENED_SPOILER = (By.CSS_SELECTOR, 'div.sc-bUbCnL.fJhsUc')
    MENTOR_IMAGE = (By.CSS_SELECTOR, 'div.sc-bUbCnL.fJhsUc > img')
    MENTOR_DESCRIPTION = (By.CSS_SELECTOR, 'div.sc-bUbCnL.fJhsUc > ul.sc-dsQDmV.iZMcmm')
    MENTORS_TITLE = (By.CSS_SELECTOR, '[id=mentors] > div:nth-of-type(1)')

    #block STARTUP FOR
    MAIN_TITLE_STARTUP_FOR = (By.CSS_SELECTOR, '[id=startup] > [id=startup-title-wrapper]')
    JUNIORS_DESCRIPTION_STARTUP_FOR = (By.CSS_SELECTOR, 'div.sc-jfmDQi.jtqNlU')
    RECRUTER_DESCRIPTIONS_STARTUP_FOR = (By.CSS_SELECTOR, 'div.sc-ehmTmK.hNtRAb')

    #block HELP PROJECT
    BOOSTY_HELP_PROJECT_BUTTON = (By.CSS_SELECTOR, 'div.sc-bWXABl.klepWn > a:nth-of-type(1)')
    PATREON_HELP_PROJECT_BUTTON = (By.CSS_SELECTOR, 'div.sc-bWXABl.klepWn > a:nth-of-type(2)')
    TITLE_HELP_PROJECT = (By.CSS_SELECTOR, 'div.sc-jTYCaT.coDMnK')
    DESCRIPTION_HELP_PROJECT = (By.CSS_SELECTOR, 'div.sc-fctJkW.gfwicC')
