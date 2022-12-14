from selenium.webdriver.common.by import By

#WHERE_WHAT_OPTIONAL


class LandingPageLocators():
    

    THEME = (By.CSS_SELECTOR, 'div.sc-bczRLJ')
    SELECTOR_FOR_SCROLL = (By.CSS_SELECTOR, 'div.sc-fEOsli.iema-Dv') #находит элементы для прыжков-скролов

    #Block HEADER
    HEADER_EXLAB_LOGO = (By.CSS_SELECTOR, 'div.sc-gKXOVf.hXUcbs > [id=logo_mobile]')
    HEADER_ABOUT_US_BUTTON= (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(1)')
    HEADER_PROJECTS_BUTTON= (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(2)')
    HEADER_MENTORS_BUTTON = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(3)')
    HEADER_STARTUP_FOR_BUTTON = (By.CSS_SELECTOR, 'li.sc-crXcEl:nth-of-type(4)') 
    HEADER_SUN_ICON = (By.CSS_SELECTOR, 'div.sc-fnykZs.fEkGUM')
    HEADER_JOIN_BUTTON = (By.CSS_SELECTOR, 'div.sc-hAZoDl.hrEelO')

    #Anchor to blocks
    ANCHOR_ABOUT_US = (By.CSS_SELECTOR, '[id=about]')
    ANCHOR_PROJECTS = (By.CSS_SELECTOR, '[id=projects]')
    ANCHOR_MENTORS = (By.CSS_SELECTOR, '[id=mentors]')
    ANCHOR_STARTUP_FOR = (By.CSS_SELECTOR, '[id=startup]')
    ANCHOR_HELP_PROJECT = (By.CSS_SELECTOR, 'div.sc-jTYCaT.coDMnK')
    ANCHOR_FOOTER = (By.CSS_SELECTOR, '[id=footer]')
    ANCHOR_WHY_EXLAB = (By.CSS_SELECTOR, 'div.sc-cCsOjp.bWNIcl')

    #Block YOUR OPPORTUNITY 
    YOUR_OPPORTUNITY_LOGO = (By.CSS_SELECTOR, 'div.sc-dIouRR.gWQVjR > img')
    YOUR_OPPORTUNITY_MAIN_TITLE = (By.CSS_SELECTOR, 'div.sc-dmRaPn.ljhwJa')
    YOUR_OPPORTUNITY_DESCRIPTION = (By.CSS_SELECTOR, 'div.sc-kgflAQ.gUFAgN')

    #block FOOTER
    FOOTER_LINKEDIN = (By.CSS_SELECTOR, 'li.sc-dkdnUF.fbGNMP:nth-of-type(1)')
    FOOTER_INSTAGRAM = (By.CSS_SELECTOR, 'li.sc-dkdnUF.fbGNMP:nth-of-type(2)')
    FOOTER_TELEGRAM = (By.CSS_SELECTOR, 'li.sc-dkdnUF.fbGNMP:nth-of-type(3)')
    FOOTER_YOUTUBE = (By.CSS_SELECTOR, 'li.sc-dkdnUF.fbGNMP:nth-of-type(4)')
    FOOTER_LOGO  = (By.CSS_SELECTOR, 'div.sc-fIavCj.fEzmxG')
    FOOTER_STAY_CONNECTED_TITLE = (By.CSS_SELECTOR, 'div.sc-bhVIhj.uaVnA')
    FOOTER_DESCRIPTION_STAY_CONNECTED = (By.CSS_SELECTOR, 'div.sc-eGAhfa.cacMWv')
    FOOTER_UNDER_LOGO_TEXT = (By.CSS_SELECTOR, 'div.sc-gITdmR.hYaavu')
    FOOTER_MAIL_ADDRESS = (By.CSS_SELECTOR, 'div.sc-evrZIY.UwGJa > a')

    #block ABOUT US
    ABOUT_US_MAIN_TITLE = (By.CSS_SELECTOR, '[id=about] > div.sc-eCYdqJ.koNCEH')
    ABOUT_US_DESCRIPTION = (By.CSS_SELECTOR, 'p.sc-himrzO.bgsrpw')

    #block WHY_EXLAB
    WHY_EXLAB_MAIN_TITLE = (By.CSS_SELECTOR, 'div.sc-ciZhAO.fBFmnR')
    WHY_EXLAB_DESCRIPTION = (By.CSS_SELECTOR, 'ol.sc-bZnhIo.fYGDkJ')
    WHY_EXLAB_JOIN_BUTTON = (By.CSS_SELECTOR, 'div.sc-jdAMXn.gLqyEH > a')

    #block PROJECTS
    PROJECTS_MAIN_TITLE = (By.CSS_SELECTOR, '[id=projects-title-wrapper]>div')
    PROJECTS_ALL_PROJECTS_BLOCK = (By.CSS_SELECTOR, 'div.sc-bBXxYQ.iMLBAV')

    #block MENTORS
    MENTORS_ALL_SPOILERS_BLOCK = (By.CSS_SELECTOR, 'div.sc-jIAOiI.eSpxWu')
    MENTORS_BLOCK_WITH_DATA_OPENED_SPOILER = (By.CSS_SELECTOR, 'div.sc-bUbCnL.fJhsUc')
    MENTOR_IMAGE = (By.CSS_SELECTOR, 'div.sc-bUbCnL.fJhsUc > img')
    MENTOR_DESCRIPTION = (By.CSS_SELECTOR, 'div.sc-bUbCnL.fJhsUc > ul.sc-dsQDmV.iZMcmm')
    MENTORS_TITLE = (By.CSS_SELECTOR, '[id=mentors] > div:nth-of-type(1)')

    #block STARTUP FOR
    STARTUP_FOR_MAIN_TITLE = (By.CSS_SELECTOR, '[id=startup] > [id=startup-title-wrapper]')
    STARTUP_FOR_JUNIORS_DESCRIPTION = (By.CSS_SELECTOR, 'div.sc-jfmDQi.jtqNlU')
    STARTUP_FOR_RECRUTER_DESCRIPTION = (By.CSS_SELECTOR, 'div.sc-ehmTmK.hNtRAb')

    #block HELP PROJECT
    HELP_PROJECT_BOOSTY_BUTTON = (By.CSS_SELECTOR, 'div.sc-bWXABl.klepWn > a:nth-of-type(1)')
    HELP_PROJECT_PATREON_BUTTON = (By.CSS_SELECTOR, 'div.sc-bWXABl.klepWn > a:nth-of-type(2)')
    HELP_PROJECT_TITLE = (By.CSS_SELECTOR, 'div.sc-jTYCaT.coDMnK')
    HELP_PROJECT_DESCRIPTION = (By.CSS_SELECTOR, 'div.sc-fctJkW.gfwicC')