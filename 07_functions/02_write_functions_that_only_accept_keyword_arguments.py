"""
Problem:
You want a function to only accept certain arguments by keyword.

Solution:
It is easy to implement if you place the keyword arguments after a * argument
or a single unnamed *.
"""


# Example 1: Note that * argument can only appear as the last positional
# argument in a function definition. A ** argument can only appear as the last
# argument.
def recv(maxsize, *, block):
    """
    Receives a message
    """
    pass


# recv(1024, True)  --> TypeError
recv(1024, block=True)
