def is_valid_date(day, month):
    if month < 1 or month > 12:
        return False
    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    return 1 <= day <= days_in_month[month - 1]

def get_season(day, month):
    if (month == 12 and day >= 1) or (month in [1, 2]):
        return "зима"
    elif month in [3, 4, 5]:
        return "весна"
    elif month in [6, 7, 8]:
        return "лето"
    elif month in [9, 10, 11]:
        return "осень"
    else:
        return None

try:
    day = int(input("Введите день: "))
    month = int(input("Введите месяц (1–12): "))
except ValueError:
    print("Ошибка: введите целые числа для дня и месяца.")
    exit()

if not is_valid_date(day, month):
    print("Ошибка: введена некорректная дата.")
else:
    season = get_season(day, month)
    print(f"Дата {day:02d}.{month:02d} относится к сезону: {season}")