from random import randint


class MelleeWeapon:

    RANGE_VALUE_ATTACK = (0, 10)

    ATTACK: float = 10
        
    def __init__(self, attack: float,
                 attack_speed: float,
                 critikal_attack: float):
        self.attack = attack
        self.attack_speed = attack_speed
        self.critical_attack = critikal_attack

    def one_heand_attack(self):
        return ((self.attack + randint(*self.RANGE_VALUE_ATTACK))
                * self.ATTACK)


class Sword(MelleeWeapon):
    RANGE_VALUE_SPEED = (1, 10)

    def ng_sword(self):
        return self.one_heand_attack() * randint(*self.RANGE_VALUE_SPEED)


mell = Sword(28, 50, 20)
print(mell.ng_sword())
