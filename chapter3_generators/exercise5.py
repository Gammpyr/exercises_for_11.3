my_list = [
    "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
    "Buzz" if i % 5 == 0 else
    "Fizz" if i % 3 == 0 else
    str(i)
    for i in range(1, 16)
]


print(my_list)

