"""
Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число).
Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений.
Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
"""

import re
import random
import string

from task_4 import TaskFour


class TaskFive(TaskFour):

    @property
    def alphanum_pat(self):
        return rf'\d+{self.SEP}\w+\d+'

    def generate_str_array(self, size):
        for i in range(size):
            item = ''.join(random.choice(string.ascii_letters) for _ in range(self.WORD_LEN))
            if i % 3 == 0:
                item += str(random.randint(100, 1000))
            yield item

    def read_file(self, filepath):
        super(TaskFive, self).read_file(filepath)
        self.search_substring()
        self.search_alphanums()

    def search_substring(self):
        print(f'{"Search substrings":-^35}')
        substr = input('Enter substring\n')
        regex = re.compile(f'.*{substr}.*')
        sub_arr = list(filter(regex.match, self._content))

        print(f'First entry {substr}: {sub_arr[0]}')
        print(f'All entries with {substr}: {sub_arr}')

        self._content = [re.sub(substr, 'TEST', d) for d in self._content]
        print(f'Updated content (replaced {substr} -> TEST)')
        [print(d) for d in self._content]

    def search_alphanums(self):
        print(f'{"Search alphanum strings":-^35}')
        regex = re.compile(self.alphanum_pat)
        alphanums = list(filter(regex.match, self._content))
        [print(s) for s in alphanums]


def main():
    file = input('Enter filename\n') or 'test.txt'
    inst = TaskFive()
    inst.write_data(file)


if __name__ == '__main__':
    main()
