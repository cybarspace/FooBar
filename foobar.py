# FooBar data type class
class FooBar:
    def __init__(self, iterable):
        self.foo_dict = {}
        join_pos = len(self.foo_dict)
        for item in iterable:
            self.foo_dict.update({join_pos: item})
            join_pos += 1

    """ def __add__(self, other):
        assert isinstance(other, FooBar)
        sum_bar = FooBar(self)
        for item in other:
            sum_bar.addfoo(item)
        return sum_bar """

    def get(self, pos):
        assert isinstance(pos, int)
        return self.__getitem__(pos)

    def index(self, item):
        return self.foo_dict.values().index(item)

    def values(self):
        return self.foo_dict.values()

    def __getitem__(self, pos):
        assert isinstance(pos, int)
        return self.foo_dict.get(pos)

    def __iter__(self):
        return self.foo_dict.values()

    def __contains__(self, item):
        if item in set(self.foo_dict.values()):
            return True
        return False

    def __len__(self):
        return len(self.foo_dict)

    def __repr__(self):
        return f"FooBar Object Containing: {self.__str__()}"

    def __str__(self):
        return f"[{', '.join(str(item) for item in self.foo_dict)}]"

    def __list__(self):
        return self.foo_dict.values()

    def __eq__(self, other):
        assert isinstance(other, FooBar)
        return (
            len(set(self.foo_dict.values()) - set(other.foo_dict.values())) == 0
        )
