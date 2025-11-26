class LinkEmpty:
    def __repr__(self):
        return 'Link.empty'

    def filter_link(self, fn):
        return self

    def no_repeat(self):
        return self

LinkEmpty = LinkEmpty()  # 实例化单例

class Link:
    empty = LinkEmpty
    def __init__(self, first, rest=empty):
        self.first = first
        if rest is Link.empty or isinstance(rest, Link):
            self.rest = rest
        else:
            raise TypeError('rest must be Link or Link.empty')

    def __repr__(self):
        if self.rest is Link.empty:
            return f'Link({self.first})'
        return f'Link({self.first}, {repr(self.rest)})'

    def filter_link(self, fn):
        if self is Link.empty:
            return Link.empty
        elif fn(self.first):
            return Link(self.first, self.rest.filter_link(fn))
        else:
            return self.rest.filter_link(fn)

    def no_repeat(self):
        if self is Link.empty:
            return Link.empty
        head = self.first
        new_link = self.rest.filter_link(lambda y: head != y)
        return Link(head, new_link.no_repeat())
s = Link(1, Link(2, Link(2, Link(3))))
print(s.no_repeat())