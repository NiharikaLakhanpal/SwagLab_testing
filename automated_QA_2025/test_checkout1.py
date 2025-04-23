# test_checkout1.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base import start_driver, take_screenshot

def test_successful_checkout_flow():
    driver = start_driver()
    wait = WebDriverWait(driver, 10)

    def login(username, password):
        print("Logging in...")
        driver.get("https://www.saucedemo.com/")
        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        print("Logged in successfully.")

    try:
        # Step 1: Login
        login("standard_user", "secret_sauce")

        # Step 2: Add item to cart
        print("Adding item to cart...")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        # Step 3: Go to cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
        print("Item is in cart.")

        # Step 4: Proceed to checkout
        driver.find_element(By.ID, "checkout").click()
        wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        print("Checkout info page loaded.")

        # Step 5: Fill info and continue
        driver.find_element(By.ID, "first-name").send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        # Step 6: Finish order
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_info")))
        driver.find_element(By.ID, "finish").click()

        # Step 7: Verify success
        complete_header = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
        if "Thank you for your order!" in complete_header.text:
            print("TC_CHECKOUT_01 -- Passed: Order placed successfully.")
            screenshot_path = take_screenshot(driver, "TC_CHECKOUT_01_pass")
        else:
            raise Exception("Success message not found.")

    except Exception as e:
        print(f"TC_CHECKOUT_01 -- Failed: {str(e)}")
        screenshot_path = take_screenshot(driver, "TC_CHECKOUT_01_fail")

    driver.quit()

# Run the test
if __name__ == "__main__":
    test_successful_checkout_flow()