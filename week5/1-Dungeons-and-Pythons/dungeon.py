from hero import Hero
from enemy import Enemy
from weapons_and_spells import Weapon


class Dungeon:

    def __init__(self, file_name):
        self.file = file_name
        self.map = None
        self.hero = None
        self.enemy = None

    def generate_map(self):
        with open(self.file, 'r') as f:
            content = f.read()
            lines = content.split("\n")
            lines = [line for line in lines if line.strip() != ""]
            self.map = [list(line) for line in lines]

    def print_map(self):
        for roll in self.map:
            print("".join(roll))

    # Add spawn if our hero dies
    def spawn(self, hero_instance):
        if not isinstance(hero_instance, Hero):
            raise TypeError("The hero must be from class Hero")
        self.hero = hero_instance
        found = False
        for roll in self.map:
            for i in range(len(roll)):
                if roll[i] == "S":
                    roll[i] = "H"
                    found = True
                    break
            if found:
                break
        return found

    def check_out_of_range(self, x, y):
        if y < 0 or y > len(self.map) - 1:
            return False
        if x < 0 or x > len(self.map[y]):
            return False
        return True

    def move_to_next_field(self, x, y):
        if self.map[y][x] == "#":
            return False  # Add what should happen in this case
        elif self.map[y][x] == ".":
            self.map[y][x] = "H"
            return True
        elif self.map[y][x] == "E":
            pass  # Add fight and return True or False
        elif self.map[y][x] == "T":
            pass  # Add treasure and return True or False

    def get_position(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == "H":
                    return (y, x)

    # def move_hero_to_direction(self, x, y):
    #     if self.check_out_of_range(x, y):
    #         if not self.move_to_next_field(x, y):
    #             return False
    #         self.map[y][x] = "."
    #     else:
    #         return False

# Refactor move_hero, use the upper function etc.

    def move_hero(self, direction):
        position = self.get_position()
        x = position[1]
        y = position[0]
        if direction == "right":
            if self.check_out_of_range(x + 1, y):
                if not self.move_to_next_field(x + 1, y):
                    return False
                self.map[y][x] = "."
            else:
                return False
        if direction == "left":
            if self.check_out_of_range(x - 1, y):
                if not self.move_to_next_field(x - 1, y):
                    return False
                self.map[y][x] = "."
            else:
                return False
        if direction == "up":
            if self.check_out_of_range(x, y - 1):
                if not self.move_to_next_field(x, y - 1):
                    return False
                self.map[y][x] = "."
            else:
                return False
        if direction == "down":
            if self.check_out_of_range(x, y + 1):
                if not self.move_to_next_field(x, y + 1):
                    return False
                self.map[y][x] = "."
            else:
                return False
        return True

    def fight(self):
        self.hero = Hero("Ahri", "Kingslayer", 100, 100, 2)
        self.enemy = Enemy(100, 100, 20)
        w = Weapon("The Axe of Destiny", damage=20)
        self.hero.equip(w)
        print("A fight was started between our {} and {}".format(
            repr(self.hero), repr(self.enemy)))
        while True:
            self.enemy.take_damage(self.hero.attack(by="weapon"))
            print("Hero hits with {} for {} dmg. Enemy health is {}".format(w.name, w.get_damage(), self.enemy.get_health()))
            if not self.enemy.is_alive():
                print("Enemy is dead!")
                break
            self.hero.take_damage(self.enemy.attack(by="weapon"))
            print("Enemy hits hero for {} dmg. Hero health is {}".format(self.enemy.damage, self.hero.get_health()))
            if not self.hero.is_alive():
                print("Hero is dead!")
                break
d = Dungeon("level1.txt")
d.fight()