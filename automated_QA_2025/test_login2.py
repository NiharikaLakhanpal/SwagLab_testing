# test_login2.py

from selenium.webdriver.common.by import By
from base import start_driver, take_screenshot
import time

# Test Case: Invalid Password (TC_LOGIN_02)
def test_invalid_password():
    driver = start_driver()  # Start the browser and navigate to the login page
    driver.get("https://www.saucedemo.com")
    time.sleep(1)  # Wait for the page to load

    # Enter valid username and invalid password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")  # Enter username
    driver.find_element(By.ID, "password").send_keys("abcd")  # Enter invalid password
    driver.find_element(By.ID, "login-button").click()  # Click the login button
    time.sleep(2)  # Wait for the page to process the login attempt

    # Retrieve the error message displayed on the page
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    expected_error_message = "Epic sadface: Username and password do not match any user in this service"

    # Validate the error message
    if error_message == expected_error_message:
        print("TC_LOGIN_02 -- Passed")
        screenshot_path = take_screenshot(driver, "TC_LOGIN_02_pass")  # Screenshot for passed test
    else:
        print("TC_LOGIN_02 -- Failed")
        screenshot_path = take_screenshot(driver, "TC_LOGIN_02_fail")  # Screenshot for failed test

    driver.quit()  # Close the browser

# Run this test if the script is executed directly
if __name__ == "__main__":
    test_invalid_password()
