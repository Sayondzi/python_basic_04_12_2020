"""
Для списка реализовать обмен значений соседних элементов, т.е. значениями
обмениваются элементы с индексом 0 и 1, 2 и 3 и т.д.
при нечётном количестве элементов последний сохранить на своём месте. Для
заполнения списка элементов необходимо использовать функцию input().
"""
user_list = []
i = 0

while True:
    user_data = input(f'введите {i + 1} - й компонент списка\n>>>')
    if user_data != '':
        user_list.append(user_data)
        i += 1
    else:
        print(user_list)
        break

idx = 0
while idx < len(user_list[:-1]):
    user_list[idx],user_list[idx+1] = user_list[idx+1],user_list[idx]
    idx += 2
print(user_list)
