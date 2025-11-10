in_str = input("Введите строку: ")

ws = in_str.split()

if not ws:
    print("Количество слов: 0")
    print("Самое длинное слово: нет слов")
    print("Самое короткое слово: нет слов")
else:
    w_c = len(ws)
    long_w = max(ws, key=len)
    short_w = min(ws, key=len)
    print(f"Количество слов: {w_c}")
    print(f"Самое длинное слово: {long_w}")
    print(f"Самое короткое слово: {short_w}")