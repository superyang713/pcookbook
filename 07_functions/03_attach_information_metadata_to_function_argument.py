"""
Problem:
You've written a function, but would like to attach some additional information
to the arguments so that others know more about how a function is supposed to
be used.

Solution:
Use annotations.
"""


# Example 1:
def add(x: int, y: int) -> int:
    return x + y


help(add)

# Discussion:
# Function annotations are merely stored in a function's __annotations__
# attribute.
print(add.__annotations__)
