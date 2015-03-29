class Entity():

    def __init__(self, name, health,):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = None

    def is_alive(self):
        return self.health > 0

    def get_health(self):
        return self.health

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health <= 0:
            self.health = 0

    def take_healing(self, healing_points):
        if self.is_alive():
            self.health += healing_points
            if self.health > self.max_health:
                self.health = self.max_health
            return True
        return False

    def has_weapon(self):
        return self.weapon is not None

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.has_weapon():
            if self.weapon.critical_hit():
                return self.weapon.damage * 2
            return self.weapon.damage
        return 0
