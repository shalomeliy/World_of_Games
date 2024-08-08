import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_scores_service():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/lib/chromium/chrome"  # Path to Chromium in Docker container

    # Use the ChromeDriver installed in the Docker container
    service = Service("/usr/lib/chromium/chromedriver")  # Ensure this matches the Dockerfile

    try:
        # Initialize WebDriver with the managed ChromeDriver
        driver_chrome = webdriver.Chrome(service=service, options=chrome_options)

        # Open the target URL
        driver_chrome.get("http://127.0.0.1:8777/")

        # Find the score element and validate it
        score = driver_chrome.find_element(By.ID, "score")
        if 0 <= int(score.text) <= 1000:
            driver_chrome.quit()
            return True
        else:
            driver_chrome.quit()
            return False
    except Exception as e:
        print(f"Error initializing ChromeDriver: {e}")
        return False

def main_function():
    if test_scores_service():
        sys.exit(0)
    else:
        sys.exit(-1)

if __name__ == "__main__":
    main_function()
