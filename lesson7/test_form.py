from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.form_page import FormPage


def test_form_submission():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_page = FormPage(driver)

    data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "zip-code": "",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    form_page.fill_form(data)
    form_page.submit_form()
    form_page.wait_for_zip_code()

    alert_danger_color = "rgba(248, 215, 218, 1)"
    color_zip = form_page.get_zip_code_color()
    assert color_zip == alert_danger_color, f"Ожидался цвет {alert_danger_color}, но получен {color_zip}"

    alert_success_color = "rgba(209, 231, 221, 1)"
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field_name in fields:
        field_color = form_page.get_field_color(field_name)
        assert field_color == alert_success_color, f"Ожидался цвет {
        alert_success_color} для {field_name}, но получен {field_color}"

    driver.quit()

