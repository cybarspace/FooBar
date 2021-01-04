# FooBar data type class
class FooBar:
    def __init__(self, *args):
        self.foo_dict = {}
        for item in args:
            self.addfoo(item)

    def __add__(self, other):
        assert isinstance(other, FooBar)
        sum_bar = FooBar(self)
        for item in other:
            sum_bar.addfoo(item)
        return sum_bar

    def append(self, item):
        self.addfoo(item)

    def addfoo(self, item):
        join_index = len(self.foo_dict)
        self.foo_dict.update({join_index: item})

    def addbar(self, other):
        assert isinstance(other, FooBar)
        self.__add__(other)

    def insert(self, data, index):
        if isinstance(data, Node):
            data = data.data
        if index < 0:
            index = self.size + index
        if index == 0:
            self.add(data)
            return
        elif index > self.size or index < 0:
            raise IndexError("Invalid index given")
        elif index == self.size:
            self.get(index - 1).next = Node(data)
        else:
            current = self.get(index - 1)
            old = current.next
            current.next = Node(data, old)
        self.size += 1

    def get(self, index):
        if index < 0:
            index = self.size + index
        if index == 0:
            return self.head
        elif index > self.size - 1 or index < 0:
            raise IndexError("Invalid index given")
        else:
            current, ind = self.head, 0
            while current:
                if index == ind:
                    return current
                ind += 1
                current = current.next

    def pop(self, index=None):
        if index is None:
            index = self.size - 2
        if index < 0:
            index = self.size + index
        if index == 0:
            rv = self.head
            self.head = self.head.next
        elif index > self.size - 1 or index < 0:
            raise IndexError("Invalid index given")
        else:
            prev = self.get(index - 1)
            rv = prev.next
            prev.next = prev.next.next
        self.size -= 1
        return rv.data

    def update(self, index, item):
        self.__setitem__(index, item)

    def values(self):
        return self.foo_dict.values()

    def __getitem__(self, index):
        assert isinstance(index, int)
        return self.foo_dict.get(index)

    def __setitem__(self, index, item):
        assert isinstance(index, int)
        self.foo_dict.update({index: item})

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
