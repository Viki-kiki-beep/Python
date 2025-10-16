from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    def your_information(self, first_name, last_name, postal_code):
        time.sleep(1)
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "first-name")))
        first_name_field.send_keys(first_name)

        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "last-name")))
        last_name_field.send_keys(last_name)

        postal_code_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "postal-code")))
        postal_code_field.send_keys(postal_code)

        continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "continue")))
        continue_button.click()

