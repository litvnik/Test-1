class Player:
    def __init__(self, initial_xp=0):
        self.__xp = initial_xp

    def raise_score(self, amount):
        if amount < 0:
            raise ValueError("Значение должно быть неотрицательным")
        self.__xp += amount

    def take_score(self, amount):
        if amount < 0:
            raise ValueError("Значение должно быть неотрицательным")
        if amount > self.__xp:
            raise ValueError("Недостаточно очков опыта")
        self.__xp -= amount

    def get_xp(self):
        return self.__xp