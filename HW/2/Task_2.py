# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль
# fractions

import fractions


# Функция сложения и умножения дробей
def sum_and_muilt_fractions(first_fraction, second_fraction):
    first_numerator, first_denominator = map(int, first_fraction.split("/"))
    second_numerator, second_denominator = map(int, second_fraction.split("/"))

    # сложение дробей
    sum_denominator = first_denominator * second_denominator
    sum_numerator = first_numerator * second_denominator + second_numerator * first_denominator

    # умножение дробей
    mult_denominator = first_denominator * second_denominator
    mult_numerator = first_numerator * second_numerator
    return sum_numerator, sum_denominator, mult_numerator, mult_denominator


# Функция упрощения дробей

def simplifying_fraction(numerator, denominator):
    whole_part = 0

    if numerator == denominator:
        whole_part = 1
        numerator = 0
    elif numerator > denominator:
        whole_part = numerator // denominator
        numerator = numerator - denominator * whole_part

    for i in range(denominator, 1, -1):
        if numerator % i == 0 and denominator % i == 0:
            numerator = int(numerator / i)
            denominator = int(denominator / i)
            break

    if whole_part == 0:
        return f'{numerator}/{denominator}'
    elif numerator == 0:
        return f'{whole_part}'
    else:
        return f'{whole_part} {numerator}/{denominator}'


def input_fraction():
    fraction = input('Введите дробь в виде а/b: ')
    denominator = int(fraction.split("/")[1])
    while denominator == 0:
        print("Деление на 0 невозможно.")
        fraction = input('Введите дробь в виде а/b: ')
        denominator = int(fraction.split("/")[1])
    return fraction


first_fraction = input_fraction()
second_fraction = input_fraction()
result_fraction = sum_and_muilt_fractions(first_fraction, second_fraction)

print(f'Сумма дробей равна {simplifying_fraction(result_fraction[0], result_fraction[1])}.')
print(f'Произведение дробей равно {simplifying_fraction(result_fraction[2], result_fraction[3])}')

# проверка
first_fraction = 3/5
second_fraction = 6/4
first = fractions.Fraction(3, 5)
second = fractions.Fraction(6, 4)
print(f'Сумма дробей через модуль fractions равна {first + second}')
print(f'роизведение дробей через модуль fractions равна {first * second}')
