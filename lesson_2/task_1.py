"""
Проверить механизм наследования в Python. Для этого создать два класса.
Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре: название и цену.
Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
отвечающую за отображение информации о товаре в одной строке.
Проверить работу программы, создав экземпляр (объект) родительского класса.
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.name = name
        self.price = price


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
