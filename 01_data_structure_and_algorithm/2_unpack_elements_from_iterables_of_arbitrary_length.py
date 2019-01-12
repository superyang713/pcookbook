"""
Problem:
You need to unpack N elements from an iterable, but the iterable may be longer
than N elements, causing a (too many values to unpack) exception.

Solution:
Python star expression can be used to address this problem.
"""

# Example 1: unpack with star expression at the end
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)
print(type(phone_numbers))

# Example 2: unpack with start expression at other positions
*trailing_qtrs, current_qtr = [3, 5, 2, 5, 8, 9, 10]
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
print(trailing_avg)

# Example 3: iterate over a sequence of tuples of varying length
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# Example 3: combined with certain kinds of string processing operations, such
# as splitting.
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *_, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
print(*_)
