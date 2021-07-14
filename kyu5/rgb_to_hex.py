def rgb(r, g, b):
    rgb_list = [r, g, b]
    hex_format = ""

    for key, decimal in enumerate(rgb_list):
        if decimal < 0:
            decimal = 0
        elif decimal > 255:
            decimal = 255

        hex_representation = f"{decimal:02x}".upper()
        hex_format += hex_representation
    return hex_format
