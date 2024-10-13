from string import printable

def decode(s):
    reserved_chars = set("!@#$%^&*()_+-")
    decoded_result = []

    for index, encoded_char in enumerate(s):
        if encoded_char in reserved_chars:
            decoded_result.append(encoded_char)
            continue

        for original_char in printable:
            test_prefix = "_" * index + original_char
            if encode(test_prefix)[-1] == encoded_char:
                decoded_result.append(original_char)
                break

    return "".join(decoded_result)
