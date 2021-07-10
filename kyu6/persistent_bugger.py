def persistence(n, count=0):
    if n < 10:
        return count

    multiplication = None
    while n:
        last_digit = n % 10
        if isinstance(multiplication, int):
            multiplication *= last_digit
        else:
            multiplication = last_digit
        n //= 10

    count += 1
    return persistence(multiplication, count)
