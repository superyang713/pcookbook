"""
Problem:
You have a sequence of items, and you'd like to determine the most frequently
occuring items in the sequence.

Solution:
The collection.Counter is designed for just such a problem.
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under',
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(word_counts)
print(type(word_counts))
print(top_three)
print(type(top_three))


# Counter object, under the hood, is a dictionary that maps the items to the
# number of occurrences.
print(word_counts['not'])
print(word_counts['eyes'])


# If you want to increment the count manually, simply use addition:
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts['eyes'])

# Alternatively, you could use the update() method:
word_counts.update(morewords)
print(word_counts['eyes'])

# A little-known feature of Counter instances is that they can be easily
# combined using various mathematical operations.
a = Counter(words)
b = Counter(morewords)

c = a + b  # Combine counts
print(c)

d = a - b  # Subtract counts
print(d)
