from address import Address 
from mailing import Mailing 
 
to_address = Address("123456", "Москва", "Невский проспект", "1", "10") 
from_address = Address("654321", "Санкт-Петербург", "Тверская улица", "2", "20") 
 
my_mailing = Mailing(to_address, from_address, 500, "123abc") 
 
print(f"Отправление {my_mailing.track} из {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment} в {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment}. Стоимость {my_mailing.cost} рублей.")