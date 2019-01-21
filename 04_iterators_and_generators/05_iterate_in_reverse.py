"""
Problem:
You want to iterate in reverse over a sequence.

Solution:
Use the built-in reversed() function. Or implement __reverse__() method
"""

# Example 1: built-in reversed() function
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

# Example 2: Reversed() iteration only works if the object in question has has
# a size that can be determined or if the object implements a __reverse__()
# special method. If neither of these is satisfied, you have to convert it to
# a list first. Be aware that turning an iterable into a list could consume a
# lot of memory if it's large.

# Print a file backward.
# with open("somefile") as fin:
#     for line in reversed(list(fin)):
#         print(line, end='')


# Example 3: reversed iteration can be customized on user-defined classes if
# they implement the __reverse__() method.
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


counter = Countdown(10)
for count in counter:
    print(count)

for count in reversed(counter):
    print(count)
