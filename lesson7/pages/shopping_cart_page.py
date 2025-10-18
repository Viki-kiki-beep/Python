from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def fill_form(self, username, password):
        """Авторизация на сайте"""
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys(username)

        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password")))
        password_field.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()

    def add_products(self):
        """Добавление товаров в корзину"""
        self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()

    def shopping_cart(self):
        """Переход в корзину"""
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_button.click()
        time.sleep(1)

    def checkout(self):
        """Начало оформления заказа"""
        checkout_button = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "checkout")))
        self.driver.execute_script("arguments[0].click();", checkout_button)
        time.sleep(2)

    def your_information(self, first_name, last_name, postal_code):
        """Заполнение информации о покупателе"""
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "first-name")))
        first_name_field.send_keys(first_name)

        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "last-name")))
        last_name_field.send_keys(last_name)

        postal_code_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "postal-code")))
        postal_code_field.send_keys(postal_code)

        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue")))
        continue_button.click()

    def total(self):
        """Получение итоговой суммы заказа"""
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
        return total_element.text
