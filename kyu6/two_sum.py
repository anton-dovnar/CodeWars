def two_sum(numbers, target):
    hashtable = set(numbers)
    for index, number in enumerate(numbers):
        difference = target - number
        if difference in hashtable:
            return (index, numbers[index+1:].index(difference) + index + 1)
