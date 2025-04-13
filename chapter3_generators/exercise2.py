"""Формула для расчёта чисел Фибоначчи:
Fn = Fn–2 + Fn–1,
где F0 = 0, F1 = 1, а n — больше или равно 2 и является целым числом."""


def get_next_fibonacci_num():
    fn1 = 0
    fn2 = 1
    while True:
        yield fn1
        fn1, fn2 = fn2, fn1 + fn2


fibonacci_num = get_next_fibonacci_num()

for i in range(10):
    print(next(fibonacci_num))

