# base.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os

# Start and return the Chrome WebDriver
def start_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito") 
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Take screenshot with test name and timestamp
def take_screenshot(driver, test_name):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(filepath)
    print(f"Screenshot saved: {filepath}")
    return filepath
