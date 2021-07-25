import re
import operator
from functools import reduce


def calc(string):
    parentheses = re.search(r'\([^()]+\)', string)

    while parentheses:
        start, end = parentheses.start(), parentheses.end()
        match = parentheses.group()[1:-1]
        match = re.sub(r'([^\d\s])(\s?--)', '\g<1> ', match)
        expression = evaluate(match).replace('--', '')

        if start == 1 and string[0] == '-' and expression[0] == '-':
            start -= 1
            expression = expression.lstrip('-')

        string = string[:start] + expression + string[end:]
        parentheses = re.search(r'\([^()]+\)', string)

    return float(evaluate(string).replace('--', ''))


def evaluate(string):
    multiply_pattern = re.compile(r'''
        (
        (?P<first_argument>[\-]?\d+([.]\d+(e\-)?\d*)?)
        (\s*\*\s*){1}
        (?P<second_argument>[\-]?\d+([.]\d+(e\-)?\d*)?)
        )
    ''', re.X)
    divide_pattern = re.compile(r'''
        (
        (?P<first_argument>[\-]?\d+([.]\d+(e\-)?\d*)?)
        (\s*\/\s*){1}
        (?P<second_argument>[\-]?\d+([.]\d+(e\-)?\d*)?)
        )
    ''', re.X)
    addition_pattern = re.compile(r'''
        (
        (?P<first_argument>[\-]?\d+([.]\d+(e\-)?\d*)?)
        (\s*\+\s*){1}
        (?P<second_argument>[\-]?\d+([.]\d+(e\-)?\d*)?)
        )
    ''', re.X)
    subtraction_pattern = re.compile(r'''
        (
        (?P<first_argument>[\-]?\d+([.]\d+(e\-)?\d*)?)
        (\s*\-\s*){1}
        (?P<second_argument>[\-]?\d+([.]\d+(e\-)?\d*)?)
        )
    ''', re.X)

    operations = {
        "*": lambda value: calculate(multiply_pattern, value, operator.mul),
        "/": lambda value: calculate(divide_pattern, value, operator.truediv),
        "+": lambda value: calculate(addition_pattern,  value, operator.add),
        "-": lambda value: calculate(subtraction_pattern, value,  operator.sub)
    }

    for sign in re.findall(r'[*/]', string):
        string = operations[sign](string)

    for sign in re.findall(r'(?:[^e-]([+\-]))', string):
        string = operations[sign](string)
    return string


def calculate(pattern, string, action):
    match = re.search(pattern, string)
    if match:
        start, end = match.start(), match.end()
        numbers = [
            float(match.group('first_argument')),
            float(match.group('second_argument'))
        ]
        calculated = reduce(action, numbers)
        string = string[:start] + str(float(calculated)) + string[end:]
    return string


if __name__ == '__main__':
    assert calc("1 + 1") == 2
    assert calc("8/16") == 0.5
    assert calc("3 -(-1)") == 4
    assert calc("2 + -2") == 0
    assert calc("10- 2- -5") == 13
    assert calc("(((10)))") == 10
    assert calc("3 * 5") == 15
    assert calc("-7 * -(6 / 3)") == 14
    assert calc("1 + 2 * 3 * (5 - (3 - 1)) - 8") == 11
    assert calc("-(-1)") == 1
    assert calc("-(-(-1))") == -1
    assert calc("(-18) + (54 - 38 * (1)) * (-71 - -(((-(-93 * 92)))) + -45)") == 135022
    assert calc("57 / -54 / -75 / 74 / 14 / -80 * 75 * -17") == 0.00021651115401115402
    assert calc("-63 / -73 / 38 / -82 / -75 + -74 - 31 * 68") == -2181.9999963071728
    assert calc("-(-60) - (-3 / 69 + -(76)) - (52 * -(((-(-1 * 52)))) - -27)") == 2813.0434782608695
    assert calc("-(-34) * (-74 - -97 - -(46)) + (31 - ((((40 - 80)))) / -40)") == 2376.0
    assert calc("(27) + (-27 + -28 + (60)) * (60 / -((((79 - 84)))) - 25)") == -38
    assert calc("-(38) + (-47 * -39 / -(53)) + (96 + -((((-52 + 15)))) - 9)") == 51.41509433962264
    assert calc("-(-61) * (-88 * 48 - (97)) / (-52 - -(((-(-43 * -56)))) + -11)") == 106.66976932416026
    assert calc("-(50) / (53 + -19 - (48)) / (-17 / -(((-(59 * 92)))) + -11)") == -0.3245829097649944
