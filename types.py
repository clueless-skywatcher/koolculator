import numbers
import math

def setVal(x, value):

    '''

    Sets value of given symbol x

    '''

    if isinstance(x, SymbolVar):
        x.val = value
    return True

def isAtom(x):
    '''

    Returns True only if x is an atomic object

    '''

    if isinstance(x, Atom) or isinstance(x, Numeric):
        return True
    else:
        return False

class Atom:
    '''

    Defines an Atomic Data type like Numeric, SymbolVar or Operation

    '''
    val = None

    def __init__(self):
        self.type = 'Atom'
        self.val = None

class SymbolVar(Atom):
    def __init__(self, name):
        self.type = 'SymbolVar'
        self.name = name

    def _holdsValue(self):
        if self.val == None:
            return False
        else:
            return True

class Numeric(Atom, numbers.Number):
    def __init__(self):
        self.type = 'Numeric'

class Fraction(Atom):
    '''
    Although fractions are not fundamentally atomic, they will be taken as
    atomic for specific purposes. I will fix this later.
    '''
    def __init__(self, f):
        l = f.split('/')
        self.num = int(l[0])
        self.den = int(l[1])

    def __repr__(self):
        return "%d/%d" % (self.num, self.den)


if __name__ == '__main__':
    '''
    
    Testing section
    
    '''
    print(Fraction('1/5'))
