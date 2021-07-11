def sort_array(source_array):
    odds = [number for number in source_array if number % 2]
    source_array = [number if number % 2 == 0 else None for number in source_array]
    odds = sorted(odds, reverse=True)
    for key, value in enumerate(source_array):
        if value == None and odds:
            source_array[key] = odds.pop()
    return source_array
