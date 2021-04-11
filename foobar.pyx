#!/usr/bin/env python3
# cython: language_level=3
"""
Module containing a function to automatically
assign given values to numbered keys in a dict
starting from 0, then returning the dict made
"""
cdef dict foo_bar(tuple _baz): return dict(enumerate(_baz))
def foobar(*__baz): return foo_bar(__baz)


if __name__ == "__main__":
    fb = foobar("foo", "bar", "baz")
    print(fb)
