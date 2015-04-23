import unittest
from gitnetwork import DirectedGraph, GitHubNetwork
import requests


class GraphTests(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()
        self.git = GitHubNetwork("PavlinGergov", 2)

    def test_add_and_has_node(self):
        self.graph.add_node("Rado")
        self.assertTrue(self.graph.has_node("Rado"))

    def test_duplication(self):
        self.graph.add_node("Rado")
        with self.assertRaises(Exception):
            self.graph.add_node("Rado")

    def test_add_edge(self):
        self.graph.add_edge("Rado", "Ivo")
        self.assertEqual(self.graph.info, {"Rado": ["Ivo"], "Ivo": []})

    def test_get_neighbours(self):
        self.graph.add_edge("Rado", "Ivo")
        self.assertEqual(self.graph.get_neighbors_for("Rado"), ["Ivo"])

    def test_path_between(self):
        self.graph.add_edge("Pavli", "Rado")
        self.graph.add_edge("Rado", "Ivo")
        self.graph.add_edge("Rado", "Ani")
        self.graph.add_edge("Ani", "Gosho")
        # {
        # "Pavli": ["Rado"],
        # "Rado": ["Ivo", "Ani"],
        # "Ivo": [],
        # "Ani": ["Gosho"],
        # "Gosho": []
        # }
        self.assertTrue(self.graph.path_between("Pavli", "Ani"))
        self.assertFalse(self.graph.path_between("Pavli", "Gosho"))

    def test_do_you_follow_directly(self):
        user = "RadoRado"
        self.assertEqual(self.git.do_you_follow(user), True)
        self.assertEqual(str(requests.get(self.git.ADDRESS + self.git.get_username(
            ) + "/following/" + user + self.git.IDS)), "<Response [204]>")

    def test_do_I_follow_indirectly_someone(self):
        self.assertTrue(self.git.do_you_follow_indirectly("stoianivanov"))
        self.assertFalse(self.git.do_you_follow_indirectly("animilh"))

    def test_does_he_she_follows_me_directly(self):
        self.assertTrue(self.git.does_he_she_follows("Rositsazz"))
        self.assertEqual(str(requests.get(self.git.ADDRESS + "Rositsazz/\
following/PavlinGergov" + self.git.IDS)), "<Response [204]>")

        self.assertFalse(self.git.does_he_she_follows("skanev"))
        self.assertEqual(str(requests.get(self.git.ADDRESS + "skanev/\
following/PavlinGergov" + self.git.IDS)), "<Response [404]>")

    def test_does_he_she_follows_indirectly(self):
        self.assertTrue(self.git.does_he_she_follows_indirectly("Rositsazz"))

    def test_who_follows_you_back(self):
        print(self.git.who_follows_you_back())

if __name__ == '__main__':
    unittest.main()
