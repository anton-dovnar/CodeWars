import re
from collections import Counter


def top_3_words(text):
    text = re.findall(r"'*[a-z][a-z']*", text.lower())
    return [w for w, _ in Counter(text).most_common(3)]
