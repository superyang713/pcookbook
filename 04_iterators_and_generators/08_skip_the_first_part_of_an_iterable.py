"""
Problem: You wan to iterate over items in an iterable, but the first few items
aren't of interest and you just want to discard them.

Solution:
Use itertools.dropwhile(), islice() function, or generator comprehension. But
the two are different.
"""

from itertools import dropwhile, islice

# Example 1: use itertools.dropwhile() function Skip all the initial comment
# lines
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

# Example 2: if you happen to know the exact number of items you want to skip,
# then you can use itertools.islice() instead.
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

# Example 3: discarding the first part of an iterable is also slightly different
# than simply filtering all of it.
with open('/etc/passwd') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')
