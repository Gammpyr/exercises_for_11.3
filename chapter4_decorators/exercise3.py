def call_count_decorator(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Функция {func.__name__} была вызвана {wrapper.call_count} раз")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

# Пример использования
@call_count_decorator
def example_function():
    print("Выполнение функции")

example_function()
example_function()