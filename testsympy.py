from koolculator.primitives.kctypes2 import *
from sympy import Symbol, srepr

if __name__ == '__main__':
	x = Var('x')
	y = Var('y')
	z = Var('z')
	print(Mul(10, y, RationalFraction(15, 2), z, Add(x, y)).separate_rat())

	# x = Symbol('x')
	# y = Symbol('y')
	# z = Symbol('z')
	# print(10*y**2 + y**2)