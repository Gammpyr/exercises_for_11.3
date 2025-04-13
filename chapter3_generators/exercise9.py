def my_map(func, xs):
    result = []
    for i in xs:
        result.append(func(i))
    return result

print(my_map(lambda x: x + 2, [-1, 2, -3]))

def my_filter(func, xs):
    result = []
    for i in xs:
        if func(i):
            result.append(i)
    return result

print(my_filter(lambda x: x % 2 == 1, range(10)))

def replicate_each(n, xs):
    result = []
    for i in xs:
        for j in range(n):
            result.append(i)
    return result

print(replicate_each(1, [1, 'a']))
print(replicate_each(3, [1, 'a']))
print(replicate_each(0, [1, 'a']))