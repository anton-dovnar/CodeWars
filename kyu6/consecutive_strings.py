def longest_consec(strarr, k):
    if not strarr or k > len(strarr) or k <= 0:
        return ""

    longest = ''
    for i in range(len(strarr)):
        temp_string = ''.join(strarr[i:i+k])
        if len(temp_string) > len(longest):
            longest = temp_string
    return longest
