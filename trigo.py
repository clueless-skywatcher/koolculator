import types
import math

class Sin(types.TrigId):
    def __init__(self, x):
        self.func_name = math.sin
        self.op = x

    def __repr__(self):
        return