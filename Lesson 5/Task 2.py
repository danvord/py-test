from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр драйвера
driver = webdriver.Chrome()

# Открываем страницу
driver.get('http://uitestingplayground.com/dynamicid')

# Кликаем на синюю кнопку
driver.find_element(By.XPATH, "//button[contains(text(),'Click Me')]").click()

# Запускаем скрипт 3 раза подряд
for i in range(3):
    # Ждем, пока появится блок с результатом
    result_block = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'dynamic-id')]/p"))
    )

    # Получаем текст результата и выводим его
    result_text = result_block.text
    print("Результат {0}: {1}".format(i+1, result_text))

    # Кликаем на синюю кнопку еще раз
    driver.find_element(By.XPATH, "//button[contains(text(),'Click Me')]").click()

# Закрываем браузер
driver.quit()