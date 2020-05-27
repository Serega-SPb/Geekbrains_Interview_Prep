"""
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением. В функции необходимо
реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).
"""

import os


def get_filename(file):
    fullpath = os.path.abspath(file)
    filename = os.path.basename(fullpath)
    return os.path.splitext(filename)[0]


def main():
    file = input('Enter file\n') or __file__
    print(get_filename(file))


if __name__ == '__main__':
    main()
