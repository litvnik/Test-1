from abc import ABC, abstractmethod

# Абстрактный класс "Транспорт"
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        # Запуск двигателя
        pass

    @abstractmethod
    def stop_engine(self):
        # Остановка двигателя
        pass

    @abstractmethod
    def move(self):
        # Движение транспорта
        pass

class Car(Vehicle): # Конкретный класс: Автомобиль
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"Автомобиль {self.brand} {self.model}: двигатель запущен")

    def stop_engine(self):
        print(f"Автомобиль {self.brand} {self.model}: двигатель остановлен")

    def move(self):
        print(f"Автомобиль {self.brand} {self.model}: едет по дороге")

class Bicycle(Vehicle): # Конкретный класс: Велосипед
    def __init__(self, bike_type: str):
        self.bike_type = bike_type

    def start_engine(self):
        # Велосипед не имеет двигателя, но по условию задачи
        # метод обязан быть реализован — делаем логичную заглушку.
        print(f"Велосипед ({self.bike_type}): не имеет двигателя — педалируем")

    def stop_engine(self):
        print(f"Велосипед ({self.bike_type}): не имеет двигателя — просто остановились")

    def move(self):
        print(f"Велосипед ({self.bike_type}): движется по тропинке")
        
class Airplane(Vehicle): # Конкретный класс: Самолет
    def __init__(self, passenger_count: int):
        self.passenger_count = passenger_count

    def start_engine(self):
        print(f"Самолёт с {self.passenger_count} пассажирами: двигатели запущены")

    def stop_engine(self):
        print(f"Самолёт с {self.passenger_count} пассажирами: двигатели остановлены")

    def move(self):
        print(f"Самолёт с {self.passenger_count} пассажирами: набирает скорость для взлёта")


# Основа
if __name__ == "__main__": # Создаём объекты каждого типа транспорта
    my_car = Car("Toyota", "Corolla")
    my_bike = Bicycle("Горный")
    my_plane = Airplane(200)

    # Демонстрация методов
    print("Демонстрация работы автомобиля")
    my_car.start_engine()
    my_car.move()
    my_car.stop_engine()

    print("\nДемонстрация работы велосипеда")
    my_bike.start_engine()
    my_bike.move()
    my_bike.stop_engine()

    print("\nДемонстрация работы самолёта")
    my_plane.start_engine()
    my_plane.move()
    my_plane.stop_engine()