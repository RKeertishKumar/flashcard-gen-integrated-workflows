import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "./Web_drivers/chromedriver-linux64/chromedriver"
screenshots_path = "./Selenium_tests_screenshots/"

chrome_service = Service(chrome_driver_path)
chrome_options = Options()
chrome_options.binary_location = '/usr/bin/google-chrome-stable'  # Replace with the actual path

# Add any other necessary options
chrome_options.add_argument('--headless')

@pytest.fixture(scope="module")
def selenium_driver():
    driver_instance = webdriver.Chrome(service=chrome_service, options=chrome_options)
    yield driver_instance
    driver_instance.quit()

def test_navigation(selenium_driver):
    selenium_driver.get("http://127.0.0.1:5000")  # Update port to 5000
    selenium_driver.save_screenshot(screenshots_path + "Navigation.png")

def test_illustrations(selenium_driver):
    selenium_driver.get("http://127.0.0.1:5000")  # Update port to 5000
    element_illustration = selenium_driver.find_element(by="id", value="use_pixabay")

    # Perform an action
    element_illustration.click()
    selenium_driver.save_screenshot(screenshots_path + "Illustrations_button.png")

    # Assert existence of text-area
    assert selenium_driver.find_element(by="id", value="input_text").is_displayed()

if __name__ == '__main__':
    pytest.main()
