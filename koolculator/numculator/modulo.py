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

def chinese_remainder(m, X):
	'''
	Given two lists of integers m = [m1, m2, ..., mn] and
	X = [x1, x2, ..., xn] of same length, and assuming the 
	integers in m are relatively prime, this function returns
	the solution of the system of equations
	x === x1 (mod m1)
	x === x2 (mod m2)
	...
	x === xn (mod mn)
	(where === is the congruence sign), using the Chinese 
	Remainder Theorem. Also for each i, xi < mi must hold.

	The user must provide mutually coprime integers in the list
	m for the algorithm to work properly. Till yet no testing
	functionality has been added to check the coprimality of integers
	in m.

	Algorithm source: Computer Algebra and Symbolic Computation:
	Mathematical Methods by Joel S. Cohen
	------------------------------------------------------------
	Usage:
	>>> from koolculator.numculator import chinese_remainder
	>>> chinese_remainder([3, 4, 5], [1, 2, 4])
	34
	>>> chinese_remainder([5, 7], [1, 3])
	31
	>>> chinese_remainder([99, 97, 95], [49, 76, 65])
	639985
	------------------------------------------------------------
	'''
	if len(m) != len(X):
		print("m and X must be equal in length")
		return

	for mi, xi in zip(m, X):
		if xi > mi:
			print("mi and xi must satisfy xi < mi")
			return

	n = m[0]
	s = X[0]

	for i in range(1, len(m)):
		xi = X[i]
		mi = m[i]

		e = gcd_extended_euclid(n, mi)
		c = e[1]
		d = e[2]

		s = c * n * xi + d * mi * s
		n = n * mi

	return s % n

