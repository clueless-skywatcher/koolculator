class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return '{0} {1} {2}'.format(self.left, '+', self.right)

    def __add__(self, other):
        if isinstance(other, Var):
            if self.left.name == other.name:
                return Add(Var(self.left.name, coeff = int(self.left.coeff) + int(other.coeff)), self.right)
            else:
                return self.left.__add__(self.right.__add__(other))
        else:
            return Add(self, other)

class Product:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        if isinstance(self.left, int):
            if self.left == 1:
                return str(self.right)
            elif self.left == 0:
                return '0'
        elif isinstance(self.right, int):
            if self.right == 1:
                return str(self.left)
            elif self.right == 0:
                return '0'
        else:
            return '{0}{1}{2}'.format(str(self.left), '*', str(self.right))

class Var:
    def __init__(self, name, coeff = 1):
        self.name = name
        self.coeff = coeff

    def __add__(self, other):
        if isinstance(other, Var):
            if self.name == other.name:
                return Var(self.name, self.coeff + other.coeff)
            else:
                return Add(self, other)
        else:
            return Add(self, other)

    def __repr__(self):
        if self.coeff == 1:
            return self.name
        else:
            return str(self.coeff) + '*' + self.name
