"""
Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
"""

class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Name: {self.name} Price: {self.price}'


def main():
    name = input('Enter item name\n') or 'test'
    price = int(input('Enter item price\n') or 100)

    try:
        item = ItemDiscount(name, price)
        item_rep = ItemDiscountReport(name, price)
        print(item_rep.get_parent_data())
    except Exception as e:
        print(f'{type(e).__name__}: {e}')


if __name__ == '__main__':
    main()
