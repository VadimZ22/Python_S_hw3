# ✔ Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

my_list = [1, 1, 4, 5, 7, 3, 6, 8, 2, 35, 6, 'q', 's', 's', 'r', 'q', [1,2,3], [1,2,3]]
dub_list = []
for i in my_list:
    if i not in dub_list and my_list.count(i) == 2:
        dub_list.append(i)
print(dub_list)
