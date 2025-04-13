def title_string(string):
    for ltr in string:
        yield ltr.upper()

upcase_gen = title_string('Какой-то текст!')

for i in range(10):
    print(next(upcase_gen))