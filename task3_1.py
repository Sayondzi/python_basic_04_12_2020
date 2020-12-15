"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую
их деление. Числа запрашивать у пользователя.
Предусмотреть обработку ситуации деления на ноль.
"""

while True:
    user_var1 = input("Введите первое число\n>>>")
    try:
        user_var1 = int(user_var1)
    except ValueError as e:
        print(f'{e}\nЗаданы некорректные условия.\nНеверное значение данных.')
        continue
    break

while True:
    user_var2 = input("Введите второе число\n>>>")
    try:
        user_var2 = int(user_var2)
    except ValueError as e:
        print(f'{e}\nЗаданы некорректные условия.\nНеверное значение данных.')
        continue
    if user_var2 == 0:
        print('Заданы некорректные условия. \nНа ноль делить нельзя.')
        continue
    break

def division(user_var1, user_var2):
    result = user_var1 / user_var2
    return result

print(division(user_var1, user_var2))
