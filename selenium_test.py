# Import code from module
from selenium import webdriver

# Import service function
from selenium.webdriver.chrome.service import Service

# Add paths
chrome_driver_path = "./Web_drivers/chromedriver-win64/chromedriver.exe"
screenshots_path = "./selenium_tests_screenshots/"

# Add a chrome service
chrome_service = Service(chrome_driver_path)

# Assign executable to code
driver = webdriver.Chrome(service = chrome_service)

# Navigate to website
# Adding print statements for better understanding of code execution

try:
    print("Navigating to the website")
    driver.get("http://127.0.0.1:3000")
    driver.save_screenshot(screenshots_path + "Navigation.png")


    # Find an element by its id and interact with it
    print("Finding and clicking the element")
    element_illustration = driver.find_element(by = "id", value = "use_pixabay")
    

    # Perform an action
    element_illustration.click()
    driver.save_screenshot(screenshots_path + "Illustrations_button.png")

    # Assert existance of text-area
    assert driver.find_element(by = "id", value = "input_text").is_displayed()
    
except Exception as e:
    print(f"An exception occured: {e}")
    

finally:
    driver.quit()
