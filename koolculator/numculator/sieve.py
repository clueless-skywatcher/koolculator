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
	------------------------------------------------
	Whenever a number n is checked for membership in 
	the sieve, if the number n is beyond the generated
	sieve, the sieve generates all primes that are 1.5
	times the number n. As a result, this is a dynamic
	sieve that generates primes as you go
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
		return self.__contains__(p)	

	def primes(self, a, b):
		prime_range = []
		if b > len(self._list) - 1:
			self.stretch_to(int(b * 1.5)) 
		for i in range(len(self._primelist)):
			if self._primelist[i] >= a:
				start = i
				break
		while self._primelist[start] <= b:
			prime_range.append(self._primelist[start])
			start += 1

		return prime_range

	def nthprime(self, n):
		if n > len(self._primelist):
			self.stretch_to(int(2 * n * math.log(n)))
		return self._primelist[n - 1]

	def __contains__(self, n):
		if n > len(self._list) - 1:
			self.stretch_to(int(n * 1.5))
		return n in self._primelist

if __name__ == '__main__':
	sieve = EratoSieve()
	print(sieve.primes(10, 100))
	