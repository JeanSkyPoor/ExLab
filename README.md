## UI automated tests for Exlab Start Up 
## [The latest allure report](https://jeanskypoor.github.io/ExLab/)
## How to start:
```sh
git clone https://github.com/JeanSkyPoor/ExLab
pip install -r requirements.txt
pytest --alluredir report tests/test_landing_page.py
allure serve report/
```