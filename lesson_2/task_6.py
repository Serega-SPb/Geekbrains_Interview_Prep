"""
Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.
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

    def get_info(self):
        raise NotImplementedError('Method not implemented')


class ItemDiscountReport(ItemDiscount):

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.__discount = discount

    def get_parent_data(self):
        return f'Name: {self.name} Price: {self.price}'

    def __str__(self):
        return f'<ItemDiscountReport>(Name: {self.name} Price(with discount): {self.price - self.price * self.__discount / 100})'


class ItemDiscountReportName(ItemDiscount):

    def get_info(self):
        return self.name

    @staticmethod
    def get_info_st(item: ItemDiscount):
        return item.name


class ItemDiscountReportPrice(ItemDiscount):

    def get_info(self):
        return self.price

    @staticmethod
    def get_info_st(item: ItemDiscount):
        return item.price


def main():
    name = input('Enter item name\n') or 'test'
    price = int(input('Enter item price\n') or 100)

    item = ItemDiscount(name, price)
    item_rep_name = ItemDiscountReportName(name, price)
    item_rep_price = ItemDiscountReportPrice(name, price)

    print('-' * 10)
    items_array = [item_rep_name, item_rep_price]
    [print(it.get_info()) for it in items_array]

    print('-' * 10)
    items_cl_array = [ItemDiscountReportName, ItemDiscountReportPrice]
    func_name = 'get_info_st'
    for it in items_cl_array:
        if hasattr(it, func_name):
            print(getattr(it, func_name)(item))

    print('-' * 10)
    print(item_rep_name.get_info())
    print(item_rep_price.get_info())

    print('-' * 10)
    try:
        item.get_info()
    except Exception as e:
        print(f'{type(e).__name__}: {e}')


if __name__ == '__main__':
    main()
