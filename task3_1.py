"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую
их деление. Числа запрашивать у пользователя.
Предусмотреть обработку ситуации деления на ноль.
"""
user_var1 = int(input("Введите первое число\n>>>"))
user_var2 = int(input("Введите второе число\n>>>"))

def division(user_var1, user_var2):
    if user_var2 == 0:
        print('Заданы некорректные условия. \nНа ноль делить нельзя.')
        exit()
    else:
        result = user_var1 / user_var2
    return result

print(division(user_var1, user_var2))


