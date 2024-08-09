import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Remote Webdriver: If you want to execute your automation scripts on a remote machine
# we need IP address, browser, windows/MAC , version of windows



def test_open_vwologin():

    driver = webdriver.Chrome()

    # this get command opens the web page in the current session
    driver.get("https://app.vwo.com")
    driver.maximize_window()


    # difference between driver.close() and driver.quit()
    # driver.close() will close the current window
    # driver.quit() will close the entire session

    time.sleep(10)

