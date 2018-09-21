import numbers

class Numeric(numbers.Number):
    def __init__(self, val):
        self.val = val
        self.ename = 'Numeric'

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other):
        if isinstance(other, Numeric):
            return self.val == other.val
        elif isinstance(other, numbers.Number):
            return self.val == other
        return self.val == other.val

    def __add__(self, other):
        if isinstance(other, Var):
            return Add(self, other)
        if isinstance(other, numbers.Number):
            return Numeric(self.val + other)
        if isinstance(other, Numeric):
            return Numeric(self.val + other.val)
        return Add(self, other)

class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.ename = "BinaryOperation"

    def strrepr(self):
        if isinstance(self.left, BinaryOp):
            return '{0}({1}, {2})'.format(self.ename, self.left.strrepr(), self.right)
        if isinstance(self.right, BinaryOp):
            return '{0}({1}, {2})'.format(self.ename, self.left, self.right.strrepr())
        if isinstance(self.left, BinaryOp) and isinstance(self.right, BinaryOp):
            return '{0}({1}, {2})'.format(self.ename, self.left.strrepr(), self.right.strrepr())
        else:
            return '{0}({1}, {2})'.format(self.ename, self.left, self.right)

class NotVariableException(Exception):
    pass

def varsearch(op, x):
    '''
    Searches op for the name of variable x and returns the variable alongwith its coefficient
    op : Variable or term
    x : Should be a variable. Throws exception if x is not a variable
    '''
    if not isinstance(x, Var):
        raise NotVariableException("Input a variable as a second argument")
    if isinstance(op, numbers.Number):
        return -1
    if isinstance(op, Var):
        if x.name == op.name:
            return op
        else:
            return -1
    else:
        a = varsearch(op.left, x)
        b = varsearch(op.right, x)
        if isinstance(a, Var):
            return a
        elif isinstance(b, Var):
            return b
        else:
            return -1

class Add(BinaryOp):
    '''
    Define a sum with left and right terms
    '''
    def __init__(self, left, right):
        self.left = left
        self.right = right
        if isinstance(left, Numeric):
            self.left, self.right = right, left
        self.ename = "Add"


    def __repr__(self):
        if self.left == 0:
            return self.right
        elif self.right == 0:
            return self.left
        return '{0} {1} {2}'.format(self.left, '+', self.right)

    def __add__(self, other):
        if isinstance(other, Var):
            if isinstance(self.left, Var):
                if self.left.name == other.name:
                    return Add(Var(other.name, self.left.coeff + other.coeff), self.right)
            if isinstance(self.right, Var):
                if self.right.name == other.name:
                    return Add(self.left, Var(other.name, self.right.coeff + other.coeff))
        return self.left.__add__(self.right.__add__(other))

    def __radd__(self, other):
        return other.__add__(self)

    def __mul__(self, other):
        if other == 0:
            return 0
        elif isinstance(other, numbers.Number):
            return Product(other, self)

    def __rmul__(self, other):
        return Product(other, self)


class Product(BinaryOp):
    '''
    Define a product with left and right terms
    '''
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        if isinstance(self.left, numbers.Number):
            if self.left == 1:
                return str(self.right)
            elif self.left == 0:
                return 0
        elif isinstance(self.right, numbers.Number):
            if self.right == 1:
                return str(self.left)
            elif self.right == 0:
                return 0
        else:
            return '{0}{1}{2}'.format(str(self.left), '*', str(self.right))

    def __mul__(self, other):
        if isinstance(self.right, numbers.Number):
            pass



class Var:
    '''
    Class for defining a symbol variable
    Usage:
    >> x = Var('x')
    >> x
    x
    >> y = Var('x', coeff = 2)
    >> y
    2*x

    Arguments:
        name : Name to be held in the variable symbol
        coeff : Coefficient of the variable symbol, by default 1

    We strongly recommend against choosing placeholder names with non-unit coefficients
    to be same as the variable names themselves, i.e we don't recommend using the following type of
    declarations:

    >> x = Var('x', coeff = 2) --> Avoid doing this

    '''

    def __init__(self, name, coeff = 1):
        self.name = name
        self.coeff = coeff
        self.ename = 'Var'

    def __add__(self, other):
        if self.coeff == 0:
            return other
        elif other == 0:
            return self
        elif isinstance(other, Var):
            if self.name == other.name:
                return Var(self.name, self.coeff + other.coeff)
            else:
                return Add(self, other)
        elif isinstance(other, numbers.Number):
            other = Numeric(other)
        return Add(self, other)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if other == 0:
            return 0
        elif isinstance(other, numbers.Number):
            return Var(self.name, coeff = self.coeff * other)
        else:
            return Product(self, other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        if self.coeff == 1:
            return self.name
        else:
            return str(self.coeff) + '*' + self.name

    def __eq__(self, other):
        if isinstance(other, Var):
            if self.name == other.name:
                return self.coeff == other.coeff
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(self, other)

def vars(s):
    '''
    Return symbols provided in string s
    Usage:
    >> x, y, z = vars('x, y, z')
    >> u, v, w = vars('2*x, 4*y, z')
    >> u
    2*x
    >> v
    4*y
    >> w
    z
    '''
    a = s.split(', ')
    l = []
    for i in a:
        if len(i) == 1:
            l.append(Var(i))
        else:
            co = i.split('*')[0]
            nm = i.split('*')[1]
            l.append(Var(nm, co))
    return tuple(l)

# Test code here
if __name__ == '__main__':
    pass
