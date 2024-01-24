# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Задание №6
# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег


MULTIPLICITY = 50
PERCENT: float = 0.015
PERCENT_BONUS: float = 0.03
COUNT_PERC = 3
MIN_LIMIT = 30
MAX_LIMIT = 600
PERCENT_RICHNESS = 0.1
RICHNESS_AMOUNT = 5_000_000
CMD_DEPOSIT = "1"
CMD_WITHDRAW = "2"
SHOW_LOG = "3"
CMD_EXIT = "4"

count = 0
balance = 0
operations_log = []


# Функция записывает операции
def logging(operation: str):
    operations_log.append(operation)

# Функция выводит спислк операции
def show_log():
    print("-- ЛОГ ОПЕРАЦИЙ --")
    for item in operations_log:
        print(item)


# Функция пополнения баланса
def top_up(balance: float) -> float:
    amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
    while amount % MULTIPLICITY != 0:
        amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
    balance += amount
    global count
    count += 1
    print(f"Внесли сумму {amount}. Баланс {balance:.2f}.")
    logging(f'Внесли сумму {amount}. Баланс {balance:.2f}.')
    balance = bonus(balance)
    return balance


# Функция снятия денег
def withdraw(balance: float) -> float:
    amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
    while amount % MULTIPLICITY != 0:
        amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
    comission = amount * PERCENT
    if comission < MIN_LIMIT:
        comission = MIN_LIMIT
    elif comission > MAX_LIMIT:
        comission = MAX_LIMIT
    if comission + amount > balance:
        print("На балансе недостаточно средств")
    else:
        balance -= (amount + comission)
        global count
        count += 1
        print(f"Сумма снятия {amount}, комиссия {comission}. Баланс {balance:.2f}.")
        logging(f'Сняли сумму {amount}, вычтена комиссия {comission}. Баланс {balance:.2f}.')
        balance = bonus(balance)
    return balance


# Функция начисления бонуса после каждой 3 операции
def bonus(balance: float) -> float:
    if count % COUNT_PERC == 0:
        bonus_sum = balance * PERCENT_BONUS
        balance += bonus_sum
        print(f"Начислен бонус {bonus_sum:.2f}. Баланс {balance:.2f}.")
        logging(f"Начислен бонус {bonus_sum:.2f}. Баланс {balance:.2f}.")
    return balance

# Функция проверки на богатство:

def ricnhess(balance: float) -> float:
    if balance > RICHNESS_AMOUNT:
        tax = balance*PERCENT_RICHNESS
        balance -= tax
        print(f"Вычтен налог на богатство в размере {tax}. Баланс {balance:.2f} ")
        logging(f"Вычтен налог на богатство в размере {tax}. Баланс {balance:.2f} ")
    return balance

# Функция меню
def menu():
    action = input(
        f" \n"
        f"пополнить - {CMD_DEPOSIT:>7}\n"
        f"снять - {CMD_WITHDRAW:>11}\n"
        f"список операций - {SHOW_LOG}\n"
        f"выход - {CMD_EXIT:>11}\n"
        f"Введите действие: "
    )
    return int(action)

action = menu()
while (action != 4):
    if (action == 1):
        balance=ricnhess(balance)
        balance = top_up(balance)
    elif (action == 2):
        balance=ricnhess(balance)
        balance = withdraw(balance)
    elif (action == 3):
        show_log()
    elif (action == 4):
        print("Вы вышли из программы.")
        break
    else:
        print("Введена неверная команда")
    action = menu()
print("Вы вышли из программы.")

# while True:
#     action = input(
#     f"пополнить-{CMD_DEPOSIT}\n"
#     f"снять-{CMD_WITHDRAW}\n"
#     f"выход-{CMD_EXIT}\n"
#     f"Введите действие: "
#     )
#     if balance > RICHNESS_AMOUNT and action != "3":
#         sum_percent = balance * PERCENT_RICHNESS
#         balance -= sum_percent
#         print(f"Вычтен налог на богатство в размере {sum_percent}")
#         print(f"Текущий баланс {balance}")
#     if action == "1" or action == "2":
#         amount = 1
#         while amount % MULTIPLICITY != 0:
#             amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
#         if action == "1":
#             operations += 1
#             balance += amount
# # print(f"Текущий баланс {balance}")
#
#         else:
#             comission = amount * PERCENT
#             if comission < MIN_LIMIT:
#                 comission = MIN_LIMIT
#             elif comission > MAX_LIMIT:
#                 comission = MAX_LIMIT
#             if comission + amount > balance:
#                 print("На балансе недостаточно средств")
#             else:
#                 operations += 1
#                 balance -= (amount + comission)
#                 print(f"Сумма снятия {amount}, комиссия {comission}, общая сумма {amount + comission}")
# # print(f"Текущий баланс {balance}")
#         if operations % COUNT_PERC == 0:
#             bonus_sum = balance * PERCENT_BONUS
#             balance += bonus_sum
#             print(f"Сумма бонуса {bonus_sum}")
# # print(f"Текущий баланс {balance}")
#         print(f"Текущий баланс {balance}")
#     elif action == "3":
#         break
#     else:
#         print("Введена неверная команда")
