class FooBar:
    def __init__(self, *args):
        self.foo_dict = {}
        for item in args:
            self.addfoo(item)

    def __add__(self, other):
        return addbar(other)

    def addfoo(self, item):
        join_index = len(self.foo_dict)
        self.foo_dict.update({join_index: item})

    def addbar(self, other):
        tempbar = foobar(self)
        for item in other:
            tempbar.addfoo(item)
        return tempbar

    def __getitem__(self, key):
        assert isinstance(key, int)
        return self.foo_dict.get(key)

    def __setitem__(self, key, value):
        assert isinstance(key, int)
        self.foo_dict.update({key: value})

    def __delitem__(self, key):
        assert isinstance(key, int)
        self.foo_dict.pop(key)

    def __iter__(self):
        return self

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
