"""
Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""
import re


def check_number_type(num):
    if num.isdigit():
        print(f'{num} is integer')
        return
    elif num.isalnum():
        print(f'{num} isn`t number')
        return
    else:
        print(f'{num} is float')
        num = num.replace(',', '.')
        left_part, right_part = map(int, num.split('.'))
        return left_part == right_part


INT_PATTERN = r'\d+'
FL_PATTERN = r'\d+[.,]\d+'


def re_check_number_type(num):
    if re.fullmatch(INT_PATTERN, num):
        print(f'{num} is integer')
        return
    elif re.fullmatch(FL_PATTERN, num):
        print(f'{num} is float')
        num = num.replace(',', '.')
        left_part, right_part = map(int, num.split('.'))
        return left_part == right_part
    else:
        print(f'{num} isn`t number')
        return


def main():
    num = input('Enter number\n')
    print(f'{"String func":-^50}')
    try:
        result = check_number_type(num)
        if result is not None:
            r_word = "is" if result else "isn`t"
            print(f'The left side {r_word} equal to the right side of the number')
    except Exception as e:
        print(e)

    print(f'{"Regex func":-^50}')
    result = re_check_number_type(num)
    if result is not None:
        r_word = "is" if result else "isn`t"
        print(f'The left side {r_word} equal to the right side of the number')


if __name__ == '__main__':
    main()
