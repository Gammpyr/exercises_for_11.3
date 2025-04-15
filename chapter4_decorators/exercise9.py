import time
from functools import wraps

start = time.time()


def memoizing(cache_size):
    def decorator(func):
        memo = {}
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args not in memo:
                if len(memo) == cache_size:
                    first_key = list(memo.keys())[0]
                    del memo[first_key]
                result = func(*args, **kwargs)
                memo[args] = result
                print('Calculating...')
                return result
            elif args in memo:
                return memo[args]

        return wrapper
    return decorator

@memoizing(2)
def f(x):
    return x * 10

print(f(1))
print(f(1))
print(f(5))
print(f(5))
print(f(12))
print(f(12))
print(f(17))
print(f(17))
print(f(7))
print(f(7))
print(f(5))
print(f(5))

print(f'Затрачено времени: {time.time() - start}')