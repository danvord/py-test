from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
 
sleep=("10")

#Click the Add Element button five times

for _ in range(5):
    add_button = driver.find_element(By.CSS_SELECTOR, "[onclick='addElement()']")
    add_button.click()

#Collect a list of Delete buttons
delete_buttons = driver.find_elements(By.CSS_SELECTOR, "#elements button")

#Display button list size

print("Размер списка кнопок Delete:", len(delete_buttons))

#Close browser 

driver.quit()