import sys
from webdriver_manager.chrome import ChromeDriverManager  # Manages the download and setup of ChromeDriver
from selenium.webdriver.chrome.options import ChromiumOptions  # Provides options for configuring Chrome WebDriver
from selenium import webdriver  # Selenium WebDriver for controlling web browsers
from selenium.webdriver.chrome.service import Service  # Handles the ChromeDriver service
from selenium.webdriver.common.by import By  # Allows locating elements by various methods (e.g., ID, name, XPath)

# Function to test the score range on the web application
def test_scores():
    # Setting up Chrome options (e.g., headless mode, window size)
    chrome_options = ChromiumOptions()
    
    # Installing ChromeDriver and setting up the service with the options
    service = Service(ChromeDriverManager().install(), options=chrome_options)
    
    # Creating an instance of the Chrome WebDriver
    driver_chrome = webdriver.Chrome(service=service)
    
    # Navigating to the local web application
    driver_chrome.get("http://127.0.0.1:8777/")
    
    # Finding the score element by its ID on the page
    score = driver_chrome.find_element(By.ID, "score")
    
    # Checking if the score is within the valid range (0 to 1000)
    if 0 <= int(score.text) <= 1000:
        driver_chrome.quit()  # Close the browser if the score is valid
        return True
    else:
        driver_chrome.quit()  # Close the browser if the score is invalid
        return False

# Main function to execute the test and return an appropriate exit code
def main_function():
    if test_scores():
        sys.exit(0)  # Exit with code 0 if the test passed
    else:
        sys.exit(-1)  # Exit with code -1 if the test failed

# Entry point of the script
main_function()
