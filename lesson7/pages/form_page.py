from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, data):
        for field_name, value in data.items():
            self.driver.find_element(By.NAME, field_name).send_keys(value)

    def submit_form(self):
        submit_button = (By.CSS_SELECTOR, "button[type='submit']")
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(submit_button))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_zip_code(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "zip-code")))

    def get_zip_code_color(self):
        zip_code = self.driver.find_element(By.ID, "zip-code")
        return zip_code.value_of_css_property("background-color")

    def get_field_color(self, field_name):
        field = self.driver.find_element(By.CSS_SELECTOR, f"[id='{field_name}']")
        return field.value_of_css_property("background-color")

