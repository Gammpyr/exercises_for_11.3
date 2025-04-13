from datetime import datetime


def orders_analyse(list_dict):
    dict_for_count = {}

    for order in list_dict:
        order_date = datetime.strptime(order['date'], '%Y-%m-%d')
        cur_time = order_date.strftime('%Y-%m')

        if cur_time not in dict_for_count:
            dict_for_count[cur_time] = {
                'order_value': 0,
                'order_count': 0,
            }

        dict_for_count[cur_time]['order_count'] += 1
        for price in order['items']:
            dict_for_count[cur_time]['order_value'] += price['price'] * price['quantity']

    result = {}
    for month in dict_for_count:
        avg_order_value = dict_for_count[month]['order_value'] / dict_for_count[month]['order_count']
        result[month] = {
            'average_order_value': avg_order_value,
            'order_count': dict_for_count[month]['order_count']
        }
    return result


orders = [
    {
        "id": 1,
        "date": "2023-05-15",
        "items": [
            {"name": "item1", "price": 100, "quantity": 2},
            {"name": "item2", "price": 50, "quantity": 1}
        ]
    },
    {
        "id": 2,
        "date": "2023-05-20",
        "items": [
            {"name": "item3", "price": 200, "quantity": 1},
            {"name": "item4", "price": 150, "quantity": 2}
        ]
    },
    {
        "id": 3,
        "date": "2023-06-05",
        "items": [
            {"name": "item5", "price": 300, "quantity": 1}
        ]
    }
]
print(orders_analyse(orders))
