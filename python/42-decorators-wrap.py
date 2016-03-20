from functools import wraps

def trace(func):
    #@wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
            (func.__name__, args, kwargs, result))
        return result
    return wrapper

@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n-2) + fibonacci(n-1))

# @study-group...why do we need this line? Isn't the purpose of
# the '@' symbol to do this automagically? It seems to have little utility
# and makes the output more verbose...
fibonacci = trace(fibonacci)

print(fibonacci(3))

print(fibonacci)
#help(fibonacci)
