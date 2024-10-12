import re
import operator


def evaluate_expression(left, sign, right):
    rules = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    return rules[sign](left, right)


def has_leading_zero(parts):
    return any(
        (lambda x: x.startswith("0") and len(x) > 1)(part.strip("-"))
        for part in parts
    )


def solve_runes(runes):
    expression, answer = runes.split("=")

    parts = re.split(r"(?<!^)([*/+-])", expression, maxsplit=1)
    left_operand, sign, right_operand = parts
    
    for digit in range(10):
        if str(digit) in runes:
            continue
        
        left = left_operand.replace("?", str(digit))
        right = right_operand.replace("?", str(digit))
        answ = answer.replace("?", str(digit))
        
        if digit == 0 and has_leading_zero([left, right, answ]):
            continue
        
        try:
            left_num = int(left)
            right_num = int(right)
            answ_num = int(answ)
        except ValueError:
            continue
        
        if evaluate_expression(left_num, sign, right_num) == answ_num:
            return digit
    
    return -1
