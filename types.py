import numbers
import math
import abc

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
    def __init__(self, f):
        l = f.split('/')
        self.num = int(l[0])
        self.den = int(l[1])

    def __repr__(self):
        return "%d/%d" % (self.num, self.den)

class TrigId:
    def __init__(self, x):
        self.func_name = eval(x.split('(')[0])
        self.op = x.split('(')[1].split(')')[0]

    def __repr__(self):
        return self.func_name.__name__ + '(' + self.op + ')'


if __name__ == '__main__':
    '''
    
    Testing section
    
    '''
    print(Fraction('1/5'))
    print(TrigId('math.sin(x)'))
