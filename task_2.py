from smartphone import Smartphone

# Создание списка для хранения экземпляров смартфонов
catalog = [
    Smartphone("Apple", "iPhone 14", "+79001234567"),
    Smartphone("Samsung", "Galaxy S21", "+79007654321"),
    Smartphone("Xiaomi", "Mi 11", "+79009876543"),
    Smartphone("Google", "Pixel 6", "+79005432123"),
    Smartphone("OnePlus", "9 Pro", "+79006789012"),
]

# Печать каталога
for smartphone in catalog:
    print(smartphone)
    