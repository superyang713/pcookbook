"""
Problem:
You want to take a slice of data produced by an iterator, but the normal slicing
operator doesn't work.

Solution:
the itertools.islice() function is perfectly suited for taking slices of
iterators and generators.
"""

import itertools


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# c[10:2] will lead to a traceback.

for x in itertools.islice(c, 10, 20):
    print(x)
