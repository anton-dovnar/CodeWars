def rot13(message):
    cipher = []

    for character in message:
        if character.isalpha():
            case_order = 65 if character.isupper() else 97

            if ord(character) - case_order < 13:
                cipher.append(chr(ord(character) + 13))
            elif ord(character) - case_order > 12:
                cipher.append(chr(ord(character) - 13))
            else:
                cipher.append(chr(ord(character) + 13))
        else:
            cipher.append(character)

    return ''.join(cipher)
