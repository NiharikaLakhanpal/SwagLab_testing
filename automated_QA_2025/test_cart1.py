# test_cart1.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base import start_driver, take_screenshot
import time

# Test Case: Add Item to Cart (TC_CART_01)
def test_add_item_to_cart():
    driver = start_driver()  # Start the browser session
    driver.get("https://www.saucedemo.com")  # Navigate to the login page

    # Log in with valid credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for inventory page to load
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    print("Login successful!")

    # Add a product to the cart
    try:
        add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()
        print("Product added to cart!")
    except Exception as e:
        print(f"Failed to add product to cart: {e}")
        driver.quit()
        return

    # Navigate to the cart page
    try:
        cart_icon = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
        cart_icon.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart_item")))
        print("Navigated to cart page!")
    except Exception as e:
        print(f"Failed to navigate to cart page: {e}")
        driver.quit()
        return

    # Screenshot of cart page
    screenshot_path = take_screenshot(driver, "TC_CART_01_add_product")

    # Verify the correct item was added
    try:
        cart_item = driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text
        expected_item_name = "Sauce Labs Backpack"

        if cart_item == expected_item_name:
            print("TC_CART_01 -- Passed")
        else:
            print("TC_CART_01 -- Failed")
    except Exception as e:
        print(f"Error finding cart item: {e}")

    driver.quit()

# Run this test if executed directly
if __name__ == "__main__":
    test_add_item_to_cart()
