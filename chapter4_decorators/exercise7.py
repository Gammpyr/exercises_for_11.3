"""Задача 7.
Реализуйте декоратор, который гарантирует автоматическое закрытие ресурсов, например файлов, после выполнения функции.

Решение"""
import functools
def auto_close(resource_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            resource = kwargs.get(resource_name) or args[0]
            try:
                return func(*args, **kwargs)
            finally:
                resource.close()
                print(f"{resource_name} has been closed.")
        return wrapper
    return decorator

# Пример использования декоратора
@auto_close('file')
def example_function(file, content):
    file.write(content)

# Пример использования декоратора с открытием файла
file = open('example.txt', 'w')
example_function(file, "Hello, world!")