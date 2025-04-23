# test_cart3.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base import start_driver, take_screenshot

def test_cart_persistence_after_relogin():
    driver = start_driver()
    wait = WebDriverWait(driver, 10)

    def login(username, password):
        print("Logging in...")
        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
        print("Logged in and reached inventory page.")

    # Step 1: Login
    driver.get("https://www.saucedemo.com")
    login("standard_user", "secret_sauce")

    # Step 2: Add item to cart
    print("Adding item to cart...")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Step 3: Logout
    print("Logging out...")
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    time.sleep(0.5)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    print("Logged out and login page loaded.")

    # Step 4: Login again
    login("standard_user", "secret_sauce")

    # Step 5: Go to cart
    print("Navigating to cart...")
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()

    # Step 6: Verify item is still in cart
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
        print("TC_CART_03 -- Passed: Item is still in the cart after re-login.")
        screenshot_path = take_screenshot(driver, "TC_CART_03_pass")
    except:
        print("TC_CART_03 -- Failed: Item is NOT in the cart after re-login.")
        screenshot_path = take_screenshot(driver, "TC_CART_03_fail")

    print(f"Screenshot saved at: {screenshot_path}")
    driver.quit()

# Run the test
if __name__ == "__main__":
    test_cart_persistence_after_relogin()
