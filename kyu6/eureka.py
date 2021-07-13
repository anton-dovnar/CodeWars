def sum_dig_pow(a, b):
    valid_numbers = []
    for number in range(a, b+1):
        list_of_powers = [int(digit) ** index for index, digit in enumerate(str(number), 1)]
        if sum(list_of_powers) == number:
            valid_numbers.append(number)
    return valid_numbers
