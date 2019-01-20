"""
Problem:
You want to implement a custom iteration pattern that's different than the
usual built-in functions (e.g., range(), reversed(), etc).

Solution:
If you want to implement a new kind of iteration patter, define it using
a generator function.
"""


# Example 1: here is a generator that produces a range of floating-point
# numbers:
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

# Example 2: the underlying mechanism about generator:
def countdown(n):
    print("Starting to count from", n)
    while n > 0:
        yield n
        n -= 1
    print("Done!")

c = countdown(3)
print(c)

print(next(c))
print(next(c))
print(next(c))
print(next(c))
