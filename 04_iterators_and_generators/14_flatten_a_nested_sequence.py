"""
Problem:
You have a nested sequence that you want to flatten into a single list of value

Solution:
It can be easily soloved by writing a recursive generator function involving 
yield from statement.
"""


from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)

        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

print(type(flatten(items)))

items = ["Dave", "Paula", ["Thomas", "Lewis"]]
for x in flatten(items):
    print(x)
