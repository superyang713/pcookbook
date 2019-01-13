"""
Problem:
You want to make a dictionary that is a subset of another dictionary.

Solution:
It can be easily accomplished using a dictionary comprehension.
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p1 = {key: value for key, value in prices.items() if key in tech_names}
