def get_exception(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as exp:
            print(f'Возникла ошибка в "{func.__name__}": {exp}.')

    return wrapper


@get_exception
def func_for_test(x):
    return 100 / x


print(func_for_test('k'))

# import traceback
# def exception_handler(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             print(f"Exception in function '{func.__name__}': {e}")
#             traceback.print_exc()
#             return None
#     wrapper.__name__ = func.__name__
#     wrapper.__doc__ = func.__doc__
#     return wrapper
#
# # Пример использования декоратора
# @exception_handler
# def example_function(x):
#     return 10 / x
#
# # Примеры вызова функции, которые вызовут и не вызовут исключения
# print(example_function(2))  # Ожидаемый результат: 5.0
# print(example_function(0))  # Ожидаемый результат: информация об исключении
