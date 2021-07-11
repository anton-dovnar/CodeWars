def decodeMorse(morse_code):
    translate = [MORSE_CODE[code] if code else '' for code in morse_code.split(' ')]
    result = ""
    for value in translate:
        if value == '':
            result += ' '
        else:
            result += value
    return result.replace('  ', ' ').strip()
