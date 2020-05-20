"""
Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря
"""

import random


def random_generator(start, end):
    result = [start]
    num_break = end
    if start > end:
        start, end = end, start
    while True:
        num = random.randint(start, end)
        if num == 0:
            continue
        result.append(num)
        if num == num_break:
            break
    return result


def dict_from_array(array):
    return {f'elem_{num}': num for num in array}


def dict_from_array_index(array):
    return {f'elem_{i}': num for i, num in enumerate(array)}


def main():
    start = int(input('Enter start\n'))
    end = int(input('Enter end\n'))

    rand_array = random_generator(start, end)
    dict_from_arr = dict_from_array(rand_array)
    dict_from_arr_index = dict_from_array_index(rand_array)

    print(rand_array)
    print(dict_from_arr)
    print(dict_from_arr_index)


if __name__ == '__main__':
    main()
