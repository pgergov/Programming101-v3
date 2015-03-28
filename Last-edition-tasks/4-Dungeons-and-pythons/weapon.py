from random import randint


class Weapon():

    def __init__(self, typpe, damage, critical_strike_percent):
        self.type = typpe
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        crit = randint(0, 100)
        print(crit)
        return crit / 100 <= self.critical_strike_percent

axe = Weapon("Mighty Axe", 25, 0.2)
print(axe.type)
print(axe.damage)
print(axe.critical_strike_percent)
print(axe.critical_hit())
