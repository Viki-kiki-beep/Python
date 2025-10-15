from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    # Инициализация драйвера Edge
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    try:
        # Шаг 1: Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Ожидание появления формы
        wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

        # Шаг 2: Заполнение формы значениями
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # Zip code оставляем пустым
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Шаг 3: Нажать кнопку Submit
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
        submit_button.click()

        # Даем время для применения стилей валидации
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

        # Шаг 4: Проверка, что поле Zip code подсвечено красным
        zip_code_field = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code_field.get_attribute("class"), "Поле Zip code должно быть подсвечено красным"

        # Шаг 5: Проверка, что остальные поля подсвечены зеленым
        fields_to_check = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]

        for field_id in fields_to_check:
            field = driver.find_element(By.ID, field_id)
            assert "alert-success" in field.get_attribute("class"), f"Поле {field_id} должно быть подсвечено зеленым"

        print("Все проверки пройдены успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        # Сделаем скриншот для отладки
        driver.save_screenshot("error.png")
        raise

    finally:
        # Закрытие браузера
        driver.quit()


# Для запуска теста напрямую
if __name__ == "__main__":
    test_form_validation()



