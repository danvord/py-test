from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://uitestingplayground.com/classattr")

sleep=("5")

#Click on the blue button

click_on_the_button=driver.find_element(By.CSS_SELECTOR, "button.btn.class3.btn-primary.btn-test")
click_on_the_button.click()

#Run the script 3 times in a row 

for blue_button in range(3):

    click_on_the_button=driver.find_element(By.CSS_SELECTOR, "button.btn.class3.btn-primary.btn-test")
    click_on_the_button.click()
    
#Close browser 

driver.quit()
