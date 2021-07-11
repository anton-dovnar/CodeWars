import operator


class Number:

    def __init__(self, value):
        self.value = value

    def __call__(self, operand=None):
        if operand:
            return operand(self.value)
        else:
            return self.value


class Operator:

    def __init__(self, oper):
        self.oper = oper

    def __call__(self, operand):
        return lambda x: self.oper(x, operand)


zero, one, two, three, four, five, six, seven, eight, nine = [Number(n) for n in range(10)]
times = Operator(operator.mul)
plus = Operator(operator.add)
minus = Operator(operator.sub)
divided_by = Operator(operator.floordiv)
