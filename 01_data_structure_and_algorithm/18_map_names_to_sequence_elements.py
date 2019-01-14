"""
Problem:
You have code that accesses list or tuple elements by position, but this makes
the code somewhat difficult to read at times. You also like to be less
dependent on position in the structure, by accessing the elements by name.

Solution:
collections.namedtuple() provides these benefits, while adding minimal overhead
over using a normal tuple object.
"""

from collections import namedtuple

# Example 1: namedtuple initialization
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

# Example 2: namedtuple is immutable, however, the attribute can be changed
# using the _replace() method.
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock(name='ACME', shares=100, price=123.45)
s = s._replace(shares=75)
print(s)

# Example 3: _replace() method can be a convenient way to populate named tuples
# that have optional or missing fields. To do this, you make a prototype tuple
# containing the default values and then use _replace() to create new instances
# with values replaced.
Stock = namedtuple('stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
stock = dict_to_stock(a)
print(stock)

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
stock = dict_to_stock(b)
print(stock)
