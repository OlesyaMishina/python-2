# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


LOWER_LIMIT = 0
UPPER_LIMIT = 100000

number = int(input('Введите целое число от 0 до 100000: '))
while number <= LOWER_LIMIT or number >= UPPER_LIMIT:
    number = int(input('Обратите внимание на диапазон. Введите целое число от 0 до 100000: '))


def is_prime(number):
    if number == 0 or number == 1:
        return f'Число {number} не является ни простым, ни составным.'
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return f'Число {number} является составным.'
        else:
            return f'Число {number} является простым.'


print(is_prime(number))
