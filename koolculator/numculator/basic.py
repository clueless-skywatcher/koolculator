import math

def gcd_euclid(a, b):
	'''
	Returns the GCD of a and b using Euclid's
	algorithm
	--------------------------------------------------------
	Usage:
	>>> from koolculator.numculator.basic import gcd_euclid
	>>> gcd_euclid(45, 18)
	9
	--------------------------------------------------------
	'''
	while b != 0:
		r = a % b
		a = b
		b = r
	return int(abs(a))

def gcd_extended_euclid(a, b):
	'''
	Returns the GCD of a and b, and integers m and n such that
	m*a + n*b = gcd(a, b). The output order is (gcd(a, b), m, n).

	Algorithm source: Computer Algebra and Symbolic Computation:
	Mathematical Methods by Joel S. Cohen
	-----------------------------------------------------------------
	Usage:
	>>> from koolculator.numculator.basic import gcd_extended_euclid
	>>> gcd_extended_euclid(45, 18)
	(9, 1, -2)
	-----------------------------------------------------------------
	'''
	mpp, mp, npp, np = 1, 0, 0, 1
	while b != 0:
		q = a // b
		r = a % b
		a, b = b, r
		m = mpp - q * mp
		n = npp - q * np
		mpp = mp
		mp = m
		npp = np
		np = n

	if a >= 0:
		return a, mpp, npp
	else:
		return -a, -mpp, -npp

