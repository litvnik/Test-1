# Базовый класс: Экспонат (Exhibit)
class Exhibit:
    def __init__(self, name, year, author, country, value): # Конструктор класса Exhibit. Все поля приватные — инкапсуляция.
        self.__name = name # Название экспоната
        self.__year = year # Год создания
        self.__author = author # Автор
        self.__country = country # Страна происхождения
        self.__value = value # Стоимость

    def get_name(self): # Геттеры
        return self.__name

    def get_year(self):
        return self.__year

    def get_author(self):
        return self.__author

    def get_country(self):
        return self.__country

    def get_value(self):
        return self.__value

    # Сеттеры с валидацией
    def set_name(self, name):
        if isinstance(name, str) and name.strip():
            self.__name = name
        else:
            raise ValueError("Название должно быть непустой строкой")

    def set_year(self, year):
        if isinstance(year, int) and 0 < year <= 2025:
            self.__year = year
        else:
            raise ValueError("Год должен быть целым числом в диапазоне 1–2025")

    def set_author(self, author):
        if isinstance(author, str) and author.strip():
            self.__author = author
        else:
            raise ValueError("Автор должен быть непустой строкой")

    def set_country(self, country):
        if isinstance(country, str) and country.strip():
            self.__country = country
        else:
            raise ValueError("Страна должна быть непустой строкой")

    def set_value(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__value = value
        else:
            raise ValueError("Стоимость должна быть неотрицательным числом")

    def display_info(self): # Метод без параметров — отображение базовой информации
        print(f"Экспонат: {self.__name}")
        print(f"Год: {self.__year}")
        print(f"Автор: {self.__author}")
        print(f"Страна: {self.__country}")
        print(f"Стоимость: ${self.__value:,.2f}")

    def is_more_expensive_than(self, other_value): # Метод с входным параметром — сравнение по стоимости
        return self.__value > other_value
    
    def historical_significance(self, curator_notes): # Метод с входным и выходным параметром — оценка исторической значимости, возвращает комментарий куратора + оценку по году создания
        if self.__year < 1800:
            era = "античность или средневековье"
        elif self.__year < 1900:
            era = "XIX век"
        else:
            era = "современность"
        return f"{curator_notes}. Экспонат относится к эпохе: {era}."

# Дочерний класс: Картина (Painting)
class Painting(Exhibit):
    def __init__(self, name, year, author, country, value, technique): # Конструктор дочернего класса Painting. Вызывает конструктор родителя и добавляет специфичное поле
        super().__init__(name, year, author, country, value)
        self.__technique = technique  # Техника исполнения

    def get_technique(self): # Геттер и сеттер для техники
        return self.__technique

    def set_technique(self, technique):
        if isinstance(technique, str) and technique.strip():
            self.__technique = technique
        else:
            raise ValueError("Техника должна быть непустой строкой")

    def display_info(self): # Переопределение метода display_info — полиморфизм
        super().display_info()
        print(f"Техника: {self.__technique}")

    def is_oil_painting(self): # Специфичный метод для картин
        return "масло" in self.__technique.lower()

if __name__ == "__main__": # Демонстрация работы
    # Создание двух экспонатов
    exhibit1 = Exhibit(
        name="Древняя ваза",
        year=450,
        author="Неизвестен",
        country="Греция",
        value=120000.0
    )

    painting1 = Painting(
        name="Звёздная ночь",
        year=1889,
        author="Винсент ван Гог",
        country="Нидерланды",
        value=100000000.0,
        technique="Масло на холсте"
    )

    print("Экспонат 1") # Вывод информации
    exhibit1.display_info()
    print("\nЗначимость:", exhibit1.historical_significance("Редкий образец античной керамики"))

    print("\nКартина 1")
    painting1.display_info()
    print("\nЯвляется масляной?", painting1.is_oil_painting())
    print("Дороже 50 млн$?", painting1.is_more_expensive_than(50_000_000))

    # Пример изменения через сеттер
    painting1.set_technique("Масляная живопись")
    print("\nОбновлённая техника:", painting1.get_technique())