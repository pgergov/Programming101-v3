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
            raise ValueError("You are not normal!")

        if not re.match(
                r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            raise Exception("Enter a valid email.")

        self.__name = name
        self.__email = email
        self.__gender = gender

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def isMale(self):
        return self.__gender == "male"

    def isFemale(self):
        return self.__gender == "female"

    def __str__(self):
        return "My name is {} and I'm a {} panda.".format(
            self.__name, self.__gender)

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(
            self.__name, self.__email, self.__gender)

    def __hash__(self):
        return hash(self.name())

    def __eq__(self, other):
        return self.name() == other.name() and self.email() == other.email() \
               and self.gender() == other.gender()
