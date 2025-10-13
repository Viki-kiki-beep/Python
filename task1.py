from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Шаг 1: Переходим на страницу
    driver.get("http://uitestingplayground.com/ajax")
    
    # Ждем, пока кнопка станет кликабельной
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ajaxButton"))
    )
    
    # Шаг 2: Нажимаем на синюю кнопку
    button.click()
    
    # Шаг 3: Ждем появления зеленой плашки и получаем текст
    success_element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )
    
    success_text = success_element.text
    print(success_text)
    
finally:
    driver.quit()