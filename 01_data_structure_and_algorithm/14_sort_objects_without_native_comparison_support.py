"""
Problem:
You want to sort objects of the same class, but they don't natively support
comparison operations.

Solultion:
The built-in sorted() function takes a key argument that can be passed a
callable that will return some value in the object that sorted will use to
compare the objects.
"""

from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
result = sorted(users, key=lambda u: u.user_id)
print(result)

# Instead of using lambda, an alternative approach is to use
# operator.attrgetter().
result = sorted(users, key=attrgetter('user_id'))
print(result)
