from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (for example, using edge)
driver = webdriver.Edge()

# Construct the local file URL
file_path = r"C:\Users\faiza\Desktop\Dev-Flashcard-Generator-WebApp\templates\index.html"
local_file_url = "file://" + file_path.replace("\\", "/")

# Open the local HTML file
driver.get(local_file_url)

# Find the input_text textarea and enter a paragraph
input_text_area = driver.find_element(By.ID, "input_text")
input_text_area.send_keys("CAT IS PLAYING WITH LION")  # Replace with your text

# Find the use_pixabay checkbox and click it
use_pixabay_checkbox = driver.find_element(By.ID, "use_pixabay")
use_pixabay_checkbox.click()

# Find the Generate Flashcards button and click it
generate_button = driver.find_element(By.XPATH, "//input[@type='submit']")
generate_button.click()

# You can continue to interact with other elements as needed

# Don't forget to close the browser when you're done
driver.quit()
