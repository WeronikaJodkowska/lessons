"""Дана база данных (в виде текстового файла) о продажах некоторого интернет-магазина. Каждая строка входного файла
представляет собой запись вида Покупатель, Товар, Количество, Стоимость где Покупатель - имя покупателя (строка без
пробелов), товар - название товара (строка без пробелов), количество - количество приобретенных единиц товара.
a) Создайте список и выведите на экран всех покупателей, а для каждого покупателя подсчитайте общее количество
приобретенных им товаров и их стоимость.
b) Создайте список и выведите на экран все товары, а для каждого товара
подсчитайте общее количество приобретенных и их стоимость.
"""


def get_customer_sales(sales):
    # create sales_dict with names as keys and lists as values
    sales_dict = {customer: [] for customer, purchase, number, price in sales}
    # add values to sales_dict
    for customer, purchase, number, price in sales:
        sales_dict[customer].append([purchase, number, price])
    # through the keys
    for key, value in sales_dict.items():
        # number of the all purchased products of the customer
        number_sum = 0
        # price of the all purchased products of the customer
        price_sum = 0
        res_dict = {}
        res_list = []
        # through the values of key
        for i in value:
            number_sum += int(i[1])
            price_sum += int(i[2])
            res_list = [number_sum, price_sum]
        res_dict[key] = res_list
        for k, v in res_dict.items():
            print(f"Customer {k}: number of products - {v[0]}, total cost - {v[1]}")


def get_products_sales(sales):
    products_dict = {purchase: [] for customer, purchase, number, price in sales}
    # add values to sales_dict
    for customer, purchase, number, price in sales:
        products_dict[purchase].append([number, price])
    for key, value in products_dict.items():
        # number of purchased product
        products_number = 0
        # price of the purchased product
        total_price = 0
        res_dict = {}
        res_list = []
        # through the values of key
        for i in value:
            products_number += int(i[0])
            total_price += int(i[1])
            res_list = [products_number, total_price]
        res_dict[key] = res_list
        for k, v in res_dict.items():
            print(f"Product{k}: purchased - {v[0]}, total cost - {v[1]}")


def main():
    sales = []
    with open("sales.txt", "r") as file:
        for line in file:
            lines = line.strip().split(",")
            sales.append(lines)

    print("Customers products")
    get_customer_sales(sales)
    print("Products purchased:")
    get_products_sales(sales)


if __name__ == "__main__":
    main()
