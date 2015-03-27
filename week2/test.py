# Клас и дефиниции
# dunder = две долни черти ( double underscore )
# Атрибутите описват пандата (дават ѝ характеристики), а методите казват какво тя може да прави.

# Duck Typing - в python нямаме интерфейс (eclipse). Очакваме поведение без да ни интересува какво са ни дали като аргумент.
# Функцията приема като аргумент инстанция, за която е важно да има метода, който искаме. Това е Duck Typing!
class Panda:

    def __init__(self, name): # Конструктор(метод на нашия клас)
        # self-a е нашия this, сочи към класа, към който сме инстанцирали
        self.name = name
        self.weight = 30
        self.age = 0


# Мутиращи методи - след извикване на метода, пандата вече не е същата (друга панда)
    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.weight += amount // 2

    def sleep(self):
        self.weight += 1

    # предефинираме "+" как да работи за нашата панда ( + извиква __add__)
    def __add__(self, other): # other е друга инстанция на Panda()
        return Panda(" ".join([self.name, other.name]))

    # str от обекта извиква __str__
    # следващите два метода вървят ръка за ръка
    def __str__(self):
        return "I am panda {} and i am {} years old".format(self.name, self.age)

    def __repr__(self):
        return self.__str__()


    def __hash__(self):
        return hash(self.name + str(self.weight))

    # eq се извиква когато направим == ( == извиква __eq__)
    def __eq__(self, other):
        return self.name == other.name and self.weight == other.weight


    # int() от обекта извиква __int__
    def __int__(self):
        return self.weight



ivo = Panda("Ivo")
rado = Panda("Rado")
zoo = {}
zoo[ivo] = 1
print(zoo)