"""
Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и
подготовить два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы.
Применить к спискам функцию zip(). Результат выполнения этой функции должен должен быть обработан и
записан в файл таким образом, чтобы каждая строка файла содержала текстовое и числовое значение.
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции.
"""

import os
import random
import string


class TaskFour:

    ARR_SIZE = random.randint(5, 10)
    WORD_LEN = random.randint(5, 10)
    SEP = ' '
    WRITE_LAMB = lambda s, t: f'{t[0]}{s.SEP}{t[-1]}'

    def generate_int_array(self, size):
        for i in range(size):
            yield random.randint(1, 100)

    def generate_str_array(self, size):
        for i in range(size):
            yield ''.join(random.choice(string.ascii_letters) for _ in range(self.WORD_LEN))

    def write_data(self, filepath):
        if os.path.isfile(filepath):
            print(f'{filepath} already exist and will be overwritten')
            answer = input('Continue (Y/n)?\n') or 'y'
            if answer.lower() != 'y':
                return

        int_arr = self.generate_int_array(self.ARR_SIZE)
        str_arr = self.generate_str_array(self.ARR_SIZE)
        zippped_arr = zip(int_arr, str_arr)

        print('Writing to file...')
        with open(filepath, 'w', encoding='utf-8') as writer:
            writer.write('\n'.join(map(self.WRITE_LAMB, zippped_arr)))
        print('Complete')
        self.read_file(filepath)

    def read_file(self, filepath):
        print('Reading from file...')
        with open(filepath, 'r', encoding='utf-8') as reader:
            self._content = reader.read().split('\n')
        for line in self._content:
            print(line)
        print('Complete')


def main():
    file = input('Enter filename\n') or 'test.txt'
    inst = TaskFour()
    inst.write_data(file)


if __name__ == '__main__':
    main()
