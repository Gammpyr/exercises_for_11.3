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


# import functools
#
# def memoizing(max_cache_size):
#     def decorator(func):
#         cache = {}
#         order = []
#
#         @functools.wraps(func)
#         def wrapper(x):
#             if x in cache:
#                 return cache[x]
#             else:
#                 result = func(x)
#                 if len(order) >= max_cache_size:
#                     oldest = order.pop(0)
#                     del cache[oldest]
#                 cache[x] = result
#                 order.append(x)
#                 return result
#         return wrapper
#     return decorator
#
# # Пример использования декоратора
#
# @memoizing(3)
# def f(x):
#     print('Calculating...')
#     return x * 10
#
# # Примеры вызовов функции
# print(f(1))  # Output: Calculating... 10
# print(f(1))  # Output: 10
# print(f(2))  # Output: Calculating... 20
# print(f(3))  # Output: Calculating... 30
# print(f(4))  # Output: Calculating... 40
# print(f(1))  # Output: Calculating... 10