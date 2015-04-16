class Weapon:
    def __init__(self, name, damage):
        if not isinstance(name, str):
            raise TypeError

        if not isinstance(damage, int):
            raise TypeError

        self.name = name
        self.__damage = damage

    def get_damage(self):
        return self.__damage


class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        if not isinstance(name, str):
            raise TypeError

        if not isinstance(damage, int):
            raise TypeError

        if not isinstance(mana_cost, int):
            raise TypeError

        if not isinstance(cast_range, int):
            raise TypeError

        self.name = name
        self.__damage = damage
        self.__mana_cost = mana_cost
        self.__cast_range = cast_range

    def get_damage(self):
        return self.__damage

    def get_mana_cost(self):
        return self.__mana_cost

    # Add cast_range stuff for the dungeon
    def get_cast_range(self):
        return self.__cast_range
