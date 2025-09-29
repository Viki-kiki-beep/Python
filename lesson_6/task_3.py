from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

# Переход на страницу
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ожидание загрузки третьего изображения
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//img[3]"))
)

# Получение всех изображений
images = driver.find_elements(By.TAG_NAME, "img")

# Вывод количества загруженных изображений
print(f"Количество загруженных изображений: {len(images)}")

# Проверка, что есть как минимум три изображения
if len(images) >= 3:
    third_image_src = images[2].get_attribute("src")
    print(third_image_src)
else:
    print("Недостаточно изображений на странице.")

# Закрытие драйвера
driver.quit()
