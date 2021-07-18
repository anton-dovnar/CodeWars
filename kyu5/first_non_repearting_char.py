def first_non_repeating_letter(string):
    string_lower = string.lower()
    for index, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[index]
    return ""
