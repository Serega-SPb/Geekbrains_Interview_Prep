"""
Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего
(функция, отвечающая за отображение информации о товаре в одной строке).
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

    @price.setter
    def price(self, value):
        self.__price = value


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Name: {self.name} Price: {self.price}'


def main():
    name = input('Enter item name\n') or 'test'
    price = int(input('Enter item price\n') or 100)

    item = ItemDiscount(name, price)
    item_rep = ItemDiscountReport(name, price)
    print(item_rep.get_parent_data())

    new_price = int(input('Enter new item price\n') or 1000)

    item.price = new_price
    item_rep.price = new_price
    print(item_rep.get_parent_data())


if __name__ == '__main__':
    main()
