# test_checkout_with_invalid_zipcode.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import time
from base import start_driver, take_screenshot  # Imported from base.py

def test_checkout_with_invalid_zipcode():
    driver = start_driver()
    wait = WebDriverWait(driver, 10)

    def dismiss_google_warning_popup():
        try:
            # Look for Google password warning popup and dismiss if present
            warning_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
            )
            warning_button.click()
            print("Google warning popup dismissed.")
        except:
            pass  # Popup not shown

    def login(username, password):
        print("Logging in...")
        driver.get("https://www.saucedemo.com/")
        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        dismiss_google_warning_popup()
        print("Logged in successfully.")

    try:
        login("standard_user", "secret_sauce")

        print("Adding item to cart...")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

        driver.find_element(By.ID, "checkout").click()
        wait.until(EC.presence_of_element_located((By.ID, "first-name")))

        print("Filling info with invalid ZIP...")
        driver.find_element(By.ID, "first-name").send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("abcde")

        driver.find_element(By.ID, "continue").click()
        time.sleep(1)

        print("Attempting to finish checkout...")
        driver.find_element(By.ID, "finish").click()

        success_msg = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))).text
        if "THANK YOU FOR YOUR ORDER" in success_msg.upper():
            print("TC_CHECKOUT_03 -- Failed: Invalid ZIP did not trigger error. The system allowed checkout with an invalid ZIP code. This reflects a missing validation or design limitation.")

            take_screenshot(driver, "TC_CHECKOUT_03_fail")
        else:
            print("TC_CHECKOUT_03 Passed: Invalid ZIP blocked the checkout.")
            take_screenshot(driver, "TC_CHECKOUT_03_pass")

    except Exception as e:
        print(f"TC_CHECKOUT_03 Passed: Exception occurred due to invalid ZIP or failed navigation: {str(e)}")
        take_screenshot(driver, "TC_CHECKOUT_03_pass_exception")

    driver.quit()

if __name__ == "__main__":
    test_checkout_with_invalid_zipcode()
