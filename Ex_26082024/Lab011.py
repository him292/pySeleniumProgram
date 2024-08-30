import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import allure


def test_relative_locators():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # this get command opens the web page in the current session
    driver.get("https://www.aqi.in/real-time-most-polluted-city-ranking")

    time.sleep(5)

    driver.find_element(By.XPATH, "//input[@id='search_city']").click()
    driver.find_element(By.XPATH, "//input[@id='search_city']").send_keys("india")
    time.sleep(5)

    list_of_states = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr/td[2]")

    for state in list_of_states:
        if state.text.__contains__("India"):
            # belo code means, in all the p tags available, find the p tag which is in right of "//table[@id='example']/tbody/tr/td[2]"
            s1 = driver.find_element(locate_with(By.TAG_NAME, "p").to_right_of(state)).text
            s2 = driver.find_element(locate_with(By.TAG_NAME, "p").to_left_of(state)).text

            print("Name" + " | " + "ACQ" " | " + "Rank")
            print(state.text + " | " + s1 + " | " + s2)

    time.sleep(5)

    driver.quit()