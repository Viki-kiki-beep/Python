from address import Address
from mailing import Mailing

# Создание экземпляров класса Address
to_address = Address("123456", "Москва", "Ленина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "15", "3")

# Создание экземпляра класса Mailing
mailing = Mailing(to_address, from_address, 250, "TRK123456")

# Печать информации об отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, "
      f"{mailing.from_address.street}, "
      f"{mailing.from_address.house} - "
      f"{mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, "
      f"{mailing.to_address.city}, "
      f"{mailing.to_address.street}, "
      f"{mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")