from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CartPage:
    """
    Класс CartPage представляет страницу корзины покупок.
    """

    def __init__(self, driver):
        """
        Инициализация класса CartPage.

        :param driver: WebDriver, экземпляр драйвера Selenium для управления браузером.
        """
        self.driver = driver
        self.driver.implicitly_wait(15)  # Установка неявного ожидания в 15 секунд
        self.driver.maximize_window()  # Максимизация окна браузера

    @allure.step("Переход в корзину и оформление заказа")
    def shop_cart(self) -> None:
        """
        Метод для перехода в корзину и оформления заказа.

        Находит ссылку на корзину и кнопку оформления заказа, затем кликает по ним.

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()  # Переход в корзину
        self.driver.find_element(By.CSS_SELECTOR, "button#checkout").click()  # Нажатие кнопки оформления заказа
        