import re
import operator
from functools import reduce


class Calculator(object):
    def evaluate(self, string):
        parentheses = re.search(r'(\([^_]+\))', string)
        final = None
        if parentheses:
            start = parentheses.start()
            end = parentheses.end()
            content = re.findall(r'[^\(\)]+', string[start:end])
            mid = len(content) // 2
            left = mid - 1
            right = mid + 1
            expression = content[mid].strip()

            while left > -1 and right < len(content):
                expression = self.assess(expression)
                expression = content[left] + expression + content[right]
                left -= 1
                right += 1

            expression = self.assess(expression).strip()
            final = string[:start] + expression + string[end:]
        return float(self.assess(final)) if final else float(self.assess(string))

    def assess(self, string):
        multiply_pattern = r'([\-]?\d+([.]\d+)?(\s+\*\s+){1}[\-]?\d+([.]\d+)?)'
        divide_pattern = r'([\-]?\d+([.]\d+)?(\s+\/\s+){1}[\-]?\d+([.]\d+)?)'
        addition_pattern = r'([\-]?\d+([.]\d+)?(\s+\+\s+){1}[\-]?\d+([.]\d+)?)'
        subtraction_pattern = r'([\-]?\d+([.]\d+)?(\s+\-\s+){1}[\-]?\d+([.]\d+)?)'

        operations = {
            "*": lambda value: self.calculate(multiply_pattern, value, operator.mul),
            "/": lambda value: self.calculate(divide_pattern, value, operator.truediv),
            "+": lambda value: self.calculate(addition_pattern,  value, operator.add),
            "-": lambda value: self.calculate(subtraction_pattern, value,  operator.sub)
        }

        for sign in re.findall(r'[*/]', string):
            string = operations[sign](string)

        for sign in re.findall(r'[+\-]', string):
            string = operations[sign](string)
        return string

    def calculate(self, pattern, string, action):
        match = re.search(pattern, string)
        if match:
            start = match.start()
            end = match.end()
            numbers = []

            for element in string[start:end].split():
                try:
                    number = float(element)
                    numbers.append(number)
                except ValueError:
                    print("Not a number")

            calculated = reduce(action, numbers)
            string = string[:start] + str(float(calculated)) + string[end:]
        return string
