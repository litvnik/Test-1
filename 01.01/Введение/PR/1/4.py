try:
    n = int(input("Введите количество записей: "))
    if n < 0:
        print("Количество записей не может быть отрицательным.")
        exit()
except ValueError:
    print("Ошибка: введите целое число.")
    exit()

phone_book = {}

for i in range(n):
    try:
        entry = input(f"Введите запись {i + 1} (имя и номер через пробел): ").strip()
        parts = entry.split()
        if len(parts) < 2:
            print(f"Ошибка: запись '{entry}' пропущена — требуется имя и номер.")
            continue
        name = parts[0]
        number = parts[-1]  # берём последнее слово как номер
        phone_book[name] = number
    except Exception:
        print("Произошла ошибка при вводе записи. Запись пропущена.")

query_name = input("Введите имя для поиска: ").strip()  # Запрос имени для поиска

if query_name in phone_book:  # Поиск в телефонной книге
    print(phone_book[query_name])
else:
    print("Контакт не найден")