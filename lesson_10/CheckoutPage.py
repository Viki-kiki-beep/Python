from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import re


class CheckoutPage:
    """
    Класс CheckoutPage представляет страницу оформления заказа.
    """

    def __init__(self, driver):
        """
        Инициализация класса CheckoutPage.

        :param driver: WebDriver, экземпляр драйвера Selenium для управления браузером.
        """
        self.driver = driver
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    @allure.step("Заполнение данных для оформления заказа")
    def made_cart(self) -> None:
        """
        Метод для заполнения данных покупателя на странице оформления заказа.

        Вводит имя, фамилию и почтовый код, затем нажимает кнопку продолжения.

        :return: None
        """
        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#first-name")
        text_input.send_keys("Марина")

        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#last-name")
        text_input.send_keys("Игамназарова")

        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#postal-code")
        text_input.send_keys("352680")

        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step("Получение общей суммы заказа")
    def get_total_amount(self) -> float:
        """
        Метод для получения общей суммы заказа.

        Находит элемент с общей суммой и возвращает его значение.

        :return: float, общая сумма заказа или None в случае ошибки.
        """
        try:
            # Ждем пока элемент станет видимым
            total_cost_element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
            )

            # Получаем текст
            total_cost_text = total_cost_element.text
            print(f"Текст элемента суммы: '{total_cost_text}'")

            # Извлекаем число
            if "Total: $" in total_cost_text:
                total_cost_value = float(total_cost_text.replace("Total: $", ""))
            else:
                # Ищем число с плавающей точкой
                numbers = re.findall(r"\d+\.\d+", total_cost_text)
                if numbers:
                    total_cost_value = float(numbers[0])
                else:
                    raise ValueError(f"Не удалось извлечь сумму из текста: {total_cost_text}")

            return total_cost_value

        except Exception as e:
            print(f"An error occurred while retrieving the total amount: {e}")
            return None
