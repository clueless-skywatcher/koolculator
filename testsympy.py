from koolculator.primitives.rational import *

if __name__ == '__main__':
	a = RationalFraction(1, 2)
	b = Integer(5)
	c = RationalFraction(25, 60)

	print(kc_rationalize_numexp(RSub(RAdd(a, b, c), c, RPow(b))))