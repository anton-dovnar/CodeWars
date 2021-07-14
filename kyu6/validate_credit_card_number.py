def validate(n):
    arr = list(map(int, list(str(n))))
    if len(arr) % 2 == 0:
        main = arr[::2]
        secondary = arr[1::2]
    else:
        main = arr[1::2]
        secondary = arr[::2]

    for key, value in enumerate(main):
        expression = value * 2
        if expression > 9:
            expression -= 9
        main[key] = expression

    main.extend(secondary)
    return sum(main) % 10 == 0
