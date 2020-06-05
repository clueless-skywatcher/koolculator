from koolculator.primitives.kctypes import *

if __name__ == '__main__':
	x = Var('x')
	y = Var('y')
	z = Var('z')
	print(RationalFraction(2, 5) * x + 5 * y + x + z + y + x + 1)