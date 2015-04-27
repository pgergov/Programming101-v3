from hero import Hero
from dungeon import Dungeon
from weapons_and_spells import Weapon, Spell


h = Hero(name="Bron", title="Dragonslayer",
         health=100, mana=100, mana_regeneration_rate=2)
w = Weapon(name="The Axe of Destiny", damage=20)
h.equip(w)
s = Spell(name="Lightning bolt", damage=30, mana_cost=50, cast_range=2)
h.learn(s)
dungeon = Dungeon("level1.txt")
dungeon.spawn(h)
dungeon.print_map()
dungeon.move_hero("right")
dungeon.move_hero("down")
dungeon.print_map()
dungeon.try_range_attack()
dungeon.move_hero("down")
dungeon.move_hero("down")
dungeon.try_range_attack()
dungeon.print_map()
dungeon.move_hero("right")
dungeon.move_hero("right")
dungeon.move_hero("right")
dungeon.move_hero("right")
dungeon.move_hero("up")
dungeon.print_map()
dungeon.move_hero("down")
