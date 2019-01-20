"""
Problem:
You want to pick random items out of a sequence or generate random numbers.

Solution:
Python random module.
"""

import random

# Example 1: pick a random item out of a sequence, use random.choice()
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

# Example 2: take a sampling of N items where selected items are removed from
# further consideration, use random.sample()
print(random.sample(values, 2))
print(random.sample(values, 2))
print(random.sample(values, 2))

# Example 3: shuffle items in a sequence in place, use random.shuffle()
random.shuffle(values)
print(values)

# Example 4: produce random integers, use random.randint():
print(random.randint(0, 10))
print(random.randint(0, 10))

# Example 5: produce uniform floating-point values in the range 0 to 1, use
# random.random()
print(random.random())
print(random.random())
