import time


def caching_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = args
        if key in cache:
            print("Восстановлено из кэша")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


@caching_decorator
def expensive_function(x, y):
    time.sleep(2)
    return x * y


print(expensive_function(3, 4))
print(expensive_function(3, 4))
