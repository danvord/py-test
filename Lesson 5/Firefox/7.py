from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/inputs")

#Enter the value "1000" and clear it

search=("input[type='number']")
search_field=driver.find_element(By.CSS_SELECTOR, search)
search_field.send_keys("1000")
search_field.clear()

#Enter the value "999" in the cleared field

search_field.send_keys("999")

#Close browser 

driver.quit()