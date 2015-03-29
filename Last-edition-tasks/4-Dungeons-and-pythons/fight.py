from hero import Hero
from orc import Orc
from weapon import Weapon
from random import randint
from dungeon import Dungeon


class Fight():

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def flip_coin(self):
        coin = randint(1, 2)
        return coin

    def hero_attack(self):
        damage = hero.attack()
        orc.take_damage(damage)
        print("{} hits {} for {} damage.".format(hero.name, orc.name, damage))
        print("{} has {} hp.".format(orc.name, orc.get_health()))

    def orc_attack(self):
        damage = orc.attack()
        hero.take_damage(damage)
        print("{} hits {} for {} damage.".format(orc.name, hero.name, damage))
        print("{} has {} hp.".format(hero.name, hero.get_health()))

    def simulate_fight(self):
        print("{} and {} forced a fight!".format(hero.known_as(), orc.name))
        print()
        while True:
            if self.flip_coin() == 1:
                self.hero_attack()
                if orc.is_alive():
                    self.orc_attack()
                else:
                    print("{} has slained {}!".format(hero.name, orc.name))
                    break
            else:
                self.orc_attack()
                if hero.is_alive():
                    self.hero_attack()
                else:
                    print("{} has slained {}!".format(orc.name, hero.name))
                    break
            print()


hero = Hero("Ashe", 100, "OrcSlayer")
orc = Orc("Kaiba", 100, 1.25)
axe = Weapon("Axe", 10, 0.35)
sword = Weapon("Sword", 15, 0.15)
hero.equip_weapon(sword)
orc.equip_weapon(axe)
battle = Fight(hero, orc)
# battle.simulate_fight()

the_map = Dungeon("basic_dungeon.txt")
print(the_map.spawn("player_1", hero))
the_map.print_map()
print(the_map.spawn("player_2", orc))
the_map.print_map()
