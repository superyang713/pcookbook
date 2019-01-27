"""
Problem:
You want to write a function that accepts any number of inputer arguments.

Solution:
To write a function that accepts any number of positional argument, use a *
argument.
"""

import html


# Example 1: rest is a tuple of all extra positional arguments passed. The code
# treats it as a sequence in performing subsequent calculations.
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(1, 2))
print(avg(1, 2, 3, 4))


# Example 2: To accept any number of keyword arguments, use an argument that
# starts with **.
def make_element(name, value, **attrs):
    keyvals = [' {}="{}"'.format(key, value) for key, value in attrs.items()]
    attr_str = "".join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name, attrs=attr_str, value=html.escape(value))
    return element


print(make_element("item", "Albatross", size="large", quantity=6))


# Example 3: if you want a function that can accept both any number of
# positional and keyword-only arguments, use * and ** together.
def anyarg(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict
