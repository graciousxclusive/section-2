# Test script to test valid login functionality

# Import necessary libraries and modules
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a test class
class ValidLoginTest(unittest.TestCase):

    # Set up the webdriver and navigate to the login page
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/login")

    # Test valid login
    def test_valid_login(self):

        # Locate the username and password input fields
        username = self.driver.find_element_by_id("username")
        password = self.driver.find_element_by_id("password")

        # Enter valid login credentials
        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
         # Submit the form
        password.send_keys(Keys.RETURN)

        # Verify that the user is logged in by checking for a success message or the appearance of a dashboard page
        success_message = self.driver.find_element_by_class_name("success")
        self.assertIn("You logged into a secure area!", success_message.text)

    # Tear down the webdriver after the test is complete
    def tearDown(self):
        self.driver.quit()

# Run the test
if __name__ == '__main__':
    unittest.main()