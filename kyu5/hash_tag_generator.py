def generate_hashtag(s):
    if not s:
        return False

    s = s.title()
    result = '#' + s.replace(' ', '')
    return result if len(result) <= 140 else False
