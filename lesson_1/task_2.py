"""
Дополнить следующую функцию недостающим кодом:
"""

import os


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """

    if not os.path.isdir(sPath):
        print(f'{sPath} is not directory')
        return

    dirs = []
    dirs_full = []
    files = []
    for path in os.listdir(sPath):
        full_path = os.path.join(sPath, path)
        if os.path.isdir(full_path):
            dirs.append(path)
            dirs_full.append(full_path)
        else:
            files.append(path)
    data = (sPath, dirs, files)
    print(data)
    [print_directory_contents(d) for d in dirs_full]


def main():
    s_path = input('Enter path to walk\n')
    print_directory_contents(s_path)


if __name__ == '__main__':
    main()
