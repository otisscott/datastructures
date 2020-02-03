class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0]*d
        else:
            self.coords = d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __mul__(self, other):
        if isinstance(other, Vector):
            total = 0
            for coord in range(len(self.coords)):
                total += self.coords[coord] * other.coords[coord]
            return total
        else:
            d = []
            for coord in range(len(self.coords)):
                d.append(self.coords[coord] * other)
            return Vector(d)

    def __rmul__(self, other):
        return Vector([self.coords[i] * other for i in range(len(self))])

    def __neg__(self):
        d = []
        for coord in range(len(self.coords)):
            d.append(self.coords[coord] * -1)
        return Vector(d)

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<'+str(self.coords)[1:-1]+'>'

    def __repr__(self):
        return str(self)
