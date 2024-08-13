import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure


def test_mini_project4():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # this get command opens the web page in the current session
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Locators
    facility_xpath = "//select[@class='form-control']"
    select_facility_value = "//select[@class='form-control']//option[@value='Hongkong CURA Healthcare Center']"
    checkbox_xpath = "//label[@class='checkbox-inline']//input[@name='hospital_readmission']"
    calendar_xpath = "//span[@class='glyphicon glyphicon-calendar']"
    select_date_xpath = "//div[@class='datepicker-days']//tr//td[@class='day' and text()='17']"
    comment_area_xpath = "//textarea[@id='txt_comment']"
    btn_book_appointment_xpath = "//button[@id='btn-book-appointment']"

    btn_appointment = driver.find_element(By.ID, "btn-make-appointment")
    btn_appointment.click()

    # Verify if the URL changes

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(3)

    enter_user = driver.find_element(By.ID, "txt-username")
    enter_user.send_keys("John Doe")

    time.sleep(1)

    enter_user = driver.find_element(By.ID, "txt-password")
    enter_user.send_keys("ThisIsNotAPassword")

    time.sleep(1)

    btn_login = driver.find_element(By.ID, "btn-login")
    btn_login.click()

    time.sleep(3)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    text_appointment = driver.find_element(By.TAG_NAME, "h2")
    assert text_appointment.text == "Make Appointment"

    # booking an appointment page - Automation script

    facility = driver.find_element(By.XPATH, facility_xpath)
    facility.click()
    select_facility = driver.find_element(By.XPATH, select_facility_value)
    select_facility.click()

    checkbox = driver.find_element(By.XPATH, checkbox_xpath)
    checkbox.click()

    time.sleep(1)

    calendar = driver.find_element(By.XPATH, calendar_xpath)
    calendar.click()
    select_date = driver.find_element(By.XPATH, select_date_xpath)
    select_date.click()

    time.sleep(1)

    comment_area = driver.find_element(By.XPATH, comment_area_xpath)
    comment_area.click()
    comment_area.send_keys("This is a test comment")
    time.sleep(1)

    btn_book_appointment = driver.find_element(By.XPATH, btn_book_appointment_xpath)
    btn_book_appointment.click()
    time.sleep(3)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/appointment.php#summary"

    time.sleep(3)
    text_confirmation = driver.find_element(By.TAG_NAME, "h2")
    assert text_confirmation.text == "Appointment Confirmation"
    time.sleep(3)


    driver.quit()
