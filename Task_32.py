'''
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не меньше
заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''
from random import randint

# Решение 1, генерируем минимум и максимум
# на основе заданного изначально списка

def mini_maxi_list(list_elem):
    mini_element = randint(min(list_elem), max(list_elem))
    maxi_element = randint(max(list_elem), 100)
    list_out = []
    for i in range(len(list_elem)):
        if mini_element <= list_elem[i] <= maxi_element:
            list_out.append(i)
    return list_out

# Решение 2, список, а также минимум и максимум задаёт пользователь

def fill_list():
    my_list = [int(i) for i in input(
        'Задайте элементы списка через пробел: ').split()]
    return my_list


def search_index(list_elem):
    min_max_list = [int(i) for i in input(
        'Введите максимум и минимум через пробел: ').split()]
    list_out = []
    for i in range(len(list_elem)):
        if min_max_list[0] <= list_elem[i] <= min_max_list[-1]:
            list_out.append(i)
    return list_out


list_in = [-5, 9, 0, 3, -1, -2, 1,
           4, -2, 10, 2, 0, -9, 8, 10, -9,
           0, -5, -5, 7]
print(f"Заданный список:\n {list_in}")
print(f"Индексы случайных мин и макс элементов:\n {mini_maxi_list(list_in)}")
print()

specified_list = fill_list()
print(f"Заданный список:\n {specified_list}")
print(f"Индексы искомых элементов:\n {search_index(specified_list)}")
