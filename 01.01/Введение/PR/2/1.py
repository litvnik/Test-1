input_str = input("Введите числа через пробел: ")

numbers = list(map(float, input_str.split()))

if not numbers:
    print("Список чисел пуст.")
else:
    total = sum(numbers)
    average = total / len(numbers)
    above_average = [num for num in numbers if num > average]

    print(f"Сумма чисел: {total}")
    print(f"Среднее арифметическое: {average:.2f}")
    print(f"Числа, больше среднего: {above_average}")