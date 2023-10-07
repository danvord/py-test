from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
 
driver.get("https://the-internet.herokuapp.com/login")

sleep=("5")

#In the "Username" field, enter the value

userName="#username"

userName_field=("username")
userName_field=driver.find_element(By.CSS_SELECTOR, username) 
userName_field.send_keys("tomsmith")

#In the "Password" field, enter the value

pasSword=("#password")

pasSword_field=("password")
pasSword_field=driver.find_element(By.CSS_SELECTOR, password) 
pasSword_field.send_keys("SuperSecretPassword!")

#CLick on the "Login" button
 
login_button=("button[type='submit']") 
login_button.find_element(By.CSS_SELECTOR, button)
login_button.click()

#Close browser 

driver.quit()

