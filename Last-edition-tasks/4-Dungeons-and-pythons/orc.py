from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        if berserk_factor < 1:
            self.berserk_factor = 1
        elif berserk_factor > 2:
            self.berserk_factor = 2
        else:
            self.berserk_factor = berserk_factor

marti = Orc("Marti", 100, 0.65)
print(marti.name)
print(marti.health)
print(marti.berserk_factor)
marti.take_damage(99)
print(marti.take_healing(100))
print(marti.is_alive())
print(marti.health)
