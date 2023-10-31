from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
 
driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep=("5")

#Press on the "Close" button in the modal footer

mfooter="div.modal-footer > p"

close_button=driver.find_element(By.CSS_SELECTOR, mfooter)
close_button.click()

#Close browser 

driver.quit()