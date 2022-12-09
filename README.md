### Landing Auto Tests. I don't know why, but code navigation DOESN'T work in this repo.

## How to start:
```sh
git clone https://github.com/JeanSkyPoor/ExLab
pip install -r requirements.txt
pytest --alluredir report test_landing_page.py
allure serve report/
```
### For tests you have to download driver, for [example](https://chromedriver.chromium.org/downloads) and add exe file in main directory (./Exlab/)
### [Here](https://jeanskypoor.github.io/ExLab/) you can check last allure report 