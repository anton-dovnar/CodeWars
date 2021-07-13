def solution(s):
    result = [s[i:i+2] for i in range(0, len(s)-1, 2)]
    if len(s) % 2 == 0:
        return result
    return result + [f"{s[-1]}_"]
