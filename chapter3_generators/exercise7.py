from math import factorial


def get_inf_factorial():
    n = 0
    while True:
        yield factorial(n)
        n += 1


next_factorial_generator = get_inf_factorial()

for i in range(11):
    print(next(next_factorial_generator))
