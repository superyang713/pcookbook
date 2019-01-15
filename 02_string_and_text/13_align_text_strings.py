"""
Problem:
You need to format text with some sort of alignment applied.

Solution:
For basic alignment of strings, the ljust(), rjust(), and center() methods of
strings can be used.
"""

# Example 1:
text = 'Hello World'
left_aligned_text = text.ljust(20, '-')
right_aligned_text = text.rjust(20, '=')
center_aligned_text = text.center(20)
print(left_aligned_text)
print(right_aligned_text)
print(center_aligned_text)

# Example 2: format() function can also be used to easily align things. All you
# need to to is to use the <, >, ^ characters along with a desired width.
left = format(text, '>20')
right = format(text, '<20')
center = format(text, '^20')
print(left)
print(right)
print(center)

left = format(text, '->20')
right = format(text, '=<20')
center = format(text, '*^20')
print(left)
print(right)
print(center)

# Example 3: these format codes can also be used in the format() method used
# when formatting multiple values.
result = '{:>10} {:=>10}'.format('hello', 'world')
print(result)
