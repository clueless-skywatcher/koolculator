import types

class Expression:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.value = None

    def getExp(self):
        return '(' + str(self.getExp(self.left)) + str(self.value) + str(self.getExp(self.right)) + ')'


def parseExpression(s, current = Expression()):
    for x in s:
        if x == '(':
            current.left = Expression()
            current.left.parent = current
            current = current.left
        elif x == ')':
            current = current.parent
        elif types.isAtom(x):
            current.value = str(x)
            current = current.parent
        else:
            current.value = str(x)
            current.right = Expression()
            current = current.right

    return current

if __name__ == '__main__':
    s = '3 * (x ^ 2) + 6 * x'
    e = parseExpression(s)
    print(e.getExp())
