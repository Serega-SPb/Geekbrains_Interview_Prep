"""
Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения,
в словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
"""

import random
from itertools import zip_longest as zip_l


def generate_array(pref, range_from=5, range_to=10):
    size = random.randint(range_from, range_to)
    return [f'{pref}_{i}' for i in range(size)]


def main():
    keys = generate_array('key')
    values = generate_array('values')

    result = {key: value for key, value in zip_l(keys, values) if key}

    print(f'Keys:\n {keys}')
    print(f'Values:\n {values}')

    print(f'Result dictionary:\n {result}')


if __name__ == '__main__':
    main()
