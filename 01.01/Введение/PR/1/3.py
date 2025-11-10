numbers = []
while True:
    try:
        num = float(input("Введите число (0 для завершения): "))
    except ValueError:
        print("Пожалуйста, введите корректное число.")
        continue

    if num == 0:
        break
    numbers.append(num)

if numbers:
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Сумма всех введённых чисел: {total}")
    print(f"Среднее арифметическое (без учёта 0): {average}")
else:
    print("Сумма всех введённых чисел: 0")
    print("Среднее арифметическое (без учёта 0): не определено (нет введённых чисел)")