from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep=("5")

#Press on the "Close" button in the modal footer

mfooter=("div.modal-footer > p")

close_button=driver.find_element(By.CSS_SELECTOR, mfooter)
close_button.click()

#Close browser 

driver.quit()