from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_images():
    driver = webdriver.Chrome()
    
    try:
        # Шаг 1: Переходим на страницу
        print("Переходим на страницу...")
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
        
        # Шаг 2: Дожидаемся загрузки всех картинок
        # Ждем когда появится текст "Done!"
        print("Ожидаем загрузки всех картинок...")
        WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
        )
        
        # Шаг 3: Получаем значение атрибута src у 3-й картинки
        third_image = driver.find_element(By.CSS_SELECTOR, "#image-container img:nth-child(3)")
        src_attribute = third_image.get_attribute("src")
        
        # Выводим результат в консоль
        print("SRC третьей картинки:", src_attribute)
        
        return src_attribute
        
    finally:
        # Закрываем браузер
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    result = wait_for_images()