"""Задача 5.
Создайте декоратор, который отслеживает, какие функции вызываются внутри другой функции,
и выводит список зависимостей."""

import sys
def track_dependencies(func):
    def wrapper(*args, **kwargs):
        called_functions = set()
        def trace_calls(frame, event, arg):
            if event == 'call':
                code = frame.f_code
                called_functions.add(code.co_name)
            return trace_calls
        sys.settrace(trace_calls)
        try:
            result = func(*args, **kwargs)
        finally:
            sys.settrace(None)
            # Remove the wrapper itself from the list of called functions
            called_functions.discard(func.__name__)
            print(f"Functions called inside {func.__name__}: {called_functions}")
        return result
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

# Примеры использования декоратора
@track_dependencies
def foo():
    bar()
    baz()

def bar():
    pass

def baz():
    qux()

def qux():
    pass

foo()