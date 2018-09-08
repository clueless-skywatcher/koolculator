import abc
import math
import numbers

class BaseClass:
    def __add__(self, other):
        return Add(self, other)

    def __mul__(self, other):
        return Product(self, other)

    def __radd__(self, other):
        return Add(other, self)

    def __rmul__(self, other):
        return Product(other, self)

    def __sub__(self, other):
        return Subtract(self, other)

    def __pow__(self, power):
        return Power(self, power)



class UnaryOperator(BaseClass):
    def __init__(self, symbol, op):
        self.op = op
        self.symbol = symbol

    def __repr__(self):
        return '{0}{1}'.format(self.symbol, self.op)

class BinaryOperator(BaseClass):
    def __init__(self, symbol, left, right):
        self.symbol = symbol
        self.left = left
        self.right = right

    def __repr__(self):
        return '({0} {1} {2})'.format(self.left, self.symbol, self.right)

class Add(BinaryOperator):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        BinaryOperator.__init__(self, '+', left, right)

    def __new__(cls, left, right):
        if left == right:
            return Product(2, left)
        return BinaryOperator.__new__(cls)

    @classmethod
    def flatten(cls, args):




class Product(BinaryOperator):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        BinaryOperator.__init__(self, '*', left, right)

    def __repr__(self):
        return '{0}{1}'.format(self.left, self.right)

    def __new__(cls, left, right):
        if left == right:
            return Power(left, 2)
        return BinaryOperator.__new__(cls)

class Power(BinaryOperator):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        BinaryOperator.__init__(self, '^', left, right)

    def __repr__(self):
        return '{0}^{1}'.format(self.left, self.right)


class Subtract(BinaryOperator):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        BinaryOperator.__init__(self, '-', left, right)

    def __new__(cls, left, right):
        if left == right:
            return '0'
        return BinaryOperator.__new__(cls)


class Atom:
    def __add__(self, other):
        return Add(self, other)

    def __radd__(self, other):
        return Add(other, self)

    def __mul__(self, other):
        return Product(self, other)

    def __rmul__(self, other):
        return Product(other, self)

    def __sub__(self, other):
        return Subtract(self, other)

class Var(BaseClass):
    def __init__(self, name, **assumptions):
        self.name = name
        self.assumptions = assumptions
        self.assumptions['commutative'] = assumptions.get('commutative', True)
        self._purge(assumptions, self)

    def __repr__(self):
        return self.name

    @staticmethod
    def _purge(assumptions, obj = None):
        '''
        Purge any None values, similar to SymPy's _sanitize()
        '''
        for x in assumptions:
            k = assumptions[x]
            if k is None:
                assumptions.pop(x)
            assumptions[x] = bool(k)

    def __eq__(self, other):
        if type(self) == type(other):
            return repr(self) == repr(other)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)





