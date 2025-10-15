from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)  # Увеличено время ожидания

    try:
        driver.get("https://www.saucedemo.com/")

        # Ожидаем загрузку формы авторизации
        wait.until(EC.presence_of_element_located((By.ID, "user-name")))

        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Ожидаем загрузку страницы товаров
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

        # Добавление товаров в корзину
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Ожидаем загрузку корзины
        wait.until(EC.presence_of_element_located((By.ID, "checkout"))).click()

        # Ожидаем загрузку формы
        wait.until(EC.presence_of_element_located((By.ID, "first-name")))

        # Заполнение формы (исправлены ID полей)
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("12345")

        # Продолжение покупки
        driver.find_element(By.ID, "continue").click()

        # Ожидаем загрузку страницы подтверждения
        wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

        # Проверка успешного оформления
        success_message = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        assert "THANK YOU FOR YOUR ORDER" in success_message.text.upper()

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        # Можно добавить скриншот для отладки
        driver.save_screenshot("error_screenshot.png")
        raise

    finally:
        driver.quit()

