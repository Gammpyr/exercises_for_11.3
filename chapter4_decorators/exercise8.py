import time

start = time.time()


def memoized(func):
    memo = {}
    def wrapper(*args, **kwargs):
        if args not in memo:
            result = func(*args, **kwargs)
            memo[args] = result
            print('Calculating...')
            return result
        elif args in memo:
            return memo[args]

    return wrapper

@memoized
def f(x):
    return x * 10

print(f(1))
print(f(1))
print(f(5))
print(f(5))
print(f(12))
print(f(12))

print(f'Затрачено времени: {time.time() - start}')