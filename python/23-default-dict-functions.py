from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
        ('red', 5),
        ('blue', 17),
        ('orange', 9),
]

def log_missing():
    print('Key added')
    return 0

'''
result = defaultdict(log_missing, current)
print('Before:', dict(result))

for key, amount in increments:
    result[key] += amount

print('After:', dict(result))

## Example with stateful closure to count the number of keys that were missing
## ...harder to read than the stateless function example
def increment_with_report(current, increments):
    added_count = 0
    def missing():
        nonlocal added_count  # Stateful closure
        added_count += 1
        return 0
    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2
print('Result:', result)
print('Count:', count)

## Cleaner approach -- define a small class that encapsulates the state we want to track
## Note how we are able to access CountMissing.missing method and passit to the defaultdict as the hook
class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = defaultdict(counter.missing, current)

for key, amount in increments:
    result[key] += amount

assert counter.added == 2
print('Result:', result)
print('Count:', counter.added)
'''

# The above class on its own doesn't make much sense until you see it used with defaultdict.
# To be more clear, we can use the special __call__ method to allow an object to be called like a fucntion
# This provides a strong hint that the goal of the class is to act as a stateful closure.
class BetterCountMissing(object):
    added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
BetterCountMissing.added=5

result = defaultdict(counter, current)  # Relies on __call__
print('test', counter.added)
for key, amount in increments:
    result[key] += amount

assert counter.added == 2
assert callable(counter)
print('Callable class?', callable(counter))
print('Result:', result)
print('Count:', counter.added)
