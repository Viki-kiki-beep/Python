from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    """
    Класс MainPage представляет главную страницу магазина.
    """

    def __init__(self, driver):
        """
        Инициализация класса MainPage.

        :param driver: WebDriver, экземпляр драйвера Selenium для управления браузером.
        """
        self.driver = driver

    @allure.step("Добавление товара в корзину")
    def add_to_cart(self, product_selector: str) -> None:
        """
        Метод для добавления товара в корзину.

        Находит кнопку добавления товара по селектору и кликает по ней.

        :param product_selector: str, CSS-селектор кнопки добавления товара.
        :return: None
        """
        product_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, product_selector))
        )
        product_button.click()

    @allure.step("Покупка товаров")
    def get_shop(self) -> None:
        """
        Метод для добавления нескольких товаров в корзину и перехода к оформлению заказа.

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

        # Ждем загрузки корзины
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button#checkout"))
        )

        self.driver.find_element(By.CSS_SELECTOR, "button#checkout").click()

        # Ждем загрузки страницы оформления заказа
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input#first-name"))
        )

