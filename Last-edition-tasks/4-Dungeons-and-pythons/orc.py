from entity import Entity
from weapon import Weapon


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        if berserk_factor < 1:
            self.berserk_factor = 1
        elif berserk_factor > 2:
            self.berserk_factor = 2
        else:
            self.berserk_factor = berserk_factor

    def attack(self):
        if self.has_weapon():
            self.weapon.damage *= self.berserk_factor
            if self.weapon.critical_hit():
                return self.weapon.damage * 2
            return self.weapon.damage
        return 0
