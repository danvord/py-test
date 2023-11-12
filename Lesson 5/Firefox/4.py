from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://uitestingplayground.com/dynamicid")


 #Click on the blue button

click_blue_button=driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
click_blue_button.click

#Run the script 3 times in a row 

for i in range(3):

    click_blue_button=driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    click_blue_button.click()

#Close browser 

driver.quit()
