import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    # Options class: Customize the behaviour of browser during automated testing
    # headless browser: means no UI -> no browser opening but execution takes place in background - its FAST
    # other ex: Disable GPU, add extentions, maximize, set window size etc (these all you can do before starting browser)

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x980")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    # driver = webdriver.Edge()
    # driver = webdriver.Firefox()

    # this get command opens the web page in the current session
    driver.get("https://app.vwo.com")
    # driver.maximize_window()
    # print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(10)
    # driver.quit()
