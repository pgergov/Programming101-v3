class Fraction:

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __str__(self):
        return "{} / {}".format(self.n, self.d)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.n / self.d == other.n / other.d

    def reducer(self, a, b):
        for i in range(a, 0, -1):
            if b % i == 0 and a % i == 0:
                a /= i
                b /= i
        return int(a), int(b)

    def __add__(self, other):
        down = self.d * other.d
        up = int(self.n * (down / self.d) + other.n * (down / other.d))
        return Fraction(self.reducer(up, down)[0], self.reducer(up, down)[1])

    def __sub__(self, other):
        down = self.d * other.d
        up = int(self.n * (down / self.d) - other.n * (down / other.d))
        if up == 0: return 0
        return Fraction(self.reducer(up, down)[0], self.reducer(up, down)[1])

    def __mul__(self, other):
        up = self.n * other.n
        down = self.d * other.d
        return Fraction(self.reducer(up, down)[0], self.reducer(up, down)[1])

a = Fraction(1, 2)
b = Fraction(2, 4)

print(a == b)

print(a + b)
print(a - b)
print(a * b)
