import koolculator as kc

if __name__ == '__main__':
    x = kc.Var('x')
    y = kc.Var('y')
    z = kc.Var('z')
    a = (x + y + 1) * (x + 1)
    print(kc.strrepr(a))