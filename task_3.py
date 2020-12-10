user_name = input("Добрый день.\nПожалуйста, представьтесь.\n>>>")
user_variable = input("Введите целое число:\n>>>")

if user_variable.isdigit():
    user_variable = int(user_variable)
else:
    print(user_name, ", необходимо было ввести число.")
    exit()
variable = user_variable + int(str(user_variable) + str(user_variable)) + int(str(user_variable) + str(user_variable) + str(user_variable))
sys_message = f'Пользователь {user_name} ввёл число {user_variable}.\nСумма чисел {user_variable}+{user_variable}{user_variable}+{user_variable}{user_variable}{user_variable} равна {variable}.'
print(sys_message)
