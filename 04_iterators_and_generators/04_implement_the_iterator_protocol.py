"""
Problem:
You are building custom objects on which you would like to support iteration,
but would like an easy way to implement the iterator protocol.

Solution:
By far, the easist way to implement iteration on an object is to use a
generator function. In recipe 4.2, a Node class was presented for representing
tree structures. This time, you want to implement an iterator that traverse
nodes in a depth-first pattern.
"""


# Example 1: implement iterator protocol with generator
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


# Example 2: Python's iterator protocol, without generator, requires __iter__
# to return a special iterator object that implements a __next__() operation
# and uses a StopIteration exception to signal completion. However,
# implementing such objects can often be a messy affair.


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    """
    Depth-first traversal
    """

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)

        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))

for ch in root.depth_first():
    print(ch)
