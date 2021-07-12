import re
from collections import deque


def generate_bc(url, separator):
    url = re.sub(r'(http[s]?:\/\/)?[^\/]+(?=\/|)', '', url, 1)
    url = re.sub(r'[\.\#\?\=\&].+', '', url, 1)

    link_element = '<a href="/{}">{}</a>'
    span_element = '<span class="active">{}</span>'
    not_allowed = set(["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"])
    links = deque()

    parts = [part for part in url.split('/')[1:] if part]
    previous_address = ''

    if parts and 'index' in parts[-1]:
        parts.pop()

    for key, url in enumerate(parts):
        address_word_representation = url.split('-')

        if len(url) > 30:
            address_word_representation = ''.join([word[0] for word in address_word_representation if word not in not_allowed]).upper()
        else:
            address_word_representation = ' '.join(address_word_representation).upper()

        if key == len(parts) - 1:
            links.append(span_element.format(address_word_representation))
        else:
            current_address = previous_address + url + '/'
            link = link_element.format(current_address, address_word_representation)
            links.append(link)
            previous_address = current_address

    if not links:
        links.append(span_element.format('HOME'))
    else:
        links.appendleft(link_element.format('', 'HOME'))

    return separator.join(links)


if __name__ == '__main__':
    print(generate_bc('https://www.github.com/at-pippi-the-and-kamehameha/uber-research-bioengineering/index.php?source=utm_pippi',  '-'))
