# Задание №1
# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform
from pathlib import Path

__all__ = ['write_file', 'gen_names']
MIN_NUM = -1000
MAX_NUM = 1000


def write_file(num_str: int, f_name: Path) -> None:
    with open(f_name, 'w', encoding='UTF-8') as f:
        for _ in range(num_str):
            f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')


# Задание №2 Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from random import randint, choice
from pathlib import Path

MIN_VALUE = 4
MAX_VALUE = 7
VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'


def gen_names(str_counts: int, file_name: str | Path) -> None:
    with open(file_name, "a", encoding="UTF-8") as f:
        for _ in range(str_counts):
            name = ''
            flag = choice([-1, 1])
            for _ in range(randint(MIN_VALUE, MAX_VALUE)):
                if flag == -1:
                    name += choice(CONSONANTS)
                else:
                    name += choice(VOWELS)
                flag *= -1
            f.write(name.title() + '\n')


if __name__ == '__main__':
    gen_names(10, Path('names.txt'))
    write_file(10, Path('numbers.txt'))
