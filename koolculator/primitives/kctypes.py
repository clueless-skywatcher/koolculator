from koolculator.primitives.rational import *
from koolculator.primitives.constants import *
from collections import OrderedDict

class Elementary:
    '''
    Base class for all types
    '''
    def __add__(self, other):
        if other == Zero:
            return self
        if other == self:
            return Mul(Integer(2), self)
        return Add(self, other)
    def __radd__(self, other):
        return other.__add__(self)

    def __mul__(self, other):
        if other == Zero:
            return Zero
        if other == One:
            return self
        return Mul(self, other)

class BinOp(Elementary):
    '''
    Class for binary operations
    '''
    def __init__(self, sym, left, right, rep):
        self.sym = sym
        self.left = left
        self.right = right
        self.rep = rep
    def __repr__(self):
        if isinstance(self.left, BinOp):
            return '({0}) {1} {2}'.format(self.left, self.sym, self.right)
        if isinstance(self.right, BinOp):
            return '{0} {1} ({2})'.format(self.left, self.sym, self.right)
        if isinstance(self.left, BinOp) and isinstance(self.right, BinOp):
            return '({0}) {1} ({2})'.format(self.left, self.sym, self.right)
        return '{0} {1} {2}'.format(self.left, self.sym, self.right)

class Add(BinOp):
    '''
    Class for Addition operation
    '''
    def __new__(cls, left, right, rep = 'Add'):
        # if one of the operands is 0, return the other one
        if left == Zero:
            return right
        if right == Zero:
            return left
        # If the left operand is a number, shift it to the right
        if isinstance(left, (RationalFraction, Integer, int)):
            left, right = right, left
        # if both operands are same, return a product of the operand with 2
        if left == right:
            return Mul(Integer(2), left)
        cls.left = left
        cls.right = right
        cls.rep = rep
        return BinOp.__new__(cls)

    def __init__(self, left, right):
        self.left = left
        self.right = right
        BinOp.__init__(self, '+', left, right, 'Add')

    def __repr__(self):
        return '{0} {1} {2}'.format(self.left, self.sym, self.right)

    def __str__(self):
        return self.__repr__()   

    def __add__(self, other):
        if other == 0:
            return self
        a = constructOpList(Add(Add(self.left, self.right), other))
        dic = constructOpDict(a)
        # things can go bad from here
        return constAddsFromOpDict(dic)

def constAddsFromOpDict(opdict):
    l = []
    for x in opdict:
        if x != 'const':
            l.append(Var(x) * opdict[x])
    if 'const' in opdict:
        if opdict['const'] != Zero:
            l.append(opdict['const'])
    a = l[0]
    for i in range(1, len(l)):
        a = Add(a, l[i])
    return a


def isSimilar(v1, v2):
    if any(isinstance(x, (BinOp, RationalFraction, int, Integer)) for x in [v1, v2]):
        return False
    if isinstance(v1, Var) and isinstance(v2, MulVar):
        return v1 == v2.var
    if isinstance(v2, Var) and isinstance(v1, MulVar):
        return v2 == v1.var
    if isinstance(v1, MulVar) and isinstance(v2, MulVar):
        return v1.var == v2.var
    return v1 == v2

def constructOpList(op):
    if isinstance(op, (Var, MulVar, RationalFraction, int, Integer)):
        return [op]
    return constructOpList(op.left) + constructOpList(op.right)

def constructOpDict(oplist):
    opdict = OrderedDict()
    for x in oplist:
        if isinstance(x, (RationalFraction, int, Integer)):
            opdict['const'] = opdict.get('const', 0) + x
        elif isinstance(x, Var):
            opdict[x.name] = opdict.get(x.name, 0) + 1
        elif isinstance(x, MulVar):
            opdict[x.var.name] = opdict.get(x.var.name, 0) + x.co
    return opdict

class Mul(BinOp):
    '''
    Class for multiplication operation
    '''
    def __new__(cls, left, right, rep = 'Mul'):
        cls.left = left
        cls.right = right
        # if the left operand is a variable exchange the operand positions
        # and make a MulVar instance, otherwise maintain the order of multiplication
        if isinstance(cls.right, (RationalFraction, int, Integer)):
            return MulVar(cls.right, cls.left)
        if isinstance(cls.right, Var):
            return MulVar(cls.left, cls.right)
        return BinOp.__new__(cls)

    def __init__(self, left, right, rep = 'Mul'):
        self.left = left
        self.right = right
        self.rep = rep
        BinOp.__init__(self, '*', left, right, 'Mul')

    def expand(self):
        pass

class MulVar(Elementary):
    '''
    Short for multiplied variable. It denotes a product where
    a single variable is one of the operands
    E.g: 2*x, (x + 1)*x
    '''
    def __init__(self, left, right):
        self.co = left
        self.var = right

    def __add__(self, other):
        if other == 0:
            return self
        #if the other operand is a variable: Eg: 2*x + y
        if isinstance(other, Var):
            # if the other operand is same as the right variable
            # implement a*x + x = (a + 1)*x
            if other == self.var:
                return MulVar(self.co + 1, other)
            else:
                return Add(self, other)
        elif isinstance(other, MulVar):
            if other.var == self.var:
                return MulVar(self.co + other.co, other.var)
            else:
                return Add(self, other)
        else:
            return Add(self, other)

    def __repr__(self):
        if isinstance(self.co, Add):
            return '({0}){1}{2}'.format(self.co, '*', self.var)
        if isinstance(self.var, Add):
            return '{0}{1}({2})'.format(self.co, '*', self.var)
        return '{0}{1}{2}'.format(self.co, '*', self.var)

    def __str__(self):
        return self.__repr__()        

    def __mul__(self, other):
        return MulVar(self, other)

    def __radd__(self, other):
        return other.__add__(self)
    def simplify(self):
        return self

class Var(Elementary):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Var):
            return self.name == other.name
        return False

    def __repr__(self):
        return str(self.name)

    def __add__(self, other):
        if other == 0:
            return self
        if isinstance(other, Var):
            if self.name == other.name:
                return Mul(Integer(2), self)
        if isinstance(other, MulVar):
            if other.var == self:
                return MulVar(other.co + One, other.var)
        return Add(self, other)

    def __mul__(self, other):
        if other == Zero:
            return Zero
        if other == One:
            return self
        return MulVar(other, self)

    def __lt__(self, other):
        if isinstance(other, Var):
            return self.name.__lt__(other.name)
        if isinstance(other, Var):
            return True
        return False

    def __str__(self):
        return self.__repr__()   

    def __hash__(self):
        return hash((self.name, "Var"))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __radd__(self, other):
        return other.__add__(self)

def strrepr(op):
    if isinstance(op, Var):
        return f"Var({op.name})"
    if isinstance(op, MulVar):
        return f"MulVar{op.co, op.var.name}"
    
    return '{}({}, {})'.format(op.rep, strrepr(op.left), strrepr(op.right))

