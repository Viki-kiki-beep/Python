from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Ожидаем загрузку поля ввода
        delay_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_field.clear()
        delay_field.send_keys("45")

        # Нажимаем кнопки
        driver.find_element(By.XPATH, "//span[text()='7']").click()  # Исправлен XPath
        driver.find_element(By.XPATH, "//span[text()='+']").click()  # Исправлен XPath
        driver.find_element(By.XPATH, "//span[text()='8']").click()  # Исправлен XPath
        driver.find_element(By.XPATH, "//span[text()='=']").click()  # Убрана лишняя кавычка

        # Ожидание результата (увеличено время ожидания)
        result = WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        # Проверка результата
        result_element = driver.find_element(By.CLASS_NAME, "screen")
        assert "15" in result_element.text

    finally:
        driver.quit()

