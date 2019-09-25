from kctypes import *
import sympy
from mplops import *

if __name__ == '__main__':
    x = Var('x')
    y = Var('y')
    z = Var('z')
    a = (x + y + 1) * x
    print(subvar(a, x, y))
