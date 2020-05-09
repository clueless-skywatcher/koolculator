from koolculator.primitives.kctypes import *

def constAddsFromOpDict(opdict):
    l = []
    for x in opdict:
        if x != 'const':
            l.append(Var(x) * opdict[x])
    if 'const' in opdict:
        if opdict['const'] != 0:
            l.append(opdict['const'])
    a = l[0]
    for i in range(1, len(l)):
        a = Add(a, l[i])
    return a


def isSimilar(v1, v2):
    if any(isinstance(x, (BinOp, numbers.Number)) for x in [v1, v2]):
        return False
    if isinstance(v1, Var) and isinstance(v2, MulVar):
        return v1 == v2.var
    if isinstance(v2, Var) and isinstance(v1, MulVar):
        return v2 == v1.var
    if isinstance(v1, MulVar) and isinstance(v2, MulVar):
        return v1.var == v2.var
    return v1 == v2

def constructOpList(op):
    if isinstance(op, (Var, MulVar, numbers.Number)):
        return [op]
    return constructOpList(op.left) + constructOpList(op.right)

def constructOpDict(oplist):
    opdict = OrderedDict()
    for x in oplist:
        if isinstance(x, numbers.Number):
            opdict['const'] = opdict.get('const', 0) + x
        elif isinstance(x, Var):
            opdict[x.name] = opdict.get(x.name, 0) + 1
        elif isinstance(x, MulVar):
            opdict[x.var.name] = opdict.get(x.var.name, 0) + x.co
    return opdict