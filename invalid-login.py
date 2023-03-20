# Test script to test invalid login functionality

# Import necessary libraries and modules
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a test class
class InvalidLoginTest(unittest.TestCase):

    # Set up the webdriver and navigate to the login page
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/login")

    # Test invalid login
    def test_invalid_login(self):

        # Locate the username and password input fields
        username = self.driver.find_element_by_id("username")
        password = self.driver.find_element_by_id("password")

        # Enter invalid login credentials
        username.send_keys("thomas")
        password.send_keys("SecretPassword!")
        # Submit the form
        password.send_keys(Keys.RETURN)

        # Verify that the user is not logged in by checking for an error message or the appearance of the login page
        error_message = self.driver.find_element_by_class_name("error")
        self.assertIn("Your username is invalid!", error_message.text)

    # Tear down the webdriver after the test is complete
    def tearDown(self):
        self.driver.quit()

# Run the test
if __name__ == '__main__':
    unittest.main()