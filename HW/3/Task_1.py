# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42, 6, 6]
duplicados = []
for item in set(data):
    if data.count(item) > 1:
        duplicados.append(item)
print(duplicados)
