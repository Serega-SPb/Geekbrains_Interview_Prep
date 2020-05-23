"""
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться
фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать
вложенную функцию подсчета процентов для пополняемой суммы. Примем, что клиент вносит средства
в последний день каждого месяца, кроме первого и последнего. Например, при сроке вклада в 6 месяцев
пополнение происходит в течение 4 месяцев. Вложенная функция возвращает сумму дополнительно
внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец периода.
"""

from task_4 import BEGIN_SUM, END_SUM, DEPOSIT_PRODUCTS


def bank_deposit_upd(deposit, dep_time, add_sum):

    def calc_add_profit(add_time, perc_m):
        add_profit = 0
        for i in range(1, add_time + 1):
            add_profit += add_sum + add_sum * i * perc_m
        return add_profit

    for prod in DEPOSIT_PRODUCTS:
        if prod[BEGIN_SUM] <= deposit < prod[END_SUM]:
            percent = prod[dep_time] / 100
            mult = dep_time / 12
            profit = deposit * percent
            return deposit + profit * mult + calc_add_profit(dep_time - 2, percent/12)
    else:
        print('Product not found')
    return deposit


def main():
    deposit = int(input('Enter deposit sum\n'))
    dep_time = int(input('Enter deposit time (6, 12 , 24)\n'))
    add_sum = int(input('Enter additional sum\n'))
    print(bank_deposit_upd(deposit, dep_time, add_sum))


if __name__ == '__main__':
    main()
