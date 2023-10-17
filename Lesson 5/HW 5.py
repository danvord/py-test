#from selenium import webdriver

#driver = webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем страницу
driver = webdriver.Chrome()  # Для этого примера используется драйвер Chrome
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Кликаем на кнопку "Add Element" пять раз
for i in range(5):
    add_element_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='addElement()']")))
    add_element_button.click()

# Собираем список кнопок "Delete"
delete_buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[onclick='deleteElement()']")))

# Выводим размер списка кнопок "Delete"
print(f"Размер списка кнопок 'Delete': {len(delete_buttons)}")

# Закрываем браузер
driver.quit()
