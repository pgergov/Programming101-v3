from soldier import Soldier


class Hero(Soldier):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        if not isinstance(name, str):
            raise TypeError("Name must be string")

        if not isinstance(title, str):
            raise TypeError("Title must me string")

        if not isinstance(mana_regeneration_rate, int):
            raise TypeError("Mana_regeneration_rate must be integer")
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        self.__max_mana = mana
        self.damage = 0

    def __str__(self):
        return "Hero(hp:{}, mana:{})".format(self.health, self.mana)

    def __hash__(self):
        return hash(self.__str__())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def known_as(self):
        return "{} the {}".format(self.name, self.title)
