from koolculator.numculator.modulo import gcd_euclid

class RationalNumExpression():
	def __init__(self, *args):
		self.args = list(map(kc_rationalize, args))

	def __repr__(self):
		return self.__str__()

class RAdd(RationalNumExpression):
	def __str__(self):
		return " + ".join([str(arg) for arg in self.args])

class RSub(RationalNumExpression):
	def __str__(self):
		return " - ".join([str(arg) for arg in self.args])	

class RMul(RationalNumExpression):
	def __str__(self):
		return " * ".join([str(arg) for arg in self.args])

class RPow(RationalNumExpression):
	def __str__(self):
		return " ^ ".join([str(arg) for arg in self.args])

class RQuot(RationalNumExpression):
	def __str__(self):
		return " / ".join([str(arg) for arg in self.args])

class Integer(RationalNumExpression, int):
	def __init__(self, val):
		self.val = int(val)

	def __str__(self):
		return str(self.val)

	def __repr__(self):
		return self.__str__()

class Fraction(RationalNumExpression):
	def __new__(cls, a, b):
		if b == 0:
			return Undefined()
		else:
			return object.__new__(cls)

	def __init__(self, a, b):
		self.num = Integer(a)
		self.denom = Integer(b)


class RationalFraction(RationalNumExpression):
	"""
	Class to represent rational fractions
	"""
	def __new__(cls, a, b):
		if b == 0:
			return Undefined()
		if b == 1:
			return Integer(a)
		if a % b == 0:
			return Integer(a // b)
		else:
			return object.__new__(cls)

	def __init__(self, a, b):
		self.num = Integer(a)
		self.denom = Integer(b)
		self._rationalize()

	def _rationalize(self):
		g = gcd_euclid(self.num.val, self.denom.val)
		if self.denom.val > 0:
			self.num = Integer(self.num.val // g)
			self.denom = Integer(self.denom.val // g)
		elif self.denom.val < 0:
			self.num = Integer(-self.num.val // g)
			self.denom = Integer(self.denom.val // g)

	def __str__(self):
		return f"{self.num}/{self.denom}"

	def __repr__(self):
		return self.__str__()

class Undefined(RationalNumExpression):
	def __init__(self):
		pass

	def __str__(self):
		return "Undefined"

	def __repr__(self):
		return self.__str__()

def kc_rationalize(x):
	if not isinstance(x, (int, RationalNumExpression)):
		return NotImplemented
	if isinstance(x, int):
		return Integer(x)
	elif isinstance(x, RationalFraction):
		n = x.num.val
		d = x.denom.val

		if n % d == 0:
			return Integer(n // d)
		else:
			g = gcd_euclid(n, d)
			if d > 0:
				return RationalFraction(Integer(n // g), Integer(d // g))
			elif d < 0:
				return RationalFraction(Integer(-n // g), Integer(d // g))

def kc_rationalize_numexp(x):
	if not isinstance(x, RationalNumExpression):
		return NotImplemented
	exp = kc_rationalize_rec_numexp(x)
	if exp == Undefined():
		return Undefined()
	else:
		return kc_rationalize(exp)

def kc_eval_sum(a, b):
	if not isinstance(a, RationalNumExpression) or not isinstance(b, RationalNumExpression):
		return NotImplemented
	
	if isinstance(a, Integer):
		a = Fraction(a, 1)
	if isinstance(b, Integer):
		b = Fraction(b, 1)

	return RationalFraction(a.num * b.denom + b.num * a.denom, a.denom * b.denom)		 

def kc_eval_diff(a, b):
	if not isinstance(a, RationalNumExpression) or not isinstance(b, RationalNumExpression):
		return NotImplemented
	
	if isinstance(a, Integer):
		a = Fraction(a, 1)
	if isinstance(b, Integer):
		b = Fraction(b, 1)

	return RationalFraction(a.num * b.denom - b.num * a.denom, a.denom * b.denom)


def kc_rationalize_rec_numexp(x):
	if isinstance(x, Integer):
		return x
	elif isinstance(x, RationalFraction):
		if x.denom == 0:
			return Undefined()
		else:
			return x
	elif isinstance(x, RationalNumExpression):
		if len(x.args) == 1:
			exp = kc_rationalize_rec_numexp(x.args[0])
			if exp == Undefined():
				return Undefined()
			elif isinstance(x, RAdd):
				return exp
			elif isinstance(x, RSub):
				return kc_eval_prod(-1, exp)
		elif len(x.args) == 2:
			if isinstance(x, (RAdd, RSub, RMul, RQuot)):
				exp1 = kc_rationalize_rec_numexp(x.args[0])
				exp2 = kc_rationalize_rec_numexp(x.args[1])
				if exp1 == Undefined() or exp2 == Undefined():
					return Undefined()
				else:
					if isinstance(x, RAdd):
						return kc_eval_sum(exp1, exp2)
					if isinstance(x, RSub):
						return kc_eval_diff(exp1, exp2)
					if isinstance(x, RMul):
						return kc_eval_prod(exp1, exp2)
					if isinstance(x, RQuot):
						return kc_eval_quot(exp1, exp2)
			elif isinstance(x, RPow):
				exp = kc_rationalize_rec_numexp(x.args[0])
				if exp is Undefined():
					return Undefined()
				else:
					return kc_eval_pow(exp, x.args[1])
