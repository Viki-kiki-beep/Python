from selenium import webdriver
from selenium.webdriver.common.by import By

# Открыть браузер FireFox
driver = webdriver.Firefox()

# Перейти на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Ввести в поле текст Sky
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("Sky")

# Очистить это поле
input_field.clear()

# Ввести в поле текст Pro
input_field.send_keys("Pro")

# Закрыть браузер
driver.quit()
