# Автопарк - контроль транспортных средств и их состояния.
class Auto: # Базовый класс для всех авто
    def __init__(self, brand, condition):
        self.brand = brand
        self.condition = condition  # Состояние: хорошее, среднее, плохое
    def display_info(self): # Инфо об авто
        print(f"Марка: {self.brand}, Состояние: {self.condition}")
    def update_condition(self, new_condition): # Обновление состояние авто
        self.condition = new_condition
        print(f"Состояние {self.brand} обновлено на: {self.condition}")

class Truck(Auto): # Класс для грузовиков (наследование)
    def __init__(self, brand, condition, cargo_capacity):
        super().__init__(brand, condition)
        self.cargo_capacity = cargo_capacity  # Грузоподъемность в тоннах
    def display_info(self): # полиморфизм
        print(f"Грузовик: {self.brand}, Состояние: {self.condition}, Грузоподъемность: {self.cargo_capacity} т")

class Car(Auto): # Класс легковых автомобилей (наследование)
    def __init__(self, brand, condition, passenger_seats):
        super().__init__(brand, condition)
        self.passenger_seats = passenger_seats  # Количество пассажирских мест
    def display_info(self): # полиморфизм
        print(f"Легковой автомобиль: {self.brand}, Состояние: {self.condition}, Мест: {self.passenger_seats}")

automobiles = [] # Коллекция автомобилей

def add_auto(): # Добавление автомобилей в парк
    print("\n--- Добавление авто ---")
    auto_type = input("Тип авто (1 - Легковое, 2 - Грузовик): ")
    brand = input("Марку автоя: ")
    condition = input("Состояние авто (хорошее, среднее, плохое): ")
    
    if auto_type == "1":
        seats = int(input("Введите количество пассажирских мест: "))
        new_auto = Car(brand, condition, seats)
    elif auto_type == "2":
        capacity = float(input("Грузоподъемность (в тоннах): "))
        new_auto = Truck(brand, condition, capacity)
    else:
        print("Нет такого типа, ну типа")
        return
    automobiles.append(new_auto)
    print(f"Авто {brand} добавлено в парк")

def show_all_autos(): # Отображение всех авто в парке
    print("\n--- Список всего авто в парке ---")
    if len(automobiles) == 0:
        print("Автопарк пуст!")
        return
    for i, auto in enumerate(automobiles, 1):
        print(f"{i}. ", end="")
        auto.display_info()

def update_auto_condition(): # Обновление состояние авто
    print("\n--- Обновление состояния авто ---")
    show_all_autos()
    
    if len(automobiles) == 0:
        return
    index = int(input("Номер авто для обновления: ")) - 1
    if 0 <= index < len(automobiles):
        new_condition = input("Введите новое состояние (хорошее, среднее, плохое): ")
        automobiles[index].update_condition(new_condition)
    else:
        print("Неверный номер автомобиля!")

def remove_auto(): # Удаление авто из парка
    print("\n--- Удаление авто ---")
    show_all_autos()
    
    if len(automobiles) == 0:
        return
    index = int(input("Номер авто для удаления: ")) - 1
    if 0 <= index < len(automobiles):
        removed_auto = automobiles.pop(index)
        print(f"Автомобиль {removed_auto.brand} удалён из автопарка")
    else:
        print("Неверный номер авто")

while True:
    print("\n           УПРАВЛЕНИЕ АВТОПАРКОМ")
    print("1. Добавить автомобиль")
    print("2. Показать все автомобили")
    print("3. Обновить состояние автомобиля")
    print("4. Удалить автомобиль")
    print("0. Выход")
    
    choice = input("Выберите действие (0-4): ")
    
    if choice == "1":
        add_auto()
    elif choice == "2":
        show_all_autos()
    elif choice == "3":
        update_auto_condition()
    elif choice == "4":
        remove_auto()
    elif choice == "0":
        break
    else:
        print("Выберите правильное действие")