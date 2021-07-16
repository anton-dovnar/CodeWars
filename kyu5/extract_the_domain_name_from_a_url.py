import re


def domain_name(url):
    return re.sub(r'(http[s]?://)?(www\.)?\b([0-9a-zA-Z\-]+)\b(.)+', r'\g<3>', url)
