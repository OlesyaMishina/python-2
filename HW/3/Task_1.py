# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42, 6, 6]
duplicados = []
for item in set(data):
    if data.count(item) > 1:
        duplicados.append(item)
print(duplicados)

my_dict = {el for el in set(data) if data.count(el) > 1}
print(my_dict)

lst_nums = [0, 0, 1, 2, 2, 3, 3, 3, 6, 7, 1, 1, 15, 15, 15, 17]
set_nums = set(lst_nums)
for num in set_nums:
    lst_nums.remove(num)
print(set(lst_nums))