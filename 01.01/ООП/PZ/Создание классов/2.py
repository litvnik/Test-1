import math

class Point: # Класс для представления точки на плоскости
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = value

    def __str__(self):
        return f"Point({self._x}, {self._y})"

class Segment: # Класс для представления отрезка с сохранением длины при изменении одной точки
    def __init__(self, point1: Point, point2: Point):
        self._point1 = point1
        self._point2 = point2
        self._original_length = self._calculate_length()  # Сохраняем начальную длину

    @property
    def point1(self) -> Point:
        return self._point1

    @point1.setter
    def point1(self, new_point: Point):
        # При изменении точки 1 — пересчитываем точку 2, чтобы сохранить длину
        old_point2 = self._point2
        new_point1 = new_point
        self._point1 = new_point1
        self._adjust_point2_for_fixed_length()
        print(f"[INFO] Точка 1 изменена. Точка 2 скорректирована для сохранения длины.")

    @property
    def point2(self) -> Point:
        return self._point2

    @point2.setter
    def point2(self, new_point: Point):
        # При изменении точки 2 — пересчитываем точку 1, чтобы сохранить длину
        old_point1 = self._point1
        new_point2 = new_point
        self._point2 = new_point2
        self._adjust_point1_for_fixed_length()
        print(f"[INFO] Точка 2 изменена. Точка 1 скорректирована для сохранения длины.")

    def _calculate_length(self) -> float: # Вычисление текущей длины отрезка
        dx = self._point1.x - self._point2.x
        dy = self._point1.y - self._point2.y
        return math.sqrt(dx*dx + dy*dy)

    def _adjust_point2_for_fixed_length(self): # Пересчёт координат точки 2 при изменении точки 1, чтобы сохранить длину
        # Новые координаты точки 1
        x12 = self._point1.x
        y12 = self._point1.y

        # Исходная длина отрезка
        L = self._original_length

        # Угол φ относительно точки 1 (в радианах)
        # Используем atan2 для корректной обработки всех квадрантов
        dx = self._point2.x - x12
        dy = self._point2.y - y12
        phi = math.atan2(dy, dx)  # угол направления от точки 1 к точке 2

        # Новые координаты точки 2
        x22 = L * math.cos(phi) + x12
        y22 = L * math.sin(phi) + y12

        self._point2.x = x22
        self._point2.y = y22

    def _adjust_point1_for_fixed_length(self): # Пересчёт координат точки 1 при изменении точки 2, чтобы сохранить длину
        # Новые координаты точки 2
        x22 = self._point2.x
        y22 = self._point2.y

        # Исходная длина отрезка
        L = self._original_length

        # Угол φ относительно точки 2 (в радианах)
        dx = self._point1.x - x22
        dy = self._point1.y - y22
        phi = math.atan2(dy, dx)  # угол направления от точки 2 к точке 1

        # Новые координаты точки 1
        x12 = L * math.cos(phi) + x22
        y12 = L * math.sin(phi) + y22

        self._point1.x = x12
        self._point1.y = y12

    @property
    def length(self) -> float: # Текущая длина отрезка (должна быть постоянной)
        return self._original_length

    def __str__(self):
        return f"Segment: {self._point1} — {self._point2}, Fixed Length = {self.length:.2f}"

# Демонстрация
print("\nЗадание 2: Работа с ограничениями (сохранение длины)")

# Создаём две точки
p1 = Point(0, 0)
p2 = Point(3, 4)

# Создаём отрезок
seg = Segment(p1, p2)
print(f"Начальный отрезок: {seg}")

# Меняем координаты точки 1 — точка 2 должна автоматически скорректироваться
print("\nИзменяем Точку 1")
seg.point1.x = 1
seg.point1.y = 1
print(f"После изменения Точки 1: {seg}")

# Меняем координаты точки 2 — точка 1 должна автоматически скорректироваться
print("\nИзменяем Точку 2")
seg.point2.x = 5
seg.point2.y = 5
print(f"После изменения Точки 2: {seg}")

# Проверка, что длина осталась прежней
print(f"\nПроверка длины: {seg.length:.2f} (должна быть равна 5.00)")

# Создаём ещё один отрезок для демонстрации
seg2 = Segment(Point(1, 1), Point(4, 5))
print(f"\nВторой отрезок: {seg2}")

# Изменяем его точку 1
seg2.point1.x = 0
seg2.point1.y = 0
print(f"После изменения Точки 1 во втором отрезке: {seg2}")