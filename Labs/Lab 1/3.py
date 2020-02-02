class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a), (self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.a + self.b * other.b)

    def __repr__(self):
        if self.b == 0:
            return str(self.a)
        elif self.a == 0:
            return str(self.b) + "i"
        elif self.b < 0:
            return str(self.a) + " - " + str(abs(self.b)) + "i"
        return str(self.a) + " + " + str(self.b) + "i"


cp1x1 = Complex(5, 2)
print(cp1x1)

cp1x2 = Complex(3, 3)
print(cp1x2)

print(cp1x1 + cp1x2)

print(cp1x1 - cp1x2)

print(cp1x1 * cp1x2)

print(cp1x1)
print(cp1x2)
