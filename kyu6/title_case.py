def title_case(title, minor_words=''):
    if not title:
        return ""

    title = title.lower().capitalize()
    minor_words = set(minor_words.lower().split())
    list_of_words = title.split()

    for key, word in enumerate(list_of_words):
        if word not in minor_words:
            list_of_words[key] = word.title()

    return ' '.join(list_of_words)
