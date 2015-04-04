from panda import Panda
import json


class PandaSocialNetwork():
    def __init__(self):
        self.__pandas = {}

    def get_pandas(self):
        return self.__pandas

    def has_panda(self, other):
        return other in self.__pandas

    def add_panda(self, other):
        if isinstance(other, Panda):
            if not self.has_panda(other):
                self.__pandas[other] = []
            else:
                raise Exception("Name is already taken.")
        else:
            raise TypeError("Give me a real panda!")

    def are_friends(self, panda1, panda2):
        return panda1 in self.__pandas[panda2] and \
            panda2 in self.__pandas[panda1]

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
            return [panda.name() for panda in self.__pandas[panda]]
        return False

    def search_for_friends(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not self.has_panda(start) or not self.has_panda(end):
            return False
        shortest = None
        for node in self.__pandas[start]:
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
        friends = [frnd for frnd in self.__pandas[panda]]
        while level <= search_level:
            for friend in friends:
                if friend not in visited:
                    visited.append(friend)
                    if friend.gender() == gender:
                        counter += 1
            friends = [
                frnd for panda in friends for frnd in self.__pandas[panda]]
            level += 1
        return counter

    def get_members(self):
        return [panda for panda in self.__pandas]

    def save(self, members_file, friends_file):
        members = {}
        for member in self.get_members():
            members[member.name()] = member.__dict__
        with open(members_file, "w") as f:
            f.write(json.dumps(members))

        friends = {}
        for panda in self.get_pandas():
            friends[panda.name()] = self.friends_of(panda)
        with open(friends_file, "w") as f:
            f.write(json.dumps(friends))

    def load(self, members_file, friends_file):
        with open(members_file, "r") as f:
            self.members = json.load(f)
        for panda in self.members:
            self.add_panda(Panda(self.members[panda]['_Panda__name'], self.members[panda]['_Panda__email'], self.members[panda]['_Panda__gender']))

        with open(friends_file, "r") as f:
            self.friends = json.load(f)
        for panda in self.friends:
            for friend in self.friends[panda]:
                pand = Panda(self.members[panda]['_Panda__name'], self.members[panda]['_Panda__email'], self.members[panda]['_Panda__gender'])
                pand_fr = Panda(self.members[friend]['_Panda__name'], self.members[friend]['_Panda__email'], self.members[friend]['_Panda__gender'])
                if not self.are_friends(pand, pand_fr):
                    self.make_friends(pand, pand_fr)
