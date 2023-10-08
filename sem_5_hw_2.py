# Задание 2
# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def keyword_arguments_to_dict(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        argument_dict[value] = key if isinstance(value, (int, float, str, bool)) else str(value)
    return argument_dict

# Пример использования функции
result = keyword_arguments_to_dict(a=10, b='hello', c=True)
print(result)
