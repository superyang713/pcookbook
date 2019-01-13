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


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
