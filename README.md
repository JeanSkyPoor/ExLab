[![pages-build-deployment](https://github.com/JeanSkyPoor/ExLab/actions/workflows/pages/pages-build-deployment/badge.svg?event=push)](https://github.com/JeanSkyPoor/ExLab/actions/workflows/pages/pages-build-deployment)

## Landing Auto Tests. I don't know why, but code navigation DOESN'T work in this repo.

### How to start:
1) 'git clone https://github.com/JeanSkyPoor/ExLab.git'
2) 'pip install -r requirements.txt' - install dependencies 
3) 'pytest --alluredir report test_landing_page.py' - run tests 
4) 'allure serve report/' - run allure report on local host