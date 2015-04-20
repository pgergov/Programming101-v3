from hero import Hero
from enemy import Enemy
from weapons_and_spells import Weapon, Spell
import random


class Dungeon:

    def __init__(self, file_name):
        self.file = file_name
        self.map = None
        self.hero = None
        self.enemy = None
        self.treasure = {
                   "heal_potion": [25, 50, 75, 100],
                   "mana_potion": [25, 50, 75, 100],
                   "weapon": [Weapon("Axe", damage=20),
                              Weapon("Sword", damage=25),
                              Weapon("Mace", damage=30)],
                   "spell": [Spell("Frostbolt", 20, 30, cast_range=3),
                             Spell("Fireball", 25, 40, cast_range=2),
                             Spell("Arcanebolt", 30, 50, cast_range=2)],
                   }
        # self.generate_map()

    def generate_map(self):
        with open(self.file, 'r') as f:
            content = f.read()
            lines = content.split("\n")
            lines = [line for line in lines if line.strip() != ""]
            self.map = [list(line) for line in lines]

    def print_map(self):
        for roll in self.map:
            print("".join(roll))

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
            return False
        elif self.map[y][x] == ".":
            self.map[y][x] = "H"
            return True
        elif self.map[y][x] == "E":
            self.enemy = Enemy(100, 100, 20)
            self.start_fight()
            if self.hero.is_alive():
                self.map[y][x] = "H"
                return True
            else:
                print("GAME OVER")
                return True
        elif self.map[y][x] == "T":
            self.pick_treasure()
            self.map[y][x] = "H"
            return True
        elif self.map[y][x] == "G":
            print("Your quest is complete! Good job!")
            return True

    def pick_treasure(self):
        treasures = ["heal_potion", "mana_potion", "weapon", "spell"]
        loot = random.choice(treasures)
        if loot == "heal_potion":
            heal = random.choice(self.treasure[loot])
            self.hero.take_healing(heal)
            print("Found health potion. Hero health is {}.".format(
                self.hero.get_health()))
        elif loot == "mana_potion":
            mana = random.choice(self.treasure[loot])
            self.hero.take_mana(mana)
            print("Found mana potion. Hero mana is {}.".format(
                self.hero.get_mana()))
        elif loot == "weapon":
            weapon = random.choice(self.treasure[loot])
            self.hero.equip(weapon)
            print("Found a weapon - {}.".format(weapon.name))
        elif loot == "spell":
            spell = random.choice(self.treasure[loot])
            self.hero.learn(spell)
            print("Learned a new spell: {}.".format(spell.name))

    def get_position(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == "H":
                    return (y, x)

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
        self.hero.take_mana(self.hero.mana_regeneration_rate)
        return True

    def determine_damage_source(self):
        if self.hero.has_spell() and self.hero.has_weapon():
            if self.hero.spell.get_damage() >= self.hero.weapon.get_damage():
                if self.hero.get_mana() >= self.hero.spell.get_mana_cost():
                    return "spell"
            return "weapon"
        elif self.hero.has_spell():
            if self.hero.get_mana() >= self.hero.spell.get_mana_cost():
                return "spell"
        elif self.hero.has_weapon():
            return "weapon"

    def check_left(self):
        position = self.get_position()
        x = position[1]
        y = position[0]
        can_pass_freely = True
        for i in range(1, self.hero.spell.get_cast_range() + 1):
            if can_pass_freely:
                if self.map[y][x - i] == "E":
                    return (y, x)
            if self.map[y][x - i] != ".":
                can_pass_freely = False

    def check_right(self):
        position = self.get_position()
        x = position[1]
        y = position[0]
        can_pass_freely = True
        for i in range(1, self.hero.spell.get_cast_range() + 1):
            if can_pass_freely:
                if self.map[y][x + i] == "E":
                    return (y, x + i)
            if self.map[y][x + i] != ".":
                can_pass_freely = False

    def check_up(self):
        position = self.get_position()
        x = position[1]
        y = position[0]
        can_pass_freely = True
        for i in range(1, self.hero.spell.get_cast_range() + 1):
            if can_pass_freely:
                if self.map[y - i][x] == "E":
                    return (y - i, x)
            if self.map[y - i][x] != ".":
                can_pass_freely = False

    def check_down(self):
        position = self.get_position()
        x = position[1]
        y = position[0]
        can_pass_freely = True
        for i in range(1, self.hero.spell.get_cast_range() + 1):
            if can_pass_freely:
                if self.map[y + i][x] == "E":
                    return (y + i, x)
            try:
                if self.map[y + i][x] != ".":
                    can_pass_freely = False
            except:
                pass

    def try_range_attack(self):
        position = self.get_position()
        x = position[1]
        y = position[0]
        if self.check_right() is not None:
            self.enemy = Enemy(100, 100, 20)
            self.range_fight(self.check_right(), "left")
            if self.hero.is_alive():
                self.map[y][x] = "H"
        elif self.check_left() is not None:
            self.enemy = Enemy(100, 100, 20)
            self.range_fight(self.check_right(), "right")
            if self.hero.is_alive():
                self.map[y][x] = "H"
        elif self.check_down() is not None:
            self.enemy = Enemy(100, 100, 20)
            self.range_fight(self.check_right(), "up")
            if self.hero.is_alive():
                self.map[y][x] = "H"
        elif self.check_up() is not None:
            self.enemy = Enemy(100, 100, 20)
            self.range_fight(self.check_right(), "down")
            if self.hero.is_alive():
                self.map[y][x] = "H"
        else:
            print("No enemy in casting range!")

    def move_enemy(self, current_position, direction):
        self.map[current_position[0]][current_position[1]] = "."
        if direction == "right":
            self.map[current_position[0]][current_position[1] + 1] = "E"
            return (current_position[0], current_position[1] + 1)
        if direction == "left":
            self.map[current_position[0]][current_position[1] - 1] = "E"
            return (current_position[0], current_position[1] - 1)
        if direction == "up":
            self.map[current_position[0] - 1][current_position[1]] = "E"
            return (current_position[0] - 1, current_position[1])
        if direction == "down":
            self.map[current_position[0] + 1][current_position[1]] = "E"
            return (current_position[0] + 1, current_position[1])

    def range_fight(self, enemy_position, enemy_moving_direction):
        print("A range fight was started between our {} and {}".format(
            repr(self.hero), repr(self.enemy)))
        while self.get_position() is not None:
            self.enemy.take_damage(self.hero.attack(by="magic"))
            print("Hero casts a {}, hits enemy for {} dmg. Enemy health\
 is {}".format(self.hero.spell.name, self.hero.spell.get_damage(
                         ), self.enemy.get_health()))
            enemy_position = self.move_enemy(enemy_position, enemy_moving_direction)
            print("Enemy moved one square towards Hero.")
        self.start_fight()

    def start_fight(self):
        print("A melee fight was started between our {} and {}".format(
            repr(self.hero), repr(self.enemy)))
        while True:
            if self.determine_damage_source() is not None:
                if self.determine_damage_source() == "spell":
                    self.enemy.take_damage(self.hero.attack(by="magic"))
                    print("Hero casts a {}, hits enemy for {} dmg. Enemy health\
 is {}".format(self.hero.spell.name, self.hero.spell.get_damage(
                         ), self.enemy.get_health()))
                elif self.determine_damage_source() == "weapon":
                    self.enemy.take_damage(self.hero.attack(by="weapon"))
                    print("Hero hits enemy with {} for {} dmg. Enemy health\
 is {}".format(self.hero.weapon.name, self.hero.weapon.get_damage(
                         ), self.enemy.get_health()))
            if not self.enemy.is_alive():
                print("Enemy is dead!")
                break
            self.hero.take_damage(self.enemy.attack(by="weapon"))
            print("Enemy hits hero for {} dmg. Hero health is {}".format(
                self.enemy.damage, self.hero.get_health()))
            if not self.hero.is_alive():
                print("Hero is dead!")
                break
