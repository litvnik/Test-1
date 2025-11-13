class Fraction:
    def __init__(self, first=1, second=1):
        self.first = first
        self.second = second
        
    def read(self): # Метод для ввода значений с клавиатуры
        while True:
            try:
                self.first = int(input("Введите числитель (целое положительное число): "))
                self.second = int(input("Введите знаменатель (целое положительное число): "))

                if self.first <= 0 or self.second <= 0:
                    print("Ошибка: Числитель и знаменатель должны быть положительными!")
                    continue
                break  # Выход из цикла, если всё введено правильно
            except ValueError:
                print("Ошибка")

    def display(self): # Метод для вывода значений полей на экран
        print(f"Дробь: {self.first} / {self.second}")

    def ipart(self): # Метод для выделения целой части дроби
        if self.second == 0:
            print("Ошибка: Знаменатель не может быть равен нулю!")
            return None
        return self.first // self.second  # Целочисленное деление

    def get_fraction_value(self): # Возвращает значение дроби как float
        calculate = lambda x, y: x / y
        if self.second != 0:
            return calculate(self.first, self.second)
        else:
            return None

    def is_proper(self):
        # Проверяет, является ли дробь правильной: числитель < знаменатель
        check = lambda x, y: x < y
        return check(self.first, self.second)

# Пример
if __name__ == "__main__":
    # Создаем объект через конструктор
    frac = Fraction(7, 3)
    print("Объект создан через конструктор:")
    frac.display()
    print(f"Целая часть: {frac.ipart()}")
    print(f"Значение дроби: {frac.get_fraction_value():.2f}")
    print(f"Правильная дробь? {frac.is_proper()}\n")

    # Вводим новые значения с клавиатуры
    print("Ввод новых значений:")
    frac.read()
    frac.display()
    print(f"Целая часть: {frac.ipart()}")
    print(f"Значение дроби: {frac.get_fraction_value():.2f}")
    print(f"Правильная дробь? {frac.is_proper()}\n")

    # Пример с нулевым знаменателем (проверка)
    print("Проверка на нулевой знаменатель:")
    frac_zero = Fraction(5, 0)
    frac_zero.display()
    frac_zero.ipart()  # Должна быть ошибка