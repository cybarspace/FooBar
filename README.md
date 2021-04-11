# FooBar module

## The performance of a dictionary at the convenience of a list

### Features

*(or bugs...)*

- Provides a `function` and a `Class`
- The `function` takes an arbitrary number of `arguments` and returns a dictionary where the keys are numbers starting at `0` (like list indices).
- The `Class` takes a `list` or `tuple` and *holds* the values in a “private” `dict` produced by the `function` above
- Uses `dataclasses` for the `Class`
- Uses a `dict` for the `function`
- The `function` provides a speedup of nearly `50%` but has no type checks or anything to discourage modification of data, since it *just* returns a `dict`. The `Class` is a joke. Use a `tuple` for better performance and “safety”.

### TL;DR code

```python
def foobar(*__baz): return dict(enumerate(__baz))

fb = foobar(
    "foo",
    "bar",
    "baz"
)

print(fb)
# output: {0: 'foo', 1: 'bar', 2: 'baz'}
```
