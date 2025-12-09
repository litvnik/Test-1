# 1: Опишите класс Player с атрибутами nickname и level.
# Создайте несколько объектов и выведите их данные в консоль.

class Player:
    def __init__(self, nickname: str, level: int):
        self.nickname = nickname
        self.level = level

    def __str__(self):
        return f"Player(nickname='{self.nickname}', level={self.level})"

# Создание объектов и вывод данных
player1 = Player("Alice", 5)
player2 = Player("Bob", 3)
print("=== Задание 1 ===")
print(player1)
print(player2)

# 2: Добавьте в Player метод level_up(), который увеличивает уровень игрока на 1.
# Продемонстрируйте работу метода.

class Player:
    def __init__(self, nickname: str, level: int):
        self.nickname = nickname
        self.level = level

    def level_up(self):
        self.level += 1

    def __str__(self):
        return f"Player(nickname='{self.nickname}', level={self.level})"

# Демонстрация level_up
player1 = Player("Alice", 5)
print("\n=== Задание 2 ===")
print("До повышения уровня:", player1)
player1.level_up()
print("После повышения уровня:", player1)

# 3: Сделайте уровень игрока скрытым (например, _level), добавьте метод get_level().
# Письменно объясните, зачем нужен такой подход.

class Player:
    def __init__(self, nickname: str, level: int):
        self.nickname = nickname
        self._level = level  # защищённый атрибут

    def level_up(self):
        self._level += 1

    def get_level(self) -> int:
        return self._level

    def __str__(self):
        return f"Player(nickname='{self.nickname}', level={self._level})"

player1 = Player("Alice", 5)
print("\n=== Задание 3 ===")
print("Уровень игрока через get_level():", player1.get_level())
print("Объект игрока:", player1)

# 4: Создайте класс Skin с атрибутами name и rarity.
# Добавьте в Player возможность «надеть» скин (атрибут skin).
# Покажите, как игроки меняют скины.

class Skin:
    def __init__(self, name: str, rarity: str):
        self.name = name
        self.rarity = rarity

    def __str__(self):
        return f"Skin(name='{self.name}', rarity='{self.rarity}')"

class Player:
    def __init__(self, nickname: str, level: int):
        self.nickname = nickname
        self._level = level
        self.skin: Skin | None = None  # изначально без скина

    def equip_skin(self, skin: Skin):
        self.skin = skin

    def get_level(self) -> int:
        return self._level

    def __str__(self):
        skin_info = self.skin.name if self.skin else "None"
        return f"Player(nickname='{self.nickname}', level={self._level}, skin='{skin_info}')"

# Демонстрация смены скинов
epic_skin = Skin("Dragon Fire", "Epic")
rare_skin = Skin("Shadow Cloak", "Rare")

player1 = Player("Alice", 5)
player2 = Player("Bob", 3)

player1.equip_skin(epic_skin)
player2.equip_skin(rare_skin)

print("\n=== Задание 4 ===")
print(player1)
print(player2)

# 5: Добавьте метод attack(other_player), который выводит,
# что один игрок атакует другого. Пока урон фиксированный (например, минус 10 ед. здоровья (HP))

class Player:
    def __init__(self, nickname: str, level: int):
        self.nickname = nickname
        self._level = level
        self.skin: Skin | None = None
        self.health = 100  # начальное здоровье

    def equip_skin(self, skin: Skin):
        self.skin = skin

    def get_level(self) -> int:
        return self._level

    def attack(self, other_player):
        print(f"{self.nickname} атакует {other_player.nickname}!")
        other_player.health -= 10

    def __str__(self):
        skin_info = self.skin.name if self.skin else "None"
        return f"Player(nickname='{self.nickname}', level={self._level}, health={self.health}, skin='{skin_info}')"

# Демонстрация атаки
attacker = Player("Warrior", 10)
defender = Player("Archer", 8)

print("\n=== Задание 5 ===")
print("До атаки:", defender)
attacker.attack(defender)
print("После атаки:", defender)

# 6: Добавьте атрибут health в класс Player. Метод attack() теперь уменьшает здоровье противника.
# Если здоровье <= 0, выводится сообщение, что игрок проиграл.

# (атрибут health уже добавлен выше, обновим метод attack)

class Player:
    def __init__(self, nickname: str, level: int):
        self.nickname = nickname
        self._level = level
        self.skin: Skin | None = None
        self.health = 100

    def equip_skin(self, skin: Skin):
        self.skin = skin

    def get_level(self) -> int:
        return self._level

    def attack(self, other_player):
        if other_player.health <= 0:
            print(f"{other_player.nickname} уже проиграл!")
            return
        print(f"{self.nickname} атакует {other_player.nickname}!")
        other_player.health -= 10
        if other_player.health <= 0:
            print(f"{other_player.nickname} проиграл!")

    def __str__(self):
        skin_info = self.skin.name if self.skin else "None"
        return f"Player(nickname='{self.nickname}', level={self._level}, health={self.health}, skin='{skin_info}')"

# Демонстрация боя до смерти
attacker = Player("Brute", 12)
defender = Player("Rogue", 9)

print("\n=== Задание 6 ===")
while defender.health > 0:
    print(f"Здоровье {defender.nickname}: {defender.health}")
    attacker.attack(defender)

# 7: Создайте класс Weapon с атрибутами name и damage.
# Сделайте так, чтобы игрок мог выбрать оружие и использовать его в attack().

class Weapon:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"Weapon(name='{self.name}', damage={self.damage})"

class Player:
    def __init__(self, nickname: str, level: int):
        self.nickname = nickname
        self._level = level
        self.skin: Skin | None = None
        self.health = 100
        self.weapon: Weapon | None = None  # изначально без оружия

    def equip_skin(self, skin: Skin):
        self.skin = skin

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def get_level(self) -> int:
        return self._level

    def attack(self, other_player):
        if other_player.health <= 0:
            print(f"{other_player.nickname} уже проиграл!")
            return

        damage = self.weapon.damage if self.weapon else 10  # по умолчанию 10
        print(f"{self.nickname} атакует {other_player.nickname} с оружием '{self.weapon.name if self.weapon else 'кулаки'}'!")
        other_player.health -= damage

        if other_player.health <= 0:
            print(f"{other_player.nickname} проиграл!")

    def __str__(self):
        skin_info = self.skin.name if self.skin else "None"
        weapon_info = self.weapon.name if self.weapon else "None"
        return f"Player(nickname='{self.nickname}', level={self._level}, health={self.health}, skin='{skin_info}', weapon='{weapon_info}')"

# Демонстрация атаки с оружием
sword = Weapon("Steel Sword", 25)
bow = Weapon("Longbow", 18)

warrior = Player("Grommash", 15)
archer = Player("Sylvanas", 14)

warrior.equip_weapon(sword)
archer.equip_weapon(bow)

print("\n=== Задание 7 ===")
print(warrior)
print(archer)
warrior.attack(archer)
print("После атаки:", archer)

# 8 и 9: Создайте классы Warrior и Mage, которые наследуются от Player.
#   У каждого свои особенности:
#   a. Warrior: повышенный урон в ближнем бою
#   b. Mage: может атаковать магией (например, случайный урон в диапазоне).
# Реализуйте метод attack() по-разному для Warrior и Mage.
# Проверьте, что можно хранить их в одном списке и вызывать attack().

import random

class Warrior(Player):
    def __init__(self, nickname: str, level: int):
        super().__init__(nickname, level)
        self.health = 120  # у воина больше здоровья

    def attack(self, other_player):
        if other_player.health <= 0:
            print(f"{other_player.nickname} уже проиграл!")
            return

        base_damage = self.weapon.damage if self.weapon else 15
        bonus_damage = 5  # бонус ближнего боя
        total_damage = base_damage + bonus_damage

        print(f"[Воин] {self.nickname} наносит мощный удар по {other_player.nickname}!")
        other_player.health -= total_damage

        if other_player.health <= 0:
            print(f"{other_player.nickname} проиграл!")

class Mage(Player):
    def __init__(self, nickname: str, level: int):
        super().__init__(nickname, level)
        self.health = 80  # у мага меньше здоровья

    def attack(self, other_player):
        if other_player.health <= 0:
            print(f"{other_player.nickname} уже проиграл!")
            return

        # Маг наносит случайный урон от 10 до 30
        magic_damage = random.randint(10, 30)
        print(f"[Маг] {self.nickname} сотворил заклинание и нанёс {magic_damage} урона {other_player.nickname}!")
        other_player.health -= magic_damage

        if other_player.health <= 0:
            print(f"{other_player.nickname} проиграл!")

# Демонстрация полиморфизма: разные типы игроков в одном списке
print("\n=== Задания 8 и 9 ===")
players = [
    Warrior("Thrall", 20),
    Mage("Jaina", 19)
]

enemy = Player("Bandit", 10)
enemy.health = 100

for player in players:
    player.attack(enemy)
    print(f"Здоровье бандита: {enemy.health}")
    if enemy.health <= 0:
        break

# 10: Добавьте атрибут inventory (список предметов).
# Сделайте метод add_item(item). Создайте класс Item и положите в инвентарь разные объекты.

class Item:
    def __init__(self, name: str, item_type: str):
        self.name = name
        self.item_type = item_type

    def __str__(self):
        return f"Item(name='{self.name}', type='{self.item_type}')"

# Обновляем базовый класс Player
class Player:
    def __init__(self, nickname: str, level: int):
        self.nickname = nickname
        self._level = level
        self.skin: Skin | None = None
        self.health = 100
        self.weapon: Weapon | None = None
        self.inventory: list[Item] = []  # инвентарь

    def equip_skin(self, skin: Skin):
        self.skin = skin

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def add_item(self, item: Item):
        self.inventory.append(item)

    def get_level(self) -> int:
        return self._level

    def attack(self, other_player):
        if other_player.health <= 0:
            print(f"{other_player.nickname} уже проиграл!")
            return
        damage = self.weapon.damage if self.weapon else 10
        print(f"{self.nickname} атакует {other_player.nickname}!")
        other_player.health -= damage
        if other_player.health <= 0:
            print(f"{other_player.nickname} проиграл!")

    def __str__(self):
        skin_info = self.skin.name if self.skin else "None"
        weapon_info = self.weapon.name if self.weapon else "None"
        inventory_info = ', '.join(item.name for item in self.inventory) if self.inventory else "Empty"
        return (f"Player(nickname='{self.nickname}', level={self._level}, health={self.health}, "
                f"skin='{skin_info}', weapon='{weapon_info}', inventory=[{inventory_info}])")

# Демонстрация инвентаря
potion = Item("Health Potion", "Consumable")
scroll = Item("Teleport Scroll", "Magic")
armor_piece = Item("Iron Plate", "Armor")

hero = Player("Luna", 25)
hero.add_item(potion)
hero.add_item(scroll)
hero.add_item(armor_piece)

print("\n=== Задание 10 ===")
print(hero)