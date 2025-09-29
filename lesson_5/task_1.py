from selenium import webdriver
from selenium.webdriver.common.by import By

# Открыть браузер Google Chrome
driver = webdriver.Chrome()

# Перейти на страницу
driver.get("http://uitestingplayground.com/classattr")

# Кликнуть на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

# Ожидание ввода от пользователя перед закрытием браузера
input("Нажмите Enter, чтобы закрыть браузер...")

# Закрыть браузер
driver.quit()
