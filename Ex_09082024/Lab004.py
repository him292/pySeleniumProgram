import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    # Options class: Customize the behaviour of browser during automated testing
    # headless browser: means no UI -> no browser opening but execution takes place in background - its FAST
    # other ex: Disable GPU, add extentions, maximize, set window size etc (these all you can do before starting browser)

    # open youtube.com and apply one extension (to block the ads) like adBlocker
    # Just add CRS downloaded on your browser and then download the CRX files of the extension you want to apply

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--incognito")
    chrome_options.add_extension("/Users/datashan/Downloads/AdBlock-—-CRX.crx")
    driver = webdriver.Chrome(chrome_options)
    # driver = webdriver.Edge()
    # driver = webdriver.Firefox()

    # this get command opens the web page in the current session
    driver.get("https://youtube.com")
    # driver.maximize_window()
    # print(driver.title)
    # assert driver.title == "Youtube"
    time.sleep(10)
    # driver.quit()
