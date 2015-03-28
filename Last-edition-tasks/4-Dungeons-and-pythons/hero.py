from entity import Entity


class Hero(Entity):

    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname

    def known_as(self):
        return "{} the {}".format(self.name, self.nickname)

h = Hero("h", 100, "DragonSlayer")
print(h.name)
print(h.health)
print(h.nickname)
print(h.known_as())
h.take_damage(99)
print(h.health)
print(h.take_healing(100))
print(h.is_alive())
print(h.health)
