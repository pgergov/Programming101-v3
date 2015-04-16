from hero import Hero
from enemy import Enemy
from weapons_and_spells import Weapon, Spell
import unittest


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Ahri", "Kingslayer", 100, 100, 2)
        self.enemy = Enemy(100, 100, 20)
        self.weapon = Weapon("The Axe of Destiny", damage=20)
        self.spell = Spell(
            name="Fireball", damage=30, mana_cost=50, cast_range=2)

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), "Ahri the Kingslayer")

    def test_take_damage(self):
        self.hero.take_damage(150)
        self.assertEqual(self.hero.get_health(), 0)

    def test_take_healing(self):
        self.hero.take_damage(50)
        self.assertTrue(self.hero.take_healing(55))
        self.assertEqual(self.hero.get_health(), 100)

    def test_take_mana_with_potion(self):
        pass

        # Test enemy who can not regenerate mana
    def test_mana_regeneration_while_moving(self):
        pass

    def test_can_cast(self):
        self.hero.learn(self.spell)
        self.assertTrue(self.hero.can_cast())

    def test_can_cast_with_no_spells_learned(self):
        self.assertFalse(self.hero.can_cast())

    def test_attack_not_being_specified(self):
        with self.assertRaises(ValueError):
            self.hero.attack(by="gun")

    def test_attack_without_weapon_or_spell(self):
        self.assertEqual(self.hero.attack(by="weapon"), 0)
        self.assertEqual(self.hero.attack(by="magic"), 0)
        # Test for enemy (base damage= = 20)
        self.assertEqual(self.enemy.attack(by="weapon"), 20)
        self.assertEqual(self.enemy.attack(by="magic"), 20)

    def test_attack(self):
        self.hero.equip(self.weapon)
        self.assertEqual(self.hero.attack(by="weapon"), 20)
        self.hero.learn(self.spell)
        self.assertEqual(self.hero.attack(by="magic"), 30)

if __name__ == '__main__':
    unittest.main()
