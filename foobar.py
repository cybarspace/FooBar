# FooBar data type class
class FooBar:
    def __init__(self, *args):
        self.foo_dict = {}
        for item in args:
            self.addfoo(item)

    def __add__(self, other):
        assert isinstance(other, FooBar)
        return self.addbar(other)

    def addfoo(self, item):
        join_index = len(self.foo_dict)
        self.foo_dict.update({join_index: item})

    def addbar(self, other):
        assert isinstance(other, FooBar)
        tempbar = self.foobar(self)
        for item in other:
            tempbar.addfoo(item)
        return tempbar

    def __getitem__(self, index):
        assert isinstance(index, int)
        return self.foo_dict.get(index)

    def __setitem__(self, index, value):
        assert isinstance(index, int)
        self.foo_dict.update({index: value})

    def __delitem__(self, index):
        assert isinstance(index, int)
        self.foo_dict.pop(index)

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
