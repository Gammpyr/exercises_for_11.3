accept_dict = {
    'Admin': ['all', ],
    'Moderator': ["double_x", "triple_x", ],
    'User': ["sum_x_plus_one", ]
}


def accept_control_decorator(func):
    def wrapper(*args, **kwargs):
        role = args[-1]
        str_func = str(func).split()[1]
        if role not in accept_dict:
            return 'В доступе отказано!'
        if str_func in accept_dict[role] or 'all' in accept_dict[role]:
            return func(*args, *kwargs)
        else:
            return 'В доступе отказано!'

    return wrapper


@accept_control_decorator
def double_x(x, user):
    return x * x


@accept_control_decorator
def triple_x(x, user):
    return x * x * x


@accept_control_decorator
def sum_x_plus_one(x, user):
    return x + 1


@accept_control_decorator
def subtrack_one(x, user):
    return x - 1


print('Удвоить:')
print(double_x(5, 'Admin'))
print(double_x(5, 'Moderator'))
print(double_x(5, 'User'))
print('Утроить:')
print(triple_x(5, 'Admin'))
print(triple_x(5, 'Moderator'))
print(triple_x(5, 'User'))
print('Прибавить:')
print(sum_x_plus_one(5, 'Admin'))
print(sum_x_plus_one(5, 'Moderator'))
print(sum_x_plus_one(5, 'User'))
print(sum_x_plus_one(5, 'User24'))
