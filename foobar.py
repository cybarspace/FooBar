"""
FooBar data type class
"""

class FooBar:
    """
    FooBar data type class
    """
    def __init__(self, *args):
        """
        Constructor
        """
        self.foo_dict = {}
        def temp_iter(self):
            for item in args:
                yield {args.index(item): item}
        self.foo_dict.update(temp_iter())
        self.foo_values = set(self.iterator())

    def index(self, item):
        return self.foo_dict.values().index(item)

    def iterator(self):
        for i in self.foo_dict:
            yield self.foo_dict[i]

    def __getitem__(self, pos):
        assert isinstance(pos, int), "Parameter 'pos' must be of type 'int'"
        try:
            return self.foo_dict[pos]
        except KeyError:
            raise IndexError("FooBar index out of range")
            return None

    def __iter__(self):
        return self.foo_dict

    def __contains__(self, item):
        return item in self.foo_values

    def __len__(self):
        return len(self.foo_dict)

    def __eq__(self, other):
        assert isinstance(
            other, FooBar
        ), f"Cannot compare foobar with {type(other)} object"
        return self.foo_dict == other.foo_dict

    def __str__(self):
        return f"([{', '.join(str(item) for item in self.foo_dict)}])"

    def __repr__(self):
        return f"FooBar Object Containing: {self.__str__()}"

    def __set__(self):
        return self.foo_values

    def __list__(self):
        return self.foo_dict.values()

    def __tuple__(self):
        return tuple(self.__list__())
