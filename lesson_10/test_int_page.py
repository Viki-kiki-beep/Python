import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from IntPage import IntPage
from MainPage import MainPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации драйвера Selenium.

    :return: webdriver.Chrome, экземпляр драйвера Chrome.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.title("Тест страницы оформления заказа")
@allure.description("Проверка процесса оформления заказа на сайте")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_page(driver):
    """
    Тест для проверки процесса оформления заказа.

    :param driver: webdriver.Chrome, экземпляр драйвера Selenium.
    :return: None
    """
    int_page = IntPage(driver)

    with allure.step("Вход в систему"):
        int_page.do_int()

    # Ждем загрузки главной страницы после входа
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_list"))
    )

    main_page = MainPage(driver)

    with allure.step("Добавление товаров в корзину"):
        main_page.get_shop()

    # Ждем обновления корзины (появление количества товаров)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
    )

    cart_page = CartPage(driver)

    with allure.step("Переход в корзину и оформление заказа"):
        cart_page.shop_cart()

    # Ждем загрузки страницы оформления заказа
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#first-name"))
    )

    checkout_page = CheckoutPage(driver)

    with allure.step("Заполнение данных для оформления заказа"):
        checkout_page.made_cart()

    # Ждем загрузки страницы с итогами
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )

    with allure.step("Проверка общей суммы заказа"):
        total_amount = checkout_page.get_total_amount()
        assert total_amount == 58.29, f"Ожидалось 58.29, но получено {total_amount}"
