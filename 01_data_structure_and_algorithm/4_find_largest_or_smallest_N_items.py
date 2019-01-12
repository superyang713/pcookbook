"""
Problem:
You want to make a list of the largest or smallest N items in a collection.

Solution:
The heapq module has two functions--nlargest() and nsmallest()--that do exactly
what you want.

Explanation:
heapq is most appropriate if you are trying to find a relatively small number
of items.
It is faster to use max() or min() to find the single largest or smallest
number.
if N is about the same size as the collection itself, it is usually faster to
sort it first and take a slice.(i.e. use sort(items)[:N])
"""

import heapq

# Example 1:
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# Example 2: Both functions also accept a key parameter that allows them to be
# used with more complicated data structures.
portfolio = [
    {
        'name': 'IBM',
        'shares': 100,
        'price': 91.1
    },
    {
        'name': 'AAPL',
        'shares': 50,
        'price': 543.22
    },
    {
        'name': 'FB',
        'shares': 200,
        'price': 21.09
    },
    {
        'name': 'HPQ',
        'shares': 35,
        'price': 31.75
    },
    {
        'name': 'YHOO',
        'shares': 45,
        'price': 16.35
    },
    {
        'name': 'ACME',
        'shares': 75,
        'price': 115.65
    },
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)
