# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного
# аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def my_dict(**kwargs) -> dict:
    result = dict()
    for k, v in kwargs.items():
        result[hash(v)] = k
        try:
            v = hash(v)
            result[v] = str(k)
        except TypeError:
            result[str(v)] = k
    return result


print(my_dict(chemistry=5, physics=4, math=3, PE=2))
