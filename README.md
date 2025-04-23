# SwagLab_testing

This repository contains the automated QA tests for the **User Authentication, Cart Management, Checkout process** functionality of an e-commerce website. The tests have been designed to ensure the application behaves correctly under various scenarios and meets the specified requirements.

## Project Overview

The automated tests have been implemented using **Python** and **Selenium**. The tests cover critical high-level functionalities, including:

- **Login Process**
- **Shopping Cart Operations**
- **Checkout Flow**

## High-Level Tests Performed

### 1. **Login Tests**

The login functionality is a key feature for any e-commerce platform, and ensuring its correctness is crucial for the user experience. The following scenarios were tested:

- **Valid Login**: Ensures that users can log in successfully with valid credentials.
- **Invalid Login**: Tests the behavior when incorrect credentials are entered, ensuring appropriate error messages are shown.
- **Empty Fields**: Verifies that the login form handles empty inputs correctly and prompts the user to fill in the necessary information.

### 2. **Shopping Cart Tests**

The shopping cart is central to the shopping experience, and its functionality was tested with the following critical scenarios:

- **Add Item to Cart**: Ensures that items are added to the cart correctly.
- **Remove Item from Cart**: Verifies that items can be removed from the cart as expected.
- **Cart Visibility**: Tests whether the cart displays the correct number of items and the total price, even after adding/removing items.

### 3. **Checkout Tests**

The checkout flow is one of the most critical parts of the e-commerce platform. The following high-level tests were performed to ensure the process is smooth and functional:

- **Successful Checkout**: Tests that users can complete a purchase successfully with valid payment information.
- **Empty Address**: Verifies the handling of missing shipping address and ensures users are prompted to provide this information.
- **Invalid Zipcode**: Checks if upon entering an invalid zipcode if an error arises or checkout processes smoothly.

### Why These Tests Are Critical

These tests represent the core functionality of the platform. Any issue with the login, cart, or checkout process directly impacts the user experience and, ultimately, the business' success. By automating these critical tests, we ensure that these features work reliably across all versions of the application, reducing the risk of failures in production.

### Tools and Technologies Used

- **Python**: Programming language used for writing test scripts.
- **Selenium**: Web automation tool used for interacting with the application.
- **HTML**: Test reporting framework for generating detailed and visually appealing HTML reports.
