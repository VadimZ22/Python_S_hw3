# ✔ Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
from random import choice

items = {'палатка':2, 'стул':1, 'лампа':0.3, 'сумка':1, 'спальник':2, 'мангал':3, 'еда':3, 'котелок':1}
bag_capacity = 10
weight = 0
list_items = list(items.items())
item_in_bag = []
while weight <= bag_capacity:
#print(list_items)
    temp = list_items.pop(list_items.index(choice(list_items)))
    weight += temp[1]
    item_in_bag.append(temp[0])
weight -= temp[1]
item_in_bag.pop(-1)

print(f'вес: {weight}')
print(f'предметы: {item_in_bag}')


