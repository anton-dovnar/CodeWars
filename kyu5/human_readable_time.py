def make_readable(seconds):
    seconds_representations = [3600, 60, 1]

    result = []
    for sec_repr in seconds_representations:
        chunk = "%02d" % (seconds // sec_repr)
        result.append(chunk)
        seconds %= sec_repr
    return ":".join(result)
