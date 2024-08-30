import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys

import pytest
import allure


def test_mouse_events():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # this get command opens the web page in the current session
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    time.sleep(2)

    # first_name = driver.find_element(By.XPATH, "//input[@id='clickable']")
    #
    # action_chains = ActionChains(driver)
    # action_chains.key_down(Keys.SHIFT).send_keys_to_element(first_name, "Himanshu").key_up(Keys.SHIFT).context_click().perform()
    #
    # time.sleep(2)

    # Normal Driver - will find the elements and click on it, release it
    # Click and Hold - Will not release - For Drag and Drop commands

    atag = driver.find_element(By.ID, "click")
    atag.click()

    # Action Builders - For Mouse Interations
    # Actions Chains - Keyboard Events

    # if we want to use the SHIFT keys to make the input values UPPERCASE, we can use it with keys operations

    action_builder = ActionBuilder(driver)
    action_builder.pointer_action.pointer_up(MouseButton.BACK)
    action_builder.perform()

    time.sleep(2)
    driver.quit()
