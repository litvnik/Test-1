input_str = input("Введите числа через пробел: ")

try:
    numbers = list(map(float, input_str.split()))
except ValueError:
    print("Ошибка: введите только числа, разделённые пробелами.")
    exit()
unique_numbers = list(dict.fromkeys(numbers)) # Удаляем дубликаты (с помощью преобразования в dict)
unique_numbers.sort() # Сортируем список по возрастанию
print("Результат:", unique_numbers)