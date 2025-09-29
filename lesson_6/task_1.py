from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажатие на синюю кнопку
button = driver.find_element(By.ID, "ajaxButton")
button.click()

# Получение текста из зеленой плашки
message = driver.find_element(By.ID, "content").text
print(message)  # Ожидаемый вывод: "Data loaded with AJAX get request."

# Закрытие драйвера
driver.quit()
