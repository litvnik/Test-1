say_hello = lambda: print("Привет, мир!") # Лямбда без параметров
add = lambda x, y: x + y # Лямбда с двумя параметрами
square = lambda n: n ** 2 # Лямбда для возведения числа в квадрат
is_even = lambda num: num % 2 == 0 # Лямбда для проверки является ли число чётным
join_strings = lambda s1, s2: s1 + " " + s2 # Лямбда для конкатенации двух строк с пробелом

# Выполнение выражений
print("1. Вызов say_hello():")
say_hello()

print("\n2. Сумма 3 и 7:", add(3, 7))
print("\n3. Квадрат числа 5:", square(5))
print("\n4. Чётное ли число 8?", is_even(8))
print("   Чётное ли число 7?", is_even(7))
print("\n5. Объединение строк:", join_strings("Привет", "студент!"))