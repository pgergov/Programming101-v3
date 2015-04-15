class Hero:

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.__max_hp = health
        self.__max_mana = mana
        self.weapon = None
        self.spell = None

    def __str__(self):
        return "{} - hp:{} mana:{}".format(self.name, self.health, self.mana)

    def __hash__(self):
        return hash(self.__str__())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health != 0

    # Add this method!
    def can_cast(self):
        pass

    def take_damage(self, damage):
        if not isinstance(damage, int) and not isinstance(damage, float):
            raise TypeError("Enter valid damage_points.")
        if self.health - damage < 0:
            self.health = 0
        self.health -= damage

    def take_healing(self, heal):
        if not self.is_alive():
            return False
        if not isinstance(heal, int):
            raise TypeError("Enter valid healing_points.")
        if self.health + heal > self.__max_hp:
            self.health = self.__max_hp
        else:
            self.health += heal
        return True

    def take_mana(self, mana):
        # Add regeneration if the hero moves
        if not isinstance(mana, int):
            raise TypeError("Enter valid healing_points.")
        if self.mana + mana > self.__max_mana:
            self.mana = self.__max_mana
        else:
            self.mana += mana

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by=""):
        if by == "weapon":
            pass
        elif by == "magic":
            pass
        else:
            raise ValueError("Enter valid attack method (weapon or magic)")
        # return damage

# hero = Hero("Ahri", "Dragonslayer", 100, 100, 2)
# print(hero.__dict__)