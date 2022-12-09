### Landing Auto Tests. I don't know why, but code navigation DOESN'T work in this repo.

## How to start:
```sh
git clone https://github.com/JeanSkyPoor/ExLab
pip install -r requirements.txt
pytest --alluredir report test_landing_page.py
allure serve report/
```
### To check last created allure report go to [here](https://github.com/JeanSkyPoor/ExLab/deployments) and click 'View deployment'