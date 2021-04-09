"""
FooBar data type class

An ordered iterable data type to hold values in
dictionaries while automatically assigning keys
"""
from dataclasses import dataclass, InitVar


def foobar(*args):
    """ foobar function for dict creation """
    __baz = {}
    for val in args:
        __baz.update({args.index(val): val})

    return __baz


@dataclass
class FooBar:
    """ FooBar class for simple data storage """

    values: InitVar[list] = None

    def __post_init__(self, values):
        try:
            self.__baz = foobar(*values)
        except AttributeError as a_err:
            raise TypeError("Values must be given in list or tuple") from a_err

    def __repr__(self):
        return f"{self.__baz}"

    def __len__(self):
        return len(self.__baz)

    def __getitem__(self, pos):
        try:
            return self.__baz[pos]
        except (KeyError, TypeError) as err:
            raise IndexError("FooBar index is nonexistent") from err
