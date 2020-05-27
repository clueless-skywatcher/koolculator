import math

class EratoSieve:
	'''
	Class for implementing the Sieve of Eratosthenes
	------------------------------------------------
	Usage:
	--> Generate a sieve of primes upto 25 by default
	>>> sieve = EratoSieve()
	--> Generate a sieve of primes upto 100
	>>> sieve = EratoSieve(100)
	--> Check if a particular number is a prime
	>>> sieve.is_prime(90)
	False
	--> Check if a particular number is in the sieve
	>>> 97 in sieve
	True
	--> Generate the list of primes from 50 to 100
	>>> sieve.primes(50, 100)
	[53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	------------------------------------------------
	Whenever a number n is checked for membership in 
	the sieve, if the number n is beyond the generated
	sieve, the sieve generates all primes upto 1.5
	times the number n. As a result, this is a dynamic
	sieve that generates primes as required.
	'''
	def __init__(self,  upto = 25):
		self._list = [1 for i in range(upto + 1)]
		self._populate_list(upto)
		self._primelist = []

		for i in range(2, len(self._list)):
			if self._list[i] == 1:
				self._primelist.append(i)
		
	def _populate_list(self, upto):
		for i in range(2, int(math.sqrt(upto)) + 1):
			if self._list[i] == 1:
				for j in range(i ** 2, upto + 1, i):
					self._list[j] = 0


	def stretch_to(self, n):
		'''
		Stretches the sieve to include all primes upto n
		------------------------------------------------
		Usage:
		>>> sieve = EratoSieve()
		>>> sieve._primelist
		[2, 3, 5, 7, 11, 13, 17, 19, 23]
		>>> sieve.stretch_to(100)
		>>> sieve._primelist
		[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
		------------------------------------------------
		'''
		prev_upto = len(self._list) - 1
		if n <= prev_upto:
			print("Cannot extend list to less than its length")
			return
		if self._list == []:
			print("Undefined error")
			return
		for i in range(prev_upto + 1, n + 1):
			self._list.append(1)
		self._populate_list(n)
		for i in range(prev_upto + 1, len(self._list)):
			if self._list[i] == 1:
				self._primelist.append(i)

	def is_prime(self, p):
		'''
		Checks if a number is prime by checking it's membership
		in the sieve.
		-------------------------------------------------------
		Usage:
		>>> sieve = EratoSieve()
		>>> sieve.is_prime(25)
		False
		>>> sieve.is_prime(97)
		True
		-------------------------------------------------------
		'''
		return self.__contains__(p)	

	def primes(self, a, b):
		'''
		Find all primes from a to b (inclusive).
		----------------------------------------
		Usage:
		>>> from sieve import EratoSieve
		>>> sieve = EratoSieve()
		>>> sieve.primes(50, 100)
		[53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
		----------------------------------------
		'''
		prime_range = []
		if b > len(self._list) - 1:
			self.stretch_to(int(b * 1.5)) 
		for i in range(len(self._primelist)):
			if self._primelist[i] > b:
				break
			if self._primelist[i] >= a and self._primelist[i] <= b:
				prime_range.append(self._primelist[i])
			
		return prime_range

	def nthprime(self, n):
		'''
		Find the nth prime number. If the nth prime number
		is not present in the sieve, the sieve is extended to
		twice the value of n * log(n).
		Note: The approximate value of the nth prime number is
		deemed to be n * log(n), so it is expected to have the
		nth prime number somewhere between 2 and 2 * n * log(n).
		-----------------------------------------------------
		Usage:
		>>> from sieve import EratoSieve
		>>> sieve = EratoSieve()
		>>> sieve.nthprime(523)
		3761
		-----------------------------------------------------
		'''
		if n > len(self._primelist):
			self.stretch_to(int(2 * n * math.log(n)))
		return self._primelist[n - 1]

	def __contains__(self, n):
		if n > len(self._list) - 1:
			self.stretch_to(int(n * 1.5))
		return n in self._primelist
