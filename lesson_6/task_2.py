from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/textinput")

# Указание текста в поле ввода
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

# Нажатие на синюю кнопку
button = driver.find_element(By.XPATH, "//button[@id='updatingButton']")
button.click()

# Получение текста кнопки
button_text = button.text
print(button_text)  # Ожидаемый вывод: "SkyPro"

# Закрытие драйвера
driver.quit()
