# Импортируем Lock из модуля threading для обеспечения потокобезопасности
from threading import Lock

# Определяем метакласс SingletonBaseClass, унаследованный от type
# Метакласс управляет созданием классов (в данном случае — созданием экземпляров)
class SingletonBaseClass(type):
    # Словарь для хранения единственных экземпляров классов
    _instances = {}
    
    # Блокировка для синхронизации в многопоточной среде
    _lock: Lock = Lock()

    # Переопределяем метод __call__, который вызывается при создании экземпляра класса
    def __call__(cls, *args, **kwargs):
        # Используем контекстный менеджер with для захвата блокировки
        with cls._lock:
            # Проверяем, существует ли уже экземпляр данного класса
            if cls not in cls._instances:
                # Если нет — создаём новый экземпляр через родительский __call__
                instance = super().__call__(*args, **kwargs)
                # Сохраняем его в словаре _instances
                cls._instances[cls] = instance
        # Возвращаем уже существующий или новый (если создан) экземпляр
        return cls._instances[cls]

# Объявляем класс MySingleton, использующий наш метакласс
class MySingleton(metaclass=SingletonBaseClass):
    
    # Конструктор класса, вызывается только при первом создании экземпляра
    def __init__(self):
        self.name = "Singleton"   # Инициализируем имя по умолчанию
        self.value_a = 3          # Значение первого числа
        self.value_b = 5          # Значение второго числа

    # Метод для сложения двух чисел
    def add_a_b(self) -> int:
        return self.value_a + self.value_b

    # Геттер для имени
    def get_name(self) -> str:
        return self.name

    # Сеттер для имени
    def set_name(self, name: str):
        self.name = name

# Точка входа в программу
if __name__ == "__main__":
    # Создаём первый экземпляр
    my_singleton1 = MySingleton()
    
    # Создаём второй экземпляр (должен быть тем же объектом)
    my_singleton2 = MySingleton()
    
    # Выводим имя первого экземпляра
    print("Singleton1 name: " + my_singleton1.get_name())
    
    # Меняем имя через первый экземпляр
    my_singleton1.set_name("New Singleton")
    
    # Выводим имя второго экземпляра — должно быть изменённым
    print("Singleton2 name: " + my_singleton2.get_name())
    
    # Выводим объекты (для наглядности)
    print(my_singleton1)
    print(my_singleton2)
    
    # Сравниваем идентификаторы объектов — должны быть одинаковыми
    print(id(my_singleton1) == id(my_singleton2))