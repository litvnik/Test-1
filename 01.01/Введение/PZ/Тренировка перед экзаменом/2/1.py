# 1. Консольный ввод/вывод в Python
name = input("Как тебя зовут? ")  # ввод
print("Привет,", name)            # вывод

# 2. Условия
if x > 0:
    print("Положительное")
else:
    print("Не положительное")

# 3. Циклы
i = 0
while i < 3:
    i += 1

for item in [1, 2, 3]:
    print(item)
    
# 4. Коллекции и проход циклом по коллекции
nums = [10, 20, 30]
for n in nums:
    print(n)

data = {"a": 1, "b": 2}
for k, v in data.items():
    print(k, v)

# 5. Создание классов
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print("Мяу!")

# 6. Наследование
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Гав!")

# 7. Полиморфизм
class Cat(Animal):
    def speak(self): return "Мяу"
class Dog(Animal):
    def speak(self): return "Гав"

for pet in [Cat("Мурка"), Dog("Шарик")]:
    print(pet.speak())

# 8. Лямбда-функции
double = lambda x: x * 2
nums = [1, 2, 3]
squares = list(map(lambda x: x**2, nums))

# 9. Абстрактные классы и абстрактные методы
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def area(self):
        return self.side ** 2