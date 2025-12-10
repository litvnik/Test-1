import math

class Point: # Класс для представления точки на плоскости
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other: 'Point') -> float: #Расстояние между двумя точками
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Segment: # Класс для представления отрезка, заданного двумя точками
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    @property # Вычисление длины отрезка
    def length(self) -> float:
        return self.point1.distance_to(self.point2)

    def __str__(self):
        return f"Segment: {self.point1} — {self.point2}, Length = {self.length:.2f}"

# Демонстрация
print("Задание 1: Создание и вывод объектов класса Отрезок")
# Создаём две точки
p1 = Point(0, 0)
p2 = Point(3, 4)
# Создаём два отрезка
seg1 = Segment(p1, p2)
seg2 = Segment(Point(-1, -1), Point(2, 2))
# Выводим информацию о каждом отрезке
print(seg1)
print(seg2)
# Показываем доступ к полям
print(f"\nДоступ к полям:")
print(f"Точка 1 отрезка 1: {seg1.point1}")
print(f"Точка 2 отрезка 1: {seg1.point2}")
print(f"Длина отрезка 1: {seg1.length}")
# Изменяем координаты одной из точек
seg1.point1.x = 1
seg1.point1.y = 1
print(f"\nПосле изменения Точки 1: {seg1}")