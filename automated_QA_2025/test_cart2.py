# test_cart2.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base import start_driver, take_screenshot

def test_add_and_remove_item_from_cart():
    driver = start_driver()
    driver.get("https://www.saucedemo.com")  # Navigate to the login page
    
    # Log in with valid credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Wait until the inventory page loads
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    print("Login successful!")
    
    # Add "Sauce Labs Bike Light" to the cart
    try:
        bike_light_add_button = driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bike-light']")
        bike_light_add_button.click()  # Add item to cart
        print("Sauce Labs Bike Light added to cart!")
    except Exception as e:
        print(f"Failed to add product to cart: {e}")
        driver.quit()
        return
    
    # Take a screenshot after adding the item to the cart
    screenshot_path_added = take_screenshot(driver, "TC_CART_02_added_bike_light")
    print(f"Screenshot (add): {screenshot_path_added}")
    
    # Navigate to the cart page to verify the item is added
    try:
        cart_icon = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
        cart_icon.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart_item")))
        print("Navigated to cart page!")
    except Exception as e:
        print(f"Failed to navigate to cart page: {e}")
        driver.quit()
        return
    
    # Verify the item is in the cart
    try:
        cart_item = driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name")
        print(f"Item in cart: {cart_item.text}")
    except Exception as e:
        print(f"Failed to find item in cart: {e}")
        driver.quit()
        return
    
    # Remove the product from the cart
    try:
        remove_button = driver.find_element(By.CSS_SELECTOR, ".cart_item .cart_button")  # Remove button
        remove_button.click()
        print("Product removed from cart!")
    except Exception as e:
        print(f"Failed to remove product from cart: {e}")
        driver.quit()
        return
    
    # Take a screenshot after removing the item from the cart
    screenshot_path_removed = take_screenshot(driver, "TC_CART_02_removed_bike_light")
    print(f"Screenshot (remove): {screenshot_path_removed}")
    
    # Verify that the cart is empty after removal
    try:
        cart_items = driver.find_elements(By.CSS_SELECTOR, ".cart_item")
        if len(cart_items) == 0:
            print("TC_CART_02 -- Passed - Cart is empty!")
        else:
            print("TC_CART_02 -- Failed - Product still in cart.")
    except Exception as e:
        print(f"Error finding cart items: {e}")
    
    driver.quit()

# Run the test
if __name__ == "__main__":
    test_add_and_remove_item_from_cart()

