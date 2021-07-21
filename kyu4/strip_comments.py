import re


def solution(string, markers):
    new_line = True if string.endswith('\n') else False
    for marker in markers:
        pattern = r'[ ]?\{}.*(\\n)?'.format(marker)
        string = re.sub(pattern, '', string)
        string.replace(marker, '')
    return string + '\n' if new_line else string
