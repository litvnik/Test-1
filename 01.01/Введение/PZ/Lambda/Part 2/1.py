class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        """Возвращает средний балл студента."""
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        return f"Student(name='{self.name}', grades={self.grades})"

# Создаём список из 5 студентов
students = [
    Student("Анастасия", [5, 4, 5, 4, 5]),
    Student("Егор", [3, 4, 2, 3, 4]),
    Student("Елизавета", [4, 4, 4, 5, 5]),
    Student("Александр", [2, 3, 2, 3, 2]),
    Student("Иван", [5, 5, 5, 5, 5])
]

# Получаем список средних баллов с помощью map и lambda
average_grades = list(map(lambda s: s.average_grade(), students))
print("Средние баллы всех студентов:", [round(g, 2) for g in average_grades])

# Отбираем студентов со средним баллом выше 4
high_achievers = list(filter(lambda s: s.average_grade() > 4, students))

print("\nСтуденты со средним баллом выше 4:")
for student in high_achievers:
    print(f"  {student.name}: {round(student.average_grade(), 2)}")

# Сортируем всех студентов по среднему баллу по убыванию
sorted_students = sorted(students, key=lambda s: s.average_grade(), reverse=True)

# Выводим имя и средний балл всех студентов (по убыванию — "лучшие" первыми)
print("\nЛучшие студенты (по убыванию среднего балла):")
for student in sorted_students:
    print(f"  {student.name}: {round(student.average_grade(), 2)}")