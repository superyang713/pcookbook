"""
Problem:
You want to perform various caluclations (e.g., minimum value, maximum value,
sorting, etc) on a dictionary of data

Solution:
1. use zip() to invert the keys and values of the dictionary
2. use lamdba function
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

# Example 1:
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# Example 2:
min_price = min(prices)  # Returns 'AAPL'
max_price = max(prices)  # Returns 'IBM'

min_value = min(prices.values())  # Returns 10.75
max_value = max(prices.values())  # Returns 612.78

# Example 3:
min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)
