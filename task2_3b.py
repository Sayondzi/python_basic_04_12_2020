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

year_list =[ 'зима', 'весна', 'лето', 'осень']

if  2 < user_month <6:
    print(year_list[1])
elif 6 <= user_month < 9:
    print(year_list[2])
elif 9 <= user_month < 12:
    print(year_list[3])
else:
    print(year_list[0])
