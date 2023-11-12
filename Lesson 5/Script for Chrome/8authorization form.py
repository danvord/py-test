from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

#In the "Username" field, enter the value

userName="#username"

userName_field=("username")
userName_field=driver.find_element(By.CSS_SELECTOR, userName) 
userName_field.send_keys("tomsmith")

#In the "Password" field, enter the value

pasSword=("#password")

pasSword_field=("password")
pasSword_field=driver.find_element(By.CSS_SELECTOR, pasSword) 
pasSword_field.send_keys("SuperSecretPassword!")

#CLick on the "Login" button
 
login_button=("button[type='submit']") 
login_button=driver.find_element(By.CSS_SELECTOR, login_button)
login_button.click()

#Close browser 

driver.quit()

