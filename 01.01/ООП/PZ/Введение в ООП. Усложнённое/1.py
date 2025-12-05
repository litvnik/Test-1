class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def _clamp(self, value):
        return max(0, min(100, value))

    def feed(self):
        self.hunger = self._clamp(self.hunger + 20)
        self.energy = self._clamp(self.energy - 10)
        self._check_alive()

    def play(self):
        self.happiness = self._clamp(self.happiness + 15)
        self.hunger = self._clamp(self.hunger - 10)
        self._check_alive()

    def sleep(self):
        self.energy = self._clamp(self.energy + 25)
        self.happiness = self._clamp(self.happiness - 10)
        self._check_alive()

    def _check_alive(self):
        zero_count = sum(attr == 0 for attr in [self.hunger, self.happiness, self.energy])
        if zero_count >= 2:
            print(f"{self.name} умер... 😢")
            exit()  # завершаем программу

    def status(self):
        print(f"\n--- Состояние {self.name} ---")
        print(f"Сытость:     {self.hunger}")
        print(f"Счастье:     {self.happiness}")
        print(f"Энергия:     {self.energy}")
        print("-" * 30)

    def __str__(self):
        return f"Питомец {self.name}: сытость={self.hunger}, счастье={self.happiness}, энергия={self.energy}"

class Dog(Pet):
    def play(self):
        self.happiness = self._clamp(self.happiness + 25)
        self.hunger = self._clamp(self.hunger - 15)
        self._check_alive()

class Cat(Pet):
    def play(self):
        self.happiness = self._clamp(self.happiness + 10)
        self.hunger = self._clamp(self.hunger - 5)
        self._check_alive()

    def sleep(self):
        self.energy = self._clamp(self.energy + 30)
        self.happiness = self._clamp(self.happiness - 3)
        self._check_alive()

if __name__ == "__main__":
    pet_type = input("Выберите питомца: (1) Собака, (2) Кот: ")
    name = input("Введите имя питомца: ")

    if pet_type == "1":
        pet = Dog(name)
    elif pet_type == "2":
        pet = Cat(name)
    else:
        pet = Pet(name)  # общий питомец по дефолту

    print(f"\nДобро пожаловать, {pet.name}!")

    while True:
        pet.status()
        print("\nЧто вы хотите сделать?")
        print("1. Покормить")
        print("2. Поиграть")
        print("3. Поспать")
        print("4. Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Попробуйте снова")