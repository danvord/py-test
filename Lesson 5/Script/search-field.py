from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

sleep=("10")

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