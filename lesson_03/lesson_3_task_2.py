from smartphone import Smartphone

catalog = [Smartphone("Samsung", "First", "+79995551111"),
           Smartphone("Apple", "Second", "+79995551112"),
           Smartphone("Fly", "By", "+79995551113"),
           Smartphone("Siemens", "A-62", "+79995551114"),
           Smartphone("Honor", "50", "+79995551115")]

for i in catalog:
    print(f"{i.brand} - {i.model}. {i.number}")
