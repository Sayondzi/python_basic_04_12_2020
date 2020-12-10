user_name = input("Добрый день.\nПожалуйста, представьтесь.\n>>>")
user_variable = input("Введите целое положительное число:\n>>>")

if user_variable.isdigit():
    user_variable = int(user_variable)
else:
    print(user_name, ", необходимо было ввести число.")
    exit()

user_variable1 = str(user_variable)
# преобразование числа в строку
a_max = int(user_variable1[0])
# по умолчанию считаем максимальным крайний левый символ числа
k = 1
while k < (len(user_variable1)):
    if a_max > int(user_variable1[k]):
        k += 1
        continue
    else:
        a_max = int(user_variable1[k])
        k += 1

sys_message = f'Пользователь {user_name} ввёл число {user_variable}.\nСамая большая цифра в  данном числе - {a_max}.'
print(sys_message)
