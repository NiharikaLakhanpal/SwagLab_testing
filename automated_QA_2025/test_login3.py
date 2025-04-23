# test_login3.py

from selenium.webdriver.common.by import By
from base import start_driver, take_screenshot
import time

# Test Case: Locked Out User Login (TC_LOGIN_03)
def test_locked_out_user():
    driver = start_driver()  # Start the browser session
    driver.get("https://www.saucedemo.com")  # Navigate to the Sauce Demo login page
    time.sleep(1)  # Wait for the page to load

    # Enter credentials for a locked-out user
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")  # Enter locked-out username
    driver.find_element(By.ID, "password").send_keys("secret_sauce")  # Enter password
    driver.find_element(By.ID, "login-button").click()  # Attempt login
    time.sleep(2)  # Wait for the result

    # Capture and compare the error message
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    expected_error_message = "Epic sadface: Sorry, this user has been locked out."

    if error_message == expected_error_message:
        print("TC_LOGIN_03 -- Passed")
        screenshot_path = take_screenshot(driver, "TC_LOGIN_03_pass")  # Screenshot for pass
    else:
        print("TC_LOGIN_03 -- Failed")
        screenshot_path = take_screenshot(driver, "TC_LOGIN_03_fail")  # Screenshot for fail

    driver.quit()  # Close the browser session

# Run this test if executed directly
if __name__ == "__main__":
    test_locked_out_user()
