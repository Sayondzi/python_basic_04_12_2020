"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
"""
auto_inc = 1
user_list = []

while True and auto_inc <= 3:
    user_var = input(f'Введите {auto_inc}-е целое число:\n>>>')
    if user_var.isdigit():
        user_var = int(user_var)
        user_list.append(user_var)
        auto_inc += 1
        continue
    else:
        print('Ошибка ввода, это не число.')

def my_func(*result):
    var_min = min(user_list)
    auto_inc = 1
    while auto_inc < (len(user_list)):
        if var_min == user_list[auto_inc]:
            user_list.pop(auto_inc)
            break
        else:
            auto_inc += 1
    result = sum(user_list)
    return result

print('#'*40, '\n', f'Сумма двух наибольших чисел: {my_func(user_list)}', '\n', '#'*40)
