from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage

def test_02_calc():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator_page = CalculatorPage(driver)

    calculator_page.set_delay("45")

    calculator_page.click_button()

    result = calculator_page.get_result("15")
    assert result == "15"

    driver.quit()
    