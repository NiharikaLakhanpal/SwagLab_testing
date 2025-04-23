# test_login1.py

from selenium.webdriver.common.by import By
from base import start_driver, take_screenshot
import time

# Test Case: Valid Login (TC_LOGIN_01)
def test_valid_login():
    driver = start_driver()  # Initialize the WebDriver to start the browser session
    driver.get("https://www.saucedemo.com")  # Navigate to the login page of the Sauce Demo website
    time.sleep(1)  # Sleep for 1 second to allow page elements to load

    driver.find_element(By.ID, "user-name").send_keys("standard_user")  # Find the username input field and send the test username
    driver.find_element(By.ID, "password").send_keys("secret_sauce")  # Find the password input field and send the test password
    driver.find_element(By.ID, "login-button").click()  # Finds the login button and clicks in attempt to log in
    time.sleep(2)  # Sleep for 2 seconds to allow the page to load after login attempt

    # Check if the current URL matches the expected URL after successful login
    if driver.current_url == "https://www.saucedemo.com/inventory.html":
        print("TC_LOGIN_01 Passed")
        screenshot_path = take_screenshot(driver, "TC_LOGIN_01_pass")  # If the login was successful, print a success message and capture a screenshot
    else:
        print("TC_LOGIN_01 Failed")
        screenshot_path = take_screenshot(driver, "TC_LOGIN_01_fail")  # If the login was not successful, print a failure message and capture a screenshot

    driver.quit()  # Close the browser session

# Executes the test if this file is run directly
if __name__ == "__main__":
    test_valid_login()
