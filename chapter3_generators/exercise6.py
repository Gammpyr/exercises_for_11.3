def get_inf_square(num):
    square = 0
    while True:
        yield num ** square
        square += 1


inf_2_square_generator = get_inf_square(2)

for _ in range(11):
    print(next(inf_2_square_generator))

# test2 = (2 ** x for x in range(0, float("inf")))

# for _ in range(11):
#     print(next(test2))
