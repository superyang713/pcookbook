"""
Problem:
You have a callable that you would like to use with some other python code, possibly as
a callback funciton or handler, but it takes too many arguments and causes an exception
when called.

Solution:
Use functools.partial()
"""


from functools import partial
import math


# Exmaple 1:
def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1)  # a = 1
s1(2, 3, 4)
s1(4, 5, 6)


s2 = partial(spam, d=42)
s2(1, 2, 3)


# Example 2: sort() can only accept a function with one parameter. Use partial to fix
# this.
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


pt = (4, 3)
points.sort(key=partial(distance, pt))
print(points)
