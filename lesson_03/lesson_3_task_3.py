from address import Address
from mailing import Mailing

first_mailing = Mailing(Address(659000, "Tokyo", "Lenina", 15, 7),
                        Address(659001, "Paris", "New", 3, 69),
                        50000, "a800f300")

# print(
#     f"Отправление {first_mailing.track} из {first_mailing.from_address.index}, {first_mailing.from_address.city}, {first_mailing.from_address.street}, {first_mailing.from_address.home} - {first_mailing.from_address.room} в {first_mailing.to_address.index}, {first_mailing.to_address.city}, {first_mailing.to_address.street}, {first_mailing.to_address.home} - {first_mailing.to_address.room}. Стоимость {first_mailing.cost} рублей")

print(f"Отправление {first_mailing.track} из {first_mailing.from_address} в {first_mailing.to_address}. Стоимость {first_mailing.cost} рублей")