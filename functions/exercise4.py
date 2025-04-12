# Задача 4


def sort_by_cost(dict_list, category=None):
    if category:
        filtered_products = [product for product in dict_list if product['category'] == category]
    else:
        filtered_products = [product for product in dict_list]

    sorted_products = sorted(filtered_products, key=lambda x: x['price'], reverse=True)

    return sorted_products


product_dict_list = ({'name': "Бананы", 'price': 150, 'category': "Фрукты", 'quantity': 5},
                     {'name': "Яблоки", 'price': 110, 'category': "Фрукты", 'quantity': 10},
                     {'name': "Тыква", 'price': 70, 'category': "Овощи", 'quantity': 2},
                     {'name': "Огурцы", 'price': 130, 'category': "Овощи", 'quantity': 4},
                     )

for product in sort_by_cost(product_dict_list, ):
    print(product)
