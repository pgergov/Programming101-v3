from random import randint


class Weapon():

    def __init__(self, typpe, damage, critical_strike_percent):
        self.type = typpe
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        crit = randint(0, 100)
        return crit / 100 <= self.critical_strike_percent
