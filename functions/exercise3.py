# Задача 3
def num_sum_max_result(num_list):
    if len(num_list) < 2:
        return 0

    sorted_num_list = sorted(map(abs, num_list))
    max1 = sorted_num_list.pop()
    max2 = sorted_num_list.pop()

    return max1 * max2


print(num_sum_max_result([2, 3, 5, 12, 7, 11]))
print(num_sum_max_result([-5, -7, -9, -13]))
print(num_sum_max_result([1, 2]))
print(num_sum_max_result([4]))