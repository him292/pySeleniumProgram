from selenium import webdriver


class test_sample():
    # Selenium4: which will take care of the driver by itself
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    assert driver.title == "https://www.google.com"
