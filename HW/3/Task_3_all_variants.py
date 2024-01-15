# *Верните все возможные варианты комплектации рюкзака.

from itertools import combinations

# Достуаные вещи
things_for_hike = {"вода": 3.5, "бутерброды": 0.6, "зажигалка": 0.25, "палатка": 4, "спальник": 3, "шампанское": 1,
                   "гречка": 0.5, "коврик": 1.5, "горелка": 0.8, "газ": 0.4, "фонарик": 0.2}

print(things_for_hike)

MIN_WEIGHT = min(things_for_hike.values())
MAX_WEIGHT = float(input("Введите максимальную вместимость рюкзака в кг: "))

# Список весов оборудования
list_weight = things_for_hike.values()
weight = 0

# Находим все возможные комбинации весов до заданного максимального веса:
comb_list_weight = []
index = 0
for i in range(1, len(list_weight)):
    temp = combinations(list_weight, i)
    for j in list(temp):
        index = index + 1
        sum_j = sum(j).__round__(2)
        if (MAX_WEIGHT - MIN_WEIGHT).__round__(2) < sum_j <= MAX_WEIGHT:
            comb_list_weight.append(j);
            # print(f'Возможный список весов {index}: {j}, {sum_j:.2f}')

# Вытаскиваем по весам предметы из листа возможных, и печатаем
count = 0;
for item in comb_list_weight:
    temp = []
    for element in item:
        for key, value in things_for_hike.items():
            if value == element:
                if key not in temp:
                    temp.append(key)
    count += 1
    print(f'Вариант комплектации рюкзака №{count}: {temp}. Вес рюкзака {sum(item).__round__(2)}')

