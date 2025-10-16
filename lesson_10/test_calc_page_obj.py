import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CalcPage import CalcPage
import allure

@pytest.fixture
def driver():
    """
    Фикстура для инициализации веб-драйвера.

    Returns:
        webdriver: Экземпляр веб-драйвера.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Тестирование калькулятора")
@allure.description("Проверка функциональности калькулятора с использованием Selenium и Allure.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calc(driver):
    """
    Тест для проверки функциональности калькулятора.

    Args:
        driver (webdriver): Экземпляр веб-драйвера.

    Returns:
        None
    """
    with allure.step("Открытие страницы калькулятора"):
        calc_page = CalcPage(driver)
        calc_page.open()

    with allure.step("Выполнение расчета"):
        calc_page.do_calc()

    # Ждем пока поле задержки станет доступным
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay"))
    )

    with allure.step("Прокрутка страницы вниз"):
        calc_page.scroll_down()

    with allure.step("Выполнение арифметической операции"):
        calc_page.perform_element()

    with allure.step("Ожидание результата расчета"):
        calc_page.wait_for_result()

    with allure.step("Проверка результата"):
        result = calc_page.get_result()
        assert result == "15", f"Ожидался результат 15, но получено {result}"

