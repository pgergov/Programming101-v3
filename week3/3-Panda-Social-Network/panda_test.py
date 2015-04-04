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
        with self.assertRaises(Exception):
            Panda("ivo", "not_valid_email", "male")

    def test_is_gender_valid_type(self):
        with self.assertRaises(TypeError):
            Panda("jorko", "joro@abv.bg", 10)

    def test_are_you_normal_panda(self):
        with self.assertRaises(ValueError):
            Panda("jorko", "joro@abv.bg", "shemale")

    def test_is_network_valid(self):
        self.assertTrue(isinstance(self.network, PandaSocialNetwork))

    def test_is_panda_added_in_network(self):
        self.network.add_panda(self.panda)
        self.assertTrue(self.panda in self.network.get_pandas())

    def test_is_name_of_added_panda_already_taken(self):
        with self.assertRaises(Exception):
            self.network.add_panda(self.panda)
            self.network.add_panda(self.panda)

    def test_if_pandas_are_already_friends_with_each_other(self):
        self.network.make_friends(self.panda, self.other_panda)
        self.assertTrue(self.network.are_friends(self.panda, self.other_panda))

    def test_are_pandas_already_friends(self):
        self.network.make_friends(self.panda, self.other_panda)
        with self.assertRaises(Exception):
            self.network.make_friends(self.panda, self.other_panda)

    def test_panda_make_friends(self):
        self.network.make_friends(self.panda, self.other_panda)
        self.assertEqual(self.network.friends_of(
            self.panda), [self.other_panda.name()])

    def test_connection_between_direct_panda_friends(self):
        self.network.make_friends(self.panda, self.other_panda)
        self.assertEqual(1, self.network.connection_level(
            self.panda, self.other_panda))

    def test_connection_on_higher_level_than_direct_friends(self):
        rado = Panda("rado", "rade@abv.bg", "male")
        ivo = Panda("ivo", "ivo@abv.bg", "male")
        self.network.make_friends(self.panda, self.other_panda)
        self.network.make_friends(self.panda, ivo)
        self.network.make_friends(ivo, rado)
        # {
        #     panda: [other_panda, ivo],
        #     other_panda: [panda],
        #     ivo: [panda, rado],
        #     rado: [ivo]
        # }
        # rado -> ivo | level 1
        # rado -> panda | level 2
        # rado -> other_panda | level 3
        self.assertEqual(3, self.network.connection_level(
            rado, self.other_panda))

    def test_connection_if_one_of_the_pandas_is_not_member(self):
        self.network.make_friends(self.panda, self.other_panda)
        ivo = Panda("Ivo", "ivo@abv.bg", "male")
        # Noone invited ivo to the super - duper www.pandabook.com
        self.assertEqual(False, self.network.connection_level(self.panda, ivo))

    def test_connection_if_pandas_have_no_connection(self):
        self.network.add_panda(self.panda)
        self.network.add_panda(self.other_panda)
        self.assertEqual(-1, self.network.connection_level(
            self.panda, self.other_panda))

    def test_are_pandas_connected_if_they_really_are(self):
        self.network.make_friends(self.panda, self.other_panda)
        self.assertTrue(self.network.are_connected(
            self.panda, self.other_panda))

    def test_are_connected_if_pandas_are_NOT_connected(self):
        self.network.add_panda(self.panda)
        self.network.add_panda(self.other_panda)
        self.assertFalse(self.network.are_connected(
            self.panda, self.other_panda))

    def test_gender_counter_with_invalid_level_input(self):
        with self.assertRaises(Exception):
            self.network.how_many_gender_in_network(0, self.panda, "male")

    def test_gender_counter_with_invalid_gender(self):
        with self.assertRaises(Exception):
            self.network.how_many_gender_in_network(2, self.panda, "shemale")

    def test_gender_counter(self):
        ani = Panda("Ani", "ani@abv.bg", "female")
        self.network.make_friends(self.panda, self.other_panda)
        self.network.make_friends(ani, self.other_panda)
        # {
        # panda: [other_panda]
        # other_panda: [panda, ani]
        # ani: [other_panda]
        # }
        self.assertEqual(2, self.network.how_many_gender_in_network(
            5, ani, "male"))

    def test_pandabook_save_and_load_capabilities(self):
        self.network.make_friends(self.panda, self.other_panda)
        self.network.save_members("members_test.txt")
        self.network.save_friends("friends_test.txt")

        pandabook = PandaSocialNetwork()
        pandabook.load_members("members_test.txt")
        pandabook.load_friends("friends_test.txt")

        self.assertEqual(self.network.get_pandas(), pandabook.get_pandas())

if __name__ == '__main__':
    unittest.main()
