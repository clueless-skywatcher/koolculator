import koolculator.numculator as kcnum

sieve = kcnum.EratoSieve()
n = int(input())
print(f"The {n}th prime is {sieve.nthprime(n)}")