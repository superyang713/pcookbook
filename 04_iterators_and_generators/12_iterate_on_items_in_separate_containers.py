"""
Problem:
You need to perform the same operation on many objects, but the objects are
contained in different containers. You would like to avoid nested loops without
losing the readability of your code.

Solution:
Use itertools.chain() method
"""

import itertools


# Example 1: 
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for x in itertools.chain(a, b):
    print(x)

print("--------------------")

# The example above is better than the following in terms of performance and
# code readability

for x in a:
    print(x)

for x in b:
    print(x)

print("--------------------")

# And also better and combining the lists first and do the iteration.

for x in a + b:
    print(x)
