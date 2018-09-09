# koolculator
A CAS made from scratch in python on the lines of SymPy.

--> Symbolic Addition Update: (Sep 10, 2018)
Till now implemented the addition of variable symbols together.
Any feedback or bug report will be highly appreciated.

Addition examples:
x = Var('x')

x
Output : x

x + x
Output : 2*x

y = Var('y')

z = Var('z')

x + y
Output : x + y

x + y + y
Output : x + 2*y

x + y + z
Output : x + y + z

x + x + y + z + x + y + z
Output : 3*x + 2*y + 2*z
