chui, talas, osh, djalal_abad, naryn, batken, issyk_kul = float(input("Введите температуру в Чуйской области: ")), \
                         float(input("Введите температуру в Талаской области: ")), \
                         float(input("Введите температуру в Ошской области: ")), \
                         float(input("Введите температуру в Джалал-Абадской области: ")),\
                         float(input("Введите температуру в Нарынской области: ")),\
                         float(input("Введите температуру в Баткенской области: ")), \
                         float(input("Введите температуру в Иссык-Кулской области: "))

average_temperature = round((chui + talas + osh + djalal_abad + naryn + batken + issyk_kul) / 7, 1)

print(f"Средний показатель температуры воздуха по КР на сегодня: {average_temperature}°C.")