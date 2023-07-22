# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

my_dict = {'Bob': ('сумка', 'палатка', 'котелок', 'спальник'),
           'Bart': ('сумка', 'палатка', 'чайник', 'спальник'),
           'Homer': ('мангал', 'палатка', 'еда', 'спальник'),
           }


# Какие вещи взяли все три друга
all_item = set()
for i in my_dict:
    all_item = all_item.union(set(my_dict[i]))
print(f'все предметы: {all_item}')

inter_item = all_item
for i in my_dict:
    inter_item = inter_item.intersection(set(my_dict[i]))
print(f'предметы, которые взял каждый из друзей: {inter_item}')


# Какие вещи уникальны, есть только у одного друга

new_dict = {}
for i in my_dict:
    for j in my_dict[i]:
        if j not in new_dict:
            new_dict[j] = []
        new_dict[j].append(i)
# print(new_dict)

uniqe_item = []
for i in new_dict:
    if len(new_dict[i]) == 1:
        uniqe_item.append(i)
print(f'уникальные вещи: {uniqe_item}')

# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует

new_dict2 = {}
for i in new_dict:
    if len(my_dict) - len(new_dict[i]) == 1:
        new_dict2[i] = set(my_dict).difference(set(new_dict[i]))
print(f'у всех друзей кроме одного: {new_dict2}')

