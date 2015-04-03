from panda import Panda


class PandaSocialNetwork():

    def __init__(self):
        self.__pandas = {}

    def pandas(self):
        return self.__pandas

    def has_panda(self, other):
        return other in self.__pandas

    def add_panda(self, other):
        if isinstance(other, Panda):
            if not self.has_panda(other):
                self.__pandas[other] = []
            else:
                raise Exception("Name is already taken")
        else:
            raise TypeError("Give me a real panda!")

    def are_friends(self, panda1, panda2):
        return panda1 in self.__pandas[panda2] \
                    and panda2 in self.__pandas[panda1]

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if self.are_friends(panda1, panda2):
            raise Exception("These cute pandas are already friends.")
        self.__pandas[panda1].append(panda2)
        self.__pandas[panda2].append(panda1)

    def friends_of(self, panda):
        if self.has_panda(panda):
            return self.__pandas[panda]
        return False

    def search_for_friends(self, panda1, panda2):
        level = 1
        friends = [1, 0]
        visited = []
        que = [panda1]
        while len(que) != 0:
            current = que.pop(0)
            if current not in visited:
                visited.append(current)
                if panda2 in self.__pandas[current]:
                    return level
                else:
                    friends[level - 1] -= 1
                for panda in self.__pandas[current]:
                    if panda not in visited:
                        friends[level] += 1
                        que.append(panda)
                if friends[level - 1] == 0:
                    level += 1
                    friends.append(0)
        return -1

    def connection_level(self, panda1, panda2):
        if not self.has_panda(panda1) or not self.has_panda(panda2):
            return False
        return self.search_for_friends(panda1, panda2)

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) not in [False, -1]

    def how_many_gender_in_network(self, search_level, panda, gender):
        if search_level < 1:
            raise ValueError("Enter level greater or equal to 1.")
        level = 1
        friends = [1, 0]
        visited = []
        que = [panda]
        counter = 0
        while len(que) != 0:
            current = que.pop(0)
            if current not in visited:
                visited.append(current)
                friends[level - 1] -= 1
                for panda in self.__pandas[current]:
                    if panda not in visited:
                        friends[level] += 1
                        que.append(panda)
                        if panda.gender() == gender:
                            counter += 1
                if friends[level - 1] == 0:
                    if level == search_level:
                        return counter
                    level += 1
                    friends.append(0)
        return counter
