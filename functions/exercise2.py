# Задача 2
list1 = ['hello', 'world', 'apple', 'pear', 'banana', 'pop']
list2 = ['', 'madam', 'racecar', 'noon', 'level', '']
list3 = []


def is_first_last_ltr_similar(my_list):
    result = []
    if not my_list:
        return my_list
    for word in my_list:
        if not word:
            result.append(word)
        elif word[0] == word[-1]:
            result.append(word)
    return result


print(is_first_last_ltr_similar(list1))
print(is_first_last_ltr_similar(list2))
print(is_first_last_ltr_similar(list3))