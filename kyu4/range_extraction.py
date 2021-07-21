def solution(args):
    result = []
    stack = []
    args = [float('inf'), *args, float('inf')]

    for index in range(1, len(args)-1):
        if abs(args[index] - args[index+1]) == 1:
            stack.append(str(args[index]))
        else:
            result.extend(extract(args, stack, index))

    if stack:
        result.extend(extract(args, stack, index))
    return ','.join(result)

def extract(args, stack, index):
    range_extraction = []
    stack.append(str(args[index]))

    if len(stack) > 2:
        range_extraction.append(f"{stack[0]}-{stack[-1]}")
    elif len(stack) == 1:
        range_extraction.append(stack[0])
    else:
        range_extraction.extend(stack)
    stack.clear()

    return range_extraction
