def month_to_season(m):
    if month in range(1, 3) or month == 12:
        return "Зима"
    elif month in range(3, 6):
        return "Весна"
    elif month in range(6, 9):
        return "Лето"
    elif month in range(9, 12):
        return "Осень"
    else:
        return "Введите номер месяца от 1 до 12"


month = int(input("Введите номер месяца"))
print(month_to_season(month))