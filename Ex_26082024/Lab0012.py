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


def test_svg_shadow_dom():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # this get command opens the web page in the current session
    # driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.get(
        "https://visitedplaces.com/india2020/?map=india2020&projection=geoMercator&theme=dark-green&water=0&graticule=0&names=1&duration=2000&placeduration=100&slider=0&autoplay=0&autozoom=none&autostep=0&home=IN&places=~IN-TR")
    time.sleep(5)

    states = driver.find_elements(By.XPATH, "//*name()='svg'/*[name()='g'][7]/*[name()='g'/*[name()='path']")

    for state in states:
        print(state.get_attribute("aria-label"))
        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name="India Map", attachment_type=allure.attachment_type.PNG)
    driver.quit()

    time.sleep(5)

    driver.find_element(By.XPATH, "//input[@id='search_city']").click()
    driver.find_element(By.XPATH, "//input[@id='search_city']").send_keys("india")
    time.sleep(5)

    list_of_states = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr/td[2]")
