import unittest
from panda import Panda
from network import PandaSocialNetwork


class PandaNetworkTest(unittest.TestCase):

    def setUp(self):
        self.panda = Panda("Joro", "joro_vr@abv.bg", "male")
        self.other_panda = Panda("Gosho", "gosho@abv.bg", "male")
        self.network = PandaSocialNetwork()

    def test_is_created_object_valid(self):
        self.assertTrue(isinstance(self.panda, Panda))

    def test_is_name_valid_type(self):
        with self.assertRaises(TypeError):
            Panda(10, "joro@abv.bg", "male")

    def test_is_email_valid_type(self):
        with self.assertRaises(TypeError):
            Panda("joro_bekyma", 10, "male")

    def test_is_email_valid(self):
        pass

    def test_is_gender_valid_type(self):
        with self.assertRaises(TypeError):
            Panda("jorko", "joro@abv.bg", 10)

    def test_are_you_human(self):
        with self.assertRaises(ValueError):
            Panda("jorko", "joro@abv.bg", "shemale")

    def test_is_network_valid(self):
        self.assertTrue(isinstance(self.network, PandaSocialNetwork))

    def test_is_panda_added_in_network(self):
        self.network.add_panda(self.panda)
        self.assertTrue(self.panda in self.network.pandas())

    def test_if_added_panda_is_in_pandas(self):
        self.network.add_panda(self.panda)
        self.assertTrue(self.network.has_panda(self.panda))

    def test_is_name_of_added_panda_already_taken(self):
        with self.assertRaises(Exception):
            self.network.add_panda(self.panda)
            self.network.add_panda(self.panda)

    def test_if_pandas_are_already_friends_with_each_other(self):
        self.network.make_friends(self.panda, self.other_panda)
        self.assertTrue(self.network.has_panda(
            self.panda) and self.network.has_panda(self.other_panda))

    def test_are_pandas_already_friends(self):
        self.network.make_friends(self.panda, self.other_panda)
        with self.assertRaises(Exception):
            self.network.make_friends(self.panda, self.other_panda)

    def test_panda_make_friends(self):
        self.network.make_friends(self.panda, self.other_panda)
        self.assertEqual(self.network.friends_of(
            self.panda), [self.other_panda])

    def test_panda_connection(self):
        joro = Panda("joro", "joro@abv.bg", "male")
        gosho = Panda("gosho", "gosho@abv.bg", "male")
        vanq = Panda("vanq", "vanq@abv.bg", "female")
        self.network.make_friends(joro, gosho)
        self.network.make_friends(joro, vanq)
        # {joro: gosho, vanq, gosho: joro, vanq: joro}
        rado = Panda("rado", "rade@abv.bg", "male")
        ivo = Panda("ivo", "ivo@abv.bg", "male")
        self.network.make_friends(ivo, rado)
        self.network.make_friends(ivo, joro)
        # {joro: gosho, ivo, vanq, gosho: joro
        # vanq: joro, ivo: rado, joro rado: ivo}
        # petko = Panda("petko", "petko@abv.bg", "male")
        self.assertEqual(3, self.network.connection_level(rado, vanq))

    def test_are_pandas_connected(self):
        self.network.make_friends(self.panda, self.other_panda)
        petko = Panda("Petko", "petko@abv.bg", "male")
        self.network.make_friends(self.panda, petko)
        self.assertTrue(self.network.are_connected(petko, self.other_panda))

    def test_are_pandas_not_connected(self):
        self.network.make_friends(self.panda, self.other_panda)
        petko = Panda("Petko", "petko@abv.bg", "male")
        self.assertFalse(self.network.are_connected(petko, self.other_panda))

    def test_how_many_gender_in_network_invalid_level(self):
        with self.assertRaises(ValueError):
            self.network.how_many_gender_in_network(0, self.panda, "male")

    def test_panda_gender_number(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        tony = Panda("Tony", "tony@pandamail.com", "female")
        self.network.make_friends(ivo, rado)
        self.network.make_friends(rado, tony)
        self.assertEqual(1, self.network.how_many_gender_in_network(
            2, ivo, "female"))

if __name__ == '__main__':
    unittest.main()
