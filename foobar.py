# FooBar data type class
class FooBar:
    def __init__(self, *args):
        self.foo_dict = {}
        for item in args:
            self.foo_dict.update({args.index(item): item})
        self.foo_set = set(self.foo_dict.values())

    def index(self, item):
        return self.foo_dict.values().index(item)

    def iterator(self):
        for i in self.foo_dict.keys():
            yield self.foo_dict[i]

    def __getitem__(self, pos):
        assert isinstance(pos, int), "Parameter 'pos' must be of type 'int'"
        return self.foo_dict.get(pos)

    def __iter__(self):
        return self.foo_dict

    def __contains__(self, item):
        return item in self.foo_set

    def __len__(self):
        return len(self.foo_dict)

    def __repr__(self):
        return f"FooBar Object Containing: {self.__str__()}"

    def __str__(self):
        return f"([{', '.join(str(item) for item in self.foo_dict)}])"

    def __list__(self):
        return self.foo_dict.values()

    def __eq__(self, other):
        assert isinstance(
            other, FooBar
        ), f"Cannot compare foobar with {type(other)} object"
        return self.foo_dict.values() == other.foo_dict.values()
