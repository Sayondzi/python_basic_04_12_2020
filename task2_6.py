'''
Реализовать структуру данных "Товары". Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два 
элемента - номер товара и словарь с параметрами (характеристиками товара:
название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
    [
    (1, {"название": "компьютер", "цена": 20000, "количествво": 5, "ед": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количествво": 2, "ед": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количествво": 7, "ед": "шт."})
    ]

Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ -
характеристика товара, например название, а значение - список значений-характеристик,
например список названий товаров.

Пример:
    {
    "название": ["компьютер", "принтер", "сканер"]
    "цена": [20000, 6000, 2000],
    "количество": [5, 2, 7],
    "ед.": ["шт."]
    }
'''

# Реализация кода, рассмотренного на уроке.

product_template = {
    'название': ("имя товара", str),
    'цена': ("стоимость товара", int),
    'количество': ("количество товара", int),
    'ед': ("Единицы измерения (шт., кг, л и т.д.)", str)
}

next_enter = True

auto_inc = 1
product_list = []

while next_enter:
    product = {}
    for key, value in product_template.items():
        while True:
            user_value = input(f'{value[0]}\n>>>')
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f'{e}\nНеверное значение данных.')
                continue
            product[key] = user_value
            break
    product_list.append((auto_inc, product))
    auto_inc += 1
    
    while True:
        next_add = input('Добавить ещё продукт? Да/Нет\n>>>')
        if next_add.lower() in ('да', 'нет'):
            next_enter = next_add.lower() == 'да'
            break
        else:
            print('Неверный ввод, повторите.')

print('#'*40, '\n', product_list)

products_analytics = {}

for key in product_template:
    result = []
    for itm in  product_list:
        result.append(itm[1][key])
    products_analytics[key] = result
    
print('-'*40, '\n',  products_analytics, '\n', '#'*40)
