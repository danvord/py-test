from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
 
driver.get("http://the-internet.herokuapp.com/entry_ad")


#Press on the "Close" button in the modal footer

mfooter="div.modal-footer > p"

close_button = WebdriverWait(driver, timeout:10).until(EC.element_to_be_clickable)((By.CSS_SELECTOR, mfooter)))
close_button.click()

#Close browser 

driver.quit()
