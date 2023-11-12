from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
 
driver.get("http://uitestingplayground.com/classattr")

# Click on the blue button
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

# Run the script 3 times in a row
for i in range(3):
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()

# Close browser
driver.quit()

