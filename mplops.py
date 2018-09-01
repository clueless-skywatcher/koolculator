import types
from math import *

def abs(x):
    '''
    Return absolute value of x
    '''
    return max(x, -x)

def decimEval(x):
    '''
    Evaluate the decimal expression, fraction or trigonometric identity
    '''
    if isinstance(x, types.Fraction):
        return float(x.num) / x.den
    elif isinstance(x, str):
        return 'decimEval(str(x))'
    else:
        return eval(x)

'''
Testing section
'''
if __name__ == '__main__':
    print(types.Fraction('1/56'))
    print(decimEval('sin(95)'))
    print(decimEval('sin(x)'))
