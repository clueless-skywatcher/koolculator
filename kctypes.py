class Add:
    '''
    Define a sum with left and right terms
    '''
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
    '''
    Define a product with left and right terms
    '''
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

    def __eq__(self, other):
        if isinstance(other, Var):
            if self.name == other.name:
                return self.coeff == other.coeff
            else:
                return False
        else:
            return False

def vars(s):
    '''
    Return symbols provided in string s
    Separate symbols with commas and write coefficients with a '*' sign
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
