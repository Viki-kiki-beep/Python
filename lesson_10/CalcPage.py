from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalcPage:
    """
    Класс для представления страницы калькулятора.

    Attributes:
        url (str): URL страницы калькулятора.
        driver (webdriver): Экземпляр веб-драйвера для взаимодействия с браузером.
        wait (WebDriverWait): Объект для ожидания элементов на странице.
    """

    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        """
        Инициализация класса CalcPage.

        Args:
            driver (webdriver): Экземпляр веб-драйвера для взаимодействия с браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Увеличено время ожидания

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        Returns:
            None
        """
        self.driver.get(self.url)

    @allure.step("Ввод задержки в калькулятор")
    def do_calc(self) -> None:
        """
        Выполняет расчет на странице калькулятора, вводя задержку.

        Returns:
            None
        """
        text_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        text_input.clear()
        text_input.send_keys("5")

    @allure.step("Прокрутка страницы вниз")
    def scroll_down(self) -> None:
        """
        Прокручивает страницу вниз.

        Returns:
            None
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Выполнение арифметической операции")
    def perform_element(self) -> None:
        """
        Выполняет арифметическую операцию на калькуляторе.

        Returns:
            None
        """
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    @allure.step("Ожидание результата")
    def wait_for_result(self) -> None:
        """
        Ожидает появления результата на странице.

        Returns:
            None
        """
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    @allure.step("Получение результата")
    def get_result(self) -> str:
        """
        Получает результат расчета.

        Returns:
            str: Результат расчета в виде строки.
        """
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result.text
