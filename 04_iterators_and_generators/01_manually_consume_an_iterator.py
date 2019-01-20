"""
Problem:
You need to process items in an iterable, but for whatever reason, you can't or
don't want to use a for loop.

Solution:
To manually consume an iterable, use the next() function and write your code to
catch the StopIteration exception.
"""

# Example 1:
with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
            
    except Exception:
        pass

# Example 2: you can also instruct it to return a terminating value.
with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line)

# Example 3: fundamental iteration mechanisms in Python:
items = [1, 2, 3]
it = iter(items)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
