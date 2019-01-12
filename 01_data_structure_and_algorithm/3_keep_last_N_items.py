"""
Problem:
You need to keep a limited history of the last few items seen during iteration
or during some other kind of processing.

Solution:
Keeping a limited history is a perfect use for a collections.deque.
"""

# Example 1: perform a simple text match on a sequence of lines and yields the
# matching line along with the previous N lines of context when found
from collections import deque


def search(lines, pattern, history=5):
    """
    Keyword Arguments:
    lines   --
    pattern --
    history -- (default 5)
    """
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
with open('2_unpack_elements_from_iterables_of_arbitrary_length.py') as f:
    for line, prevlines in search(f, 'Example', 3):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-' * 20)
    print(prevlines)

# Example 2: use deque(maxlen=N) to create a fixed-sized queue. When new items
# are added and the queue is full, the oldest item is automatically removed.
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)

q.append(4)
print(q)

q.append(5)
print(q)

# If a maximum size is not given, you get an unbounded queue that lets you
# append and pop items on either end.
d = deque()
d.append(1)
d.append(2)
d.append(3)
print(d)

d.appendleft(4)
print(dp)

d.pop()
print(d)

d.popleft()
print(d)
