"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
"""

while True:
    user_month = input('Укажите порядковый номер месяца.\n>>>')
    if user_month.isdigit():
        user_month = int(user_month)
        if 1 <= user_month <= 12:
            break
        else:
            print(f'Похоже, дрогнула рука.\nПопробуйте ещё.')
    else:
        print('Ошибка ввода, необходимо указать целое число.')

year_dict ={
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11],
}

k=1
for key in year_dict:
    if user_month in year_dict[key] != True:
        break
    else:
        k += 1
print(f'{key}')

