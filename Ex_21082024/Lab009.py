import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import allure


def test_makemytrip():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # this get command opens the web page in the current session
    driver.get("https://www.makemytrip.com/")
    time.sleep(5)

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='commonModal__close']")))

    driver.find_element(By.XPATH, "//span[@class='commonModal__close']").click()

    fromCity = driver.find_element(By.XPATH, "//input[@id='fromCity']")
    action_chains = ActionChains(driver)
    action_chains.send_keys_to_element(fromCity, "New Delhi").perform()
    time.sleep(3)
    action_chains.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    time.sleep(2)
    driver.quit()
