import time

from selenium import webdriver


def test_open_vwologin():
    driver = webdriver.Chrome()
    # driver = webdriver.Edge()
    # driver = webdriver.Firefox()

    # this get command opens the web page in the current session
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(10)
    # driver.quit()
