from panda import Panda
import json


class PandaSocialNetwork():

    def __init__(self):
        self.pandas = {}

    def get_pandas(self):
        return self.pandas

    def has_panda(self, other):
        return other in self.pandas

    def add_panda(self, other):
        if isinstance(other, Panda):
            if not self.has_panda(other):
                self.pandas[other] = []
            else:
                raise Exception("Name is already taken.")
        else:
            raise TypeError("Give me a real panda!")

    def are_friends(self, panda1, panda2):
        return panda1 in self.pandas[panda2] and \
            panda2 in self.pandas[panda1]

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if self.are_friends(panda1, panda2):
            raise Exception("These cute pandas are already friends.")
        self.pandas[panda1].append(panda2)
        self.pandas[panda2].append(panda1)

    def friends_of(self, panda):
        if self.has_panda(panda):
            return [panda for panda in self.pandas[panda]]
        return False

# BFS отговаря с True или False на въпроса има ли път между две точки.
# Ако графа е с безтегловни ребра можем да намерим най-краткия път между тях.
# Ако имаме тегла използваме Дийкстра алгоритъма (BFS дава грещен резултат).

    def search_for_friends(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not self.has_panda(start) or not self.has_panda(end):
            return False
        shortest = None
        for node in self.pandas[start]:
            if node not in path:
                newpath = self.search_for_friends(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        if shortest is not None:
            return shortest
        return -1

    def connection_level(self, panda1, panda2):
        if self.search_for_friends(panda1, panda2) not in [False, -1]:
            return len(self.search_for_friends(panda1, panda2)) - 1
        return self.search_for_friends(panda1, panda2)

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) not in [False, -1]

    def how_many_gender_in_network(self, search_level, panda, gender):
        if search_level < 1:
            raise Exception("Enter level greater or equal to 1.")
        if gender != "male" and gender != "female":
            raise Exception("Your gender must be male or female.")
        counter, level = 0, 1
        visited = [panda]
        friends = [friend for friend in self.pandas[panda]]
        while level <= search_level:
            for friend in friends:
                if friend not in visited:
                    visited.append(friend)
                    if friend.gender == gender:
                        counter += 1
            friends = [
                friend for panda in friends for friend in self.pandas[panda]]
            level += 1
        return counter

    def get_friends_json(self, panda):
        return [panda.__dict__ for panda in self.pandas[panda]]

    def save(self, file_name):
        result = {}
        for panda in self.pandas:
            data = {}
            data["info"] = panda.__dict__
            data["friends"] = self.get_friends_json(panda)
            result[repr(panda)] = data
        with open(file_name, 'w') as f:
            f.write(json.dumps(result, indent=True))

    def load(self, file_name):
        with open(file_name, 'r') as f:
            data = json.load(f)
        for member in data:
            sexy_panda = Panda(
                data[member]["info"]["name"], data[member]["info"]["email"], data[member]["info"]["gender"])
            try:
                self.add_panda(sexy_panda)
            except:
                pass
            for friend in data[member]["friends"]:
                try:
                    self.make_friends(sexy_panda, Panda(
                        friend["name"], friend["email"], friend["gender"]))
                except:
                    pass
