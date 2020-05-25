"""
Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Name: {self.name} Price: {self.price}'


def main():
    name = input('Enter item name\n') or 'test'
    price = int(input('Enter item price\n') or 100)

    item = ItemDiscount(name, price)
    item_rep = ItemDiscountReport(name, price)
    print(item_rep.get_parent_data())


if __name__ == '__main__':
    main()
