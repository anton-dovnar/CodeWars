def revrot(string, sz):
    if not string or sz == 0:
        return ""

    chunks = []
    for idx in range(0, len(string), sz):
        chunk = string[idx:idx+sz]
        if len(chunk) == sz:
            if sum([int(digit) ** 3 for digit in chunk]) % 2 == 0:
                chunks.append(chunk[::-1])
            else:
                chunks.append(chunk[1:] + chunk[0])
    return "".join(chunks)
