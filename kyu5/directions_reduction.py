def dirReduc(arr):
    opposit_directions = {
        "WEST": "EAST",
        "EAST": "WEST",
        "NORTH": "SOUTH",
        "SOUTH": "NORTH"
    }
    stack = []
    for direction in arr:
        if stack and stack[-1] == opposit_directions[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack
