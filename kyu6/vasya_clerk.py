def tickets(people):
    coin25 = coin50 = coin100 = 0
    for coin in people:
        if coin == 100:
            coin100 += 1
            if coin50:
                coin50 -= 1
                coin25 -= 1
            else:
                coin25 -= 3
        elif coin == 50:
            coin50 += 1
            coin25 -= 1
        else:
            coin25 += 1

        if coin25 < 0:
            return "NO"
    return "YES"
