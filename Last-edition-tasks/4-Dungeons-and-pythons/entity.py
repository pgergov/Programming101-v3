class Entity():

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health

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
