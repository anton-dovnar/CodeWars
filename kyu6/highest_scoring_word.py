def high(x):
    highest_score = (0, '')
    for word in x.split():
        score = sum(map(lambda x: ord(x) - 96, word))
        if score > highest_score[0]:
            highest_score = score, word
    return highest_score[1]
