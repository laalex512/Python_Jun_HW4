# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def home_task2(*, a, b, c) -> dict:
    current_vars = locals()
    result_dict = {}
    for key, value in current_vars.items():
        result_dict.setdefault(str(value), key)
    return result_dict


print(home_task2(a=5, b=7, c=9))
