import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# PageLoad Strategy: 3 strategies:

# None: default, will not wait for page to load completely
# Normal: waits for the page to load completely
# Eager:  DOMContentLoaded event is fired as soon as possible, without waiting for resources to finish loading (images might still be loading)
def test_open_vwologin():

    chrome_options = Options()
    # chrome_options.page_load_strategy = 'eager'
    chrome_options.add_argument("--page-load-strategy=none")
    driver = webdriver.Chrome(chrome_options)

    # this get command opens the web page in the current session
    driver.get("https://app.vwo.com")
    driver.maximize_window()

