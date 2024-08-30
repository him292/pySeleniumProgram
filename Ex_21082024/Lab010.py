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


def test_vwo_hover_and_click():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # this get command opens the web page in the current session
    driver.get("https://app.vwo.com/#/analyze/recording")
    main_window_handle = driver.current_window_handle
    print("Before Click " + main_window_handle)

    list = driver.find_elements(By.CSS_SELECTOR, "//button[@class='font-semibold relative rounded-[0.5em] opacity-100 hover:opacity-90 active:opacity-100 flex w-full items-center justify-center shadow-hotBox transition-opacity cursor-pointer min-h-[3em] text-[1em] leading-[1.125em] px-[1.25em] py-[0.75em]']")

    value = list[0]

    action_chains = ActionChains(driver)
    action_chains.click(value).perform()

    time.sleep(5)

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn--primary btn--inverted btn--big Mend(20px) Mend(0):lc ng-binding ng-scope']")))