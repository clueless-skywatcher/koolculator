from koolculator.numculator import EratoSieve
import random

sieve = EratoSieve()

def nth_prime(n):
	'''
	Returns the nth prime number. Equivalent to invoking
	sieve.nthprime(n)
	---------------------------------------------------
	Usage:
	>>> from koolculator.numculator import prime
	>>> prime.nth_prime(15)
	47
	---------------------------------------------------
	'''
	if n == 0:
		return
	return sieve.nthprime(n)

def prime_range(a, b):
	'''
	Returns a range of primes from a to b (inclusive). 
	Equivalent to invoking sieve.primes(a, b)
	---------------------------------------------------
	Usage:
	>>> from koolculator.numculator import prime
	>>> prime.primes(10, 20)
	[11, 13, 17, 19]
	---------------------------------------------------
	'''
	if a >= b:
		print("Give proper range as input")
		return
	return sieve.primes(a, b)

def isprime(x):
	'''
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
	'''
	if x == 0 or x == 1:
		return
	return sieve.is_prime(x)

def random_prime(a, b):
	'''
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
	'''
	if a >= b:
		print("Give proper range as input")
		return

	prime_list = prime_range(a, b)
	if len(prime_list) == 0:
		return
	rand = random.randint(0, len(prime_list) - 1)
	return prime_list[rand]