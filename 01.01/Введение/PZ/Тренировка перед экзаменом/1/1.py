class BaseChar:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        return 0  # базовый урон - переопределяется в подклассах

class Player(BaseChar):
    def __init__(self, name):
        super().__init__(name, hp=100)
        self.inv = []  # инвентарь

    def addItem(self, item):
        self.inv.append(item)

    def hasItem(self, item):
        return item in self.inv

class Enemy(BaseChar):
    def __init__(self, name, hp):
        super().__init__(name, hp)

class Goblin(Enemy):
    def __init__(self, name):
        super().__init__(name, hp=30)  # Здоровье гоблина

    def attack(self):
        import random
        return random.randint(5, 10)

class Orc(Enemy):
    def __init__(self, name):
        super().__init__(name, hp=50)  # Здоровье орка

    def attack(self):
        return 20

class Loc:
    def __init__(self, name, desc, items=None, enemies=None):
        self.name = name
        self.desc = desc
        self.items = items or []
        self.enemies = enemies or []

# Глобальные переменные состояния игры
player = None
currLocIdx = 0
gameWin = False
gameOver = False

# Места: старт - лес - пещера - замок
locs = [
    Loc("Деревня", "Ты в родной деревне Впереди - тропа в лес", ["меч"]),
    Loc("Лес", "Темный лес Слышен шорох", [], [Goblin("Гоблин")]),
    Loc("Пещера", "Сырая пещера Пахнет гнилью", ["ключ"], [Orc("Орк")]),
    Loc("Замок", "Тронный зал Здесь ждёт финал", [], [Orc("Главный Орк")])
]

def handle_go():
    global currLocIdx
    if currLocIdx < len(locs) - 1:
        currLocIdx += 1
        print(f"Ты перешёл в: {locs[currLocIdx].name}")
        print(locs[currLocIdx].desc)
        if locs[currLocIdx].enemies:
            print("Враги здесь:", ", ".join(e.name for e in locs[currLocIdx].enemies))
    else:
        print("Дальше идти некуда")

def handle_take():
    loc = locs[currLocIdx]
    if loc.items:
        item = loc.items.pop(0)
        player.addItem(item)
        print(f"Ты подобрал: {item}")
    else:
        print("Здесь ничего нет")

def handle_fight():
    loc = locs[currLocIdx]
    if not loc.enemies:
        print("Нет с кем драться")
        return

    for enemy in loc.enemies[:]:  # копия списка для безопасного удаления
        print(f"Сражение с {enemy.name}!")
        while player.hp > 0 and enemy.hp > 0:
            dmgToEnemy = 15  # урон игрока
            enemy.hp -= dmgToEnemy
            print(f"Ты наносишь {dmgToEnemy} урона")
            if enemy.hp <= 0:
                print(f"{enemy.name} повержен!")
                loc.enemies.remove(enemy)
                break

            dmgToPlayer = enemy.attack()
            player.hp -= dmgToPlayer
            print(f"{enemy.name} наносит тебе {dmgToPlayer} урона Здоровье: {player.hp}")
            if player.hp <= 0:
                global gameOver
                gameOver = True
                print("Ты погиб")
                return

    if currLocIdx == len(locs) - 1 and not locs[currLocIdx].enemies: # Проверка победы в финальной локации
        if player.hasItem("ключ"):
            global gameWin
            gameWin = True
            print("Ты победил Ключ открыл трон - королевство спасено")
        else:
            print("Ты победил врага но без ключа ты не герой")

def handle_info():
    loc = locs[currLocIdx]
    print(f"\nМесто: {loc.name}")
    print(f"Здоровье: {player.hp}")
    print(f"Инвентарь: {player.inv if player.inv else 'пусто'}")
    if loc.items:
        print(f"Предметы здесь: {loc.items}")
    if loc.enemies:
        print(f"Враги: {[e.name for e in loc.enemies]}")

def main():
    global player  # объявление глобальной переменной ДО присваивания
    print("Добро пожаловать в мини-квест")
    name = input("Введи имя героя: ")
    player = Player(name)

    print(f"\nПривет {player.name}! Ты в {locs[0].name}")
    print(locs[0].desc)
    print("Доступные команды: иди, бери, бейся, инфо, выход")

    while True:
        if gameWin:
            print("Игра окончена ты победил")
            break
        if gameOver:
            print("Игра окончена ты проиграл")
            break

        cmd = input("\n> ").strip().lower()
        if cmd == "иди":
            handle_go()
        elif cmd == "бери":
            handle_take()
        elif cmd == "бейся":
            handle_fight()
        elif cmd == "инфо":
            handle_info()
        elif cmd == "выход":
            break
        else:
            print("Ошибка, все доступные команды: иди, бери, бейся, инфо, выход")

if __name__ == "__main__":
    main()