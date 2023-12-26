# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
# подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT_COUNT = 10

number = randint(LOWER_LIMIT, UPPER_LIMIT)
print((number))
count = 0
answer = -1
while count <= ATTEMPT_COUNT-1 and answer != number:
    count += 1
    answer = int(input(f'Попытка {count}, введите целое число от 0 до 1000: '))
    if answer < number:
        print(f'Загаданное число больше {answer}.')
    elif answer > number:
        print(f'Загаданное число меньше {answer}.')

if count <= ATTEMPT_COUNT-1:
    print('Вы угадали!')
else:
    print('Попытки закончились, вы проиграли.')
