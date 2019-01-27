"""
Problem:
You want to iterate over the items contained in more than one sequence at a
time.

Solution:
Use zip() or itertools.zip_longest().
"""


from itertools import zip_longest


# Example 1: use zip()
x = [1, 5, 4, 2, 10, 7]
y = [181, 6, 34, 62, 4, 99]

for i, j in zip(x, y):
    print(i, j)

x = [1, 4, 3]
y = ['w', 'x', 'y', 'z']

for i in zip(x, y):
    print(i)

print("--------------------")

# Example 2: if the iteration length needs to be the same as the longest input:
for i in zip_longest(x, y, fillvalue=0):
    print(i)
print("--------------------")

# Example 3: zip() can also be used to pair the data together to create a dict.
headers = ["name", "shares", "price"]
values = ["ACME", 100, 490.1]

s = dict(zip(headers, values))
print(s)

print("--------------------")
# Example 4: zip() creates an iterator as a result. If you need the paired
# values stored in a list, use list() function
print(type(zip(x, y)))
print(list(zip(x, y)))
