import re


class Panda():
    def __init__(self, name, email, gender):

        if not isinstance(name, str):
            raise TypeError("Enter a valid name represented as a string.")

        if not isinstance(email, str):
            raise TypeError("Enter a valid email represented as a string")

        if not isinstance(gender, str):
            raise TypeError("We accept only pandas in our community!")

        if gender != "male" and gender != "female":
            raise ValueError("Enter a valid gender (male or female).")

        if not re.match(
                r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            raise Exception("Enter a valid email.")

        self.name = name
        self.email = email
        self.gender = gender

    # def name(self):
    #     return self.name

    # def email(self):
    #     return self.__email

    # def gender(self):
    #     return self.gender

    def isMale(self):
        return self.gender == "male"

    def isFemale(self):
        return self.gender == "female"

    def __str__(self):
        return "My name is {} and I'm a {} panda.".format(
            self.name, self.gender)

    def __repr__(self):
        return "{}, {} panda".format(
            self.name, self.gender)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email \
               and self.gender == other.gender
