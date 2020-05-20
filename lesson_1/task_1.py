"""
Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
Полученная строка выводится в главной функции.
Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
"""

CELL_FORMATION_LAMB = lambda r, c: r * c if r != 0 and c != 0 else r + c
PRETTY_PRINT_LAMB = lambda num_arr: '\t'.join(map(str, num_arr))


def generate_table(rows_count, cols_count):
    for row in range(rows_count + 1):
        yield [CELL_FORMATION_LAMB(row, col) for col in range(cols_count + 1)]


def main():
    rows_count = int(input('Enter rows\n'))
    cols_count = int(input('Enter cols\n'))
    table = generate_table(rows_count, cols_count)
    print(f'Table {rows_count}x{cols_count}:')
    [print(PRETTY_PRINT_LAMB(line)) for line in table]


if __name__ == '__main__':
    main()
