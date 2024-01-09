# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление. Функцию hex используйте для проверки своего результата.
def into_hex(original_num):
    DIV_HEX = 16
    HEX = "0123456789abcdef"

    num = original_num
    result = ""
    while num > 0:
        result = HEX[num % DIV_HEX] + result
        num //= DIV_HEX
    return result

#Проверка
original_num = 123456
if into_hex(original_num) == hex(original_num)[2:]:
    print(
        f'Программа работает верно. '
        f'Число {original_num} в шестнадцатеричном представлении {into_hex(original_num)}.'
    )
