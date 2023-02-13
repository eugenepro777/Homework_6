'''
Задача 30: Заполните массив элементами 
арифметической прогрессии. Её первый элемент,
разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Пример
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''


def progress(a1, d, n):
    progress_list = []
    for _ in range(n):
        progress_list.append(a1 + (n-1)*d)
        n -= 1
        progress_list.sort()
    return progress_list

first_element = int(input('Первый элемент прогрессии: '))
step = int(input('Задайте разность d (шаг прогрессии): '))
elements = int(input('Количество элементов: '))

print(progress(first_element, step, elements))

