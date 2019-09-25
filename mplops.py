from math import *
from kctypes import *

def subvar(expr, x: Var, y: Var):
    '''
    Substitutes every symbol 'x' in a given expression "expr"
    with the symbol 'y'
    '''
    if isinstance(expr, Var):
        if expr == x:
            return y
    if isinstance(expr, MulVar):
        if expr.var == x:
            return MulVar(subvar(expr.co, x, y), y)
    if isinstance(expr, Add):
        return subvar(expr.left, x, y) + subvar(expr.right, x, y)
    return expr
