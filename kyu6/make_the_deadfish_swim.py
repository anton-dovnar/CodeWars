def parse(data):
    value = 0
    output = []
    table_of_operations = {
        'i': lambda x: x + 1,
        'd': lambda x: x - 1,
        's': lambda x: x ** 2,
        'o': None,
    }
    for operation in data:
        if operation in table_of_operations:
            if operation == 'o':
                output.append(value)
            else:
                value = table_of_operations[operation](value)
    return output
