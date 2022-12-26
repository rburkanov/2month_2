
date = int(input("Введите день рождения:"))
month = int(input("Введите месяц рождения:"))

if (21 <= date <= 31 and month == 3) or (month == 4 and 1 <= date <= 19):
    print("Знак зодиака:Овен")

elif (20 <= date <= 30 and month == 4) or (month == 5 and 1 <= date <= 20):
    print("Знак зодиака:Телец")

elif (21 <= date <= 31 and month == 5) or (month == 6 and 1 <= date <= 21):
    print("Знак зодиака:Близнецы")

elif (22 <= date <= 30 and month == 6) or (month == 7 and 1 <= date <= 22):
    print("Знак зодиака:Рак")

elif (23 <= date <= 31 and month == 7) or (month == 8 and 1 <= date <= 22):
    print("Знак зодиака:Лев")

elif (23 <= date <= 31 and month == 8) or (month == 9 and 1 <= date <= 22):
    print("Знак зодиака:Дева")

elif (23 <= date <= 30 and month == 9) or (month == 10 and 1 <= date <= 23):
    print("Знак зодиака:Весы")

elif (24 <= date <= 31 and month == 10) or (month == 11 and 1 <= date <= 22):
    print("Знак зодиака:Скорпион")

elif (23 <= date <= 30 and month == 11) or (month == 12 and 1 <= date <= 21):
    print("Знак зодиака:Стрелец")

elif (22 <= date <= 31 and month == 12) or (month == 1 and 1 <= date <= 20):
    print("Знак зодиака:Козерог")

elif (21 <= date <= 31 and month == 1) or (month == 2 and 1 <= date <= 18):
    print("Знак зодиака:Водолей")

elif (19 <= date <= 29 and month == 2) or (month == 3 and 1 <= date <= 20):
    print("Знак зодиака:Рыбы")
else:
    print('Вы ввели дату не правильным образом ')