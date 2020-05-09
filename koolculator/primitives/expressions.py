import types
import numbers
import operator
import heapq

def getOperator(op):
    return {
        '+' : (operator.add, 2),
        '-' : (operator.sub, 1),
        '*' : (operator.mul, 3),
        '/' : (operator.truediv, 4),
        '^' : (operator.pow, 5),
        '(' : (None, 6)
    }[op]



if __name__ == '__main__':
    s = '3*x^2+6*x'
    print(s)
