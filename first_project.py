from random import randint


class Character:

    RANGE_VALUE_ATTACK = (1, 10)

    FIRST_ATTACK: int = 10
    SECOND_ATTACK: int = 15
    DEFENCE: int = 30

    def __init__(self, attack: int, deffence: int):
        self.attack = attack
        self.deffence = deffence

    def first_attack(self):
        return ((self.attack + randint(*self.RANGE_VALUE_ATTACK))
                * self.FIRST_ATTACK / self.deffence)


class Warrior(Character):
    pass


mell = Character(28, 50)
print(mell.first_attack())
