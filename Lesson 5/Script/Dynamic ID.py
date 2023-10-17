from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
 
driver.get("http://uitestingplayground.com/dynamicid")

sleep=("5")

 #Click on the blue button

click_blue_button=driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
click_blue_button.click

#Run the script 3 times in a row 

for i in range(3):

    click_blue_button=driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    click_blue_button.click()

#Close browser 

driver.quit()
