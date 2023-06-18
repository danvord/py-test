from smartphone import Smartphone

my_phone = Smartphone("Apple", "iPhone X", "+123456789")

catalog = []
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 11 Pro", "+79123456789"))
catalog.append(Smartphone("Huawei", "P40 Pro", "+79123456789"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79123456789"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79123456789"))

for phone in catalog:
    print(phone.brand + " - " + phone.model + ". " + phone.phone_number)
