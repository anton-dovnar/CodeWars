def iq_test(numbers):
    arr = [int(number) % 2 for number in numbers.split()]
    a = arr.count(1)
    b = arr.count(0)
    return arr.index(0) + 1 if a > b else arr.index(1) + 1
