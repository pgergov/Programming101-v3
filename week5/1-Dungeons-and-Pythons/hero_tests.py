from hero import Hero
import unittest


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Ahri", "Kingslayer", 100, 100, 2)

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), "Ahri the Kingslayer")

    def test_take_damage(self):
        self.hero.take_damage(50.5)
        self.assertEqual(self.hero.get_health(), 49.5)

    def test_take_healing(self):
        self.hero.take_damage(50)
        self.assertTrue(self.hero.take_healing(55))
        self.assertEqual(self.hero.get_health(), 100)

    def test_mana_regeneration_while_moving(self):
        pass

    def test_mana_regeneration_with_potion(self):
        pass


if __name__ == '__main__':
    unittest.main()
