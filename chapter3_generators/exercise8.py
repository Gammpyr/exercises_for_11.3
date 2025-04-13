def non_empty_truths(my_list):
    next_list_generator = get_next_list(my_list)
    result = []
    try:
        while True:
            cur_list = next(next_list_generator)
            truths_list = []
            for elem in cur_list:
                if elem:
                    truths_list.append(elem)
            if truths_list:
                result.append(truths_list)
    except StopIteration:
        return result


def get_next_list(lst):
    for el in lst:
        yield el


print(non_empty_truths([[0, 1, 2], [], [], [False, True, 42], [5, True, 'Final']]))
