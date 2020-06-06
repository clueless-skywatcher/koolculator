from koolculator.primitives.rational import *
from koolculator.primitives.constants import *

AUTO_EVAL = False

class KCBase():
	def __init__(self):
		self._args = None

	@property
	def args(self):
		return self._args

	def __repr__(self):
		return self.__str__()

class Atomic(KCBase):
	pass

class Operation(KCBase):
	def __init__(self, *args):
		self._args = list(args)
		self.__func_head = self.__class__.__name__

	@property
	def func_head(self):
		return self.__func_head

class Add(Operation):
	def __str__(self):
		return " + ".join([str(arg) for arg in self._args])	
	

	

class Mul(Operation):
	def __str__(self):
		return "*".join([str(arg) for arg in self._args])

	def search_var(self, x):
		if not isinstance(x, Var):
			return False
		return x in self._args

	def separate_rat(self):
		rats = []
		non_rats = []

		for i in self._args:
			if isinstance(i, (RationalFraction, Integer, int)):
				rats.append(kc_rationalize(i))
			if isinstance(i, (Operation, Var)):
				non_rats.append(i)

		return rats, non_rats


	def __add__(self, other):
		return Add(self, other)

class Var(Atomic):
	def __init__(self, name):
		self.name = str(name)

	def __str__(self):
		return self.name

	def __add__(self, other):
		# x + x = 2*x
		if isinstance(other, Var):
			return Mul(2, self)
		

	def __mul__(self, other):
		if isinstance(other, Mul):
			return Mul(self, *other._args)
		return Mul(self, other)

	def __rmul__(self, other):
		return self.__mul__(other)



