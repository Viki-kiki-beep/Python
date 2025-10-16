from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import allure

class IntPage:
    """
    Класс IntPage представляет страницу входа в систему.
    """

    def __init__(self, driver):
        """
        Инициализация класса IntPage.

        :param driver: WebDriver, экземпляр драйвера Selenium для управления браузером.
        """
        self.driver = driver
        self.driver.implicitly_wait(15)  # Установка неявного ожидания в 15 секунд
        self.driver.maximize_window()  # Максимизация окна браузера

    @allure.step("Выполнение входа в систему")
    def do_int(self) -> None:
        """
        Метод для выполнения входа в систему.

        Находит поля ввода для имени пользователя и пароля, вводит данные и нажимает кнопку входа.

        :return: None
        """
        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#user-name")
        text_input.send_keys("standard_user")  # Ввод имени пользователя
        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#password")
        text_input.send_keys("secret_sauce")  # Ввод пароля
        self.driver.find_element(By.CSS_SELECTOR, "input#login-button").click()  # Нажатие кнопки входа
