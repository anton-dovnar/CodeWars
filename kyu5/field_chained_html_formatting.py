class Format:
    tags = frozenset(('div', 'h1', 'p', 'span'))

    def __init__(self, chained={}):
        self.chained = chained.get('chained', [])

    def __getattr__(self, attribute):
        return Format({'chained': self.chained.__add__([attribute])})

    def __call__(self, *args):
        result = ''.join(args)
        for tag in reversed(self.chained):
            result = f'<{tag}>{result}</{tag}>'
        return result


format = Format()

if __name__ == '__main__':
    assert format.div("Foo") == "<div>Foo</div>"
    assert format.div.h1("Foo") == "<div><h1>Foo</h1></div>"
    assert format.div("Foo", "Bar") == "<div>FooBar</div>"
    assert format.h1("bu") == "<h1>bu</h1>"
    assert format.p("bu") == "<p>bu</p>"
    assert format.div.p.span("frj") == '<div><p><span>frj</span></p></div>'
