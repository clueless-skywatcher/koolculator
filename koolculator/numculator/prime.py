from koolculator.numculator import EratoSieve
import random

sieve = EratoSieve()

def nth_prime(n):
	"""
	Returns the nth prime number. Equivalent to invoking
	sieve.nthprime(n)
	---------------------------------------------------
	Usage:
	>>> from koolculator.numculator import prime
	>>> prime.nth_prime(15)
	47
	---------------------------------------------------
	"""
	if n == 0:
		return
	return sieve.nthprime(n)

def prime_range(a, b):
	"""
	Returns a range of primes from a to b (inclusive). 
	Equivalent to invoking sieve.primes(a, b)
	---------------------------------------------------
	Usage:
	>>> from koolculator.numculator import prime
	>>> prime.prime_range(10, 20)
	[11, 13, 17, 19]
	---------------------------------------------------
	"""
	if a >= b:
		print("Give proper range as input")
		return
	return sieve.primes(a, b)

def isprime(x):
	"""
	Checks if a number x is prime or not. Equivalent to
	invoking sieve.is_prime(x)
	--------------------------------------------------
	Usage:
	>>> from koolculator.numculator import prime
	>>> prime.isprime(28)
	False
	>>> prime.isprime(37)
	True
	--------------------------------------------------
	"""
	if x == 0 or x == 1:
		return
	return sieve.is_prime(x)

def random_prime(a, b):
	"""
	Returns a random prime number in the range [a, b]
	(inclusive). According to Bertrand's postulate, this
	is guaranteed to give a result for ranges of the form
	[n, 2*n].
	----------------------------------------------------
	Usage:
	>>> prime.random_prime(25, 28)
	>>> prime.random_prime(28, 95)
	47
	----------------------------------------------------
	"""
	if a >= b:
		print("Give proper range as input")
		return

	prime_list = prime_range(a, b)
	if len(prime_list) == 0:
		return
	rand = random.randint(0, len(prime_list) - 1)
	return prime_list[rand]

def primorial(n):
	"""
	Returns the product of the first n primes
	-----------------------------------------
	Usage:
	>>> prime.primorial(25)
	2305567963945518424753102147331756070
	>>> prime.primorial(1)
	2
	-----------------------------------------
	"""
	if n < 1:
		return 1
	prod = 1
	for i in range(1, n + 1):
		prod *= nth_prime(i)

	return prod

def natural_primorial(n):
	"""
	Returns the product of all the primes less than
	or equal to n
	-----------------------------------------------
	Usage:
	>>> prime.natural_primorial(25)
	223092870
	>>> prime.natural_primorial(1)
	1
	-----------------------------------------------
	"""
	if n <= 1:
		return 1
	prod = 1
	primelist = prime_range(1, n)
	for prime in primelist:
		prod *= prime

	return prod