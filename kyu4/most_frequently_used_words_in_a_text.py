import re
from collections import Counter

def weight(line):
    items = [
        ord(c) if ord(c) > 96 else ord(c) + 100
        for c in line
    ]
    return sum(items)


def top_3_words(text):
    text = re.findall(r"([\']*(?:[a-z]+[\']+[a-z]+|[a-z]+)[\']*)", text, re.I)
    occurences = Counter(text).most_common()
    return [character.lower() for character, _ in sorted(occurences, key=lambda x: (-x[1], weight(x[0])))][:3]
