'''
Реализовать структуру "Рейтинг", представляющую собой невозрастающий
набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то
новый элемент с тем же значением должен разместиться после них.

####################
Подсказка
    Например, набор натуральных чисел:    7, 5, 3, 3, 2.
    Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
    Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
    Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например,
my_list = [7, 5, 3, 3, 2].
####################
'''

my_list = [7, 5, 3, 3, 2]

while True:
    user_rating = input('Укажите новый элемент рейтинга\n>>>')
    if user_rating.isdigit():
        user_rating = int(user_rating)
        break
    else:
        print('Ошибка ввода, необходимо указать натуральное число.')

len_list = len(my_list)
idx = 0
while idx < len_list:
    if user_rating > my_list[idx]:
        my_list.insert(idx, user_rating)
        break
    elif user_rating == my_list[idx] and user_rating > my_list[idx + 1]:
        my_list.insert(idx+1, user_rating)
        break
    elif user_rating <= my_list[len_list-1]:
        my_list.append(user_rating)
        break
    else:
        idx += 1

print(my_list)