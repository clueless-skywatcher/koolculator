import kctypes

# "===" implies "congruent to"

def euclideanGCD(a, b):
    '''
    Calculates the GCD of a and b using Euclidean algorithm
    '''
    if abs(a) < abs(b):
        return  euclideanGCD(b, a)
    if b == 0:
        return a
    return euclideanGCD(b, a % b)

def extendedEuclideanGCD(a, b):
    '''
    Calculates the Bezout coefficients of a and b alongwith their GCD
    '''

    so, sn = 1, 0
    to, tn = 0, 1

    ro, rn = a, b

    while rn != 0:
        q = ro // rn
        rn, ro = ro - rn * q, rn
        sn, so = so - sn * q, sn
        tn, to = to - tn * q, tn

    return so, to, ro

def modularInverse(n, p):
    '''
    Calculates the modular inverse of n modulo p
    :param n: The number whose inverse is to be found
    :param p: With modulo
    :return: Value of x such that nx === 1 mod p
    '''

    x, y, gcd = extendedEuclideanGCD(n, p)
    return x % p


if __name__ == '__main__':
    print(modularInverse(3, 11))