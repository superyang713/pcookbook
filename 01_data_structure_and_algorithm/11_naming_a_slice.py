"""
Problem:
Your program has become an unreadable mess of hardcoded slice indices and you
want to clean it up.

As a general rule, writing code with a lot of hardcoded index values leads to a
readability and maintenance mess.
"""

record = '....................100          .....513.25    ...........'

# Traditional way to slice the string and get the information
cost = int(record[20:32]) * float(record[38:48])
print(cost)

# The drawback is that pure indices do not have any meanings. Instead, we can
# name the slices.
SHARES = slice(20, 32)
PRICE = slice(38, 48)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

print(SHARES.start)
