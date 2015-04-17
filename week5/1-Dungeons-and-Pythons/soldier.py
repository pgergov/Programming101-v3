class Soldier:

    def __init__(self, health, mana):
        if not isinstance(health, int):
            raise TypeError("Health must be integer")

        if not isinstance(mana, int):
            raise TypeError("Mana must be integer")

        self.health = health
        self.mana = mana
        self.__max_hp = health
        self.__max_mana = mana
        self.weapon = None
        self.spell = None

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health > 0

    # Include cast_range in this method!
    def can_cast(self):
        if self.mana == 0:
            return False
        if self.spell is not None:
            if self.mana >= self.spell.get_mana_cost():
                return True
        return False

    def take_damage(self, damage):
        if not isinstance(damage, int) and not isinstance(damage, float):
            raise TypeError("Enter valid damage_points.")
        if self.health - damage < 0:
            self.health = 0
        else:
            self.health -= damage

    def take_mana(self, mana):
        if not isinstance(mana, int):
            raise TypeError("Enter valid mana_points.")
        if self.mana + mana > self.__max_mana:
            self.mana = self.__max_mana
        else:
            self.mana += mana

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

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def has_weapon(self):
        return self.weapon is not None

    def has_spell(self):
        return self.spell is not None

    def attack(self, by=""):
        if by not in ["weapon", "magic"]:
            raise ValueError("Enter valid attack method (weapon or magic)")
        if by == "weapon":
            if self.weapon is not None:
                return self.weapon.get_damage()
        elif by == "magic":
            if self.spell is not None:
                if self.can_cast():
                    self.mana -= self.spell.get_mana_cost()
                    return self.spell.get_damage()
                raise Exception("Not enough mana.")
        return self.damage
