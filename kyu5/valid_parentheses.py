def valid_parentheses(string):
    stack = []
    brackets = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }
    closing = {")", "]", "}", ">"}
    opening = {"(", "[", "{", "<"}
    for character in string:
        if character in opening:
            stack.append(character)
        elif character in closing:
            if not stack or brackets[character] != stack.pop():
                return False

    return not stack
