"""
Problem: There is an N-element tuple or sequence that you would like to unpack
intot a collection of N variable.
"""

# You have an N-element tuple or sequence that you would like to unpack into a
# collection of N variable.
p = (4, 5)
x, y = p

# A slightly more complicated problem
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
name, shares, price, (year, mon, day) = data
print(name)

# Unpacking works with any object that happens to be iterable, not just tuples,
# or lists. This includes string, files, iterators, and generators.
s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)

# Discard certain values
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)
