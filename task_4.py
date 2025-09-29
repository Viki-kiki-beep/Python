from selenium import webdriver
from selenium.webdriver.common.by import By

# Открыть браузер FireFox
driver = webdriver.Firefox()

# Перейти на страницу
driver.get("http://the-internet.herokuapp.com/login")

# Ввести значение в поле username
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("tomsmith")

# Ввести значение в поле password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("SuperSecretPassword!")

# Нажать кнопку Login
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Вывести текст с зеленой плашки в консоль
success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
print(success_message)

# Закрыть браузер
driver.quit()
