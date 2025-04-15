"""Задача 4.
Напишите декоратор, который выводит промежуточные результаты выполнения функции для отладки."""

import sys
def debug_intermediate_results(func):
    def wrapper(*args, **kwargs):
        def trace_calls(frame, event, arg):
            if event == 'line':
                local_vars = frame.f_locals
                print(f"Промежуточные результат в {func.__name__}: {local_vars}")
            return trace_calls
        sys.settrace(trace_calls)
        try:
            result = func(*args, **kwargs)
        finally:
            sys.settrace(None)
            return result
    return wrapper

# Пример использования декоратора
@debug_intermediate_results
def example_function(x):
    y = x + 1
    z = y * 2
    return z

result = example_function(5)
print(f"Финальный результат: {result}")