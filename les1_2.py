user_name = input("Введите ваше имя\n>>>")

user_age = input("Введите ваш возраст\n>>>")

if user_age.isdigit():
    user_age = int(user_age)
else:
    print(user_name, ", ошибка ввода возраста, введите число")
    exit()

print("Добрый день, ", user_name)
# sys_message = 'Пользователь {} в возрасте {} лет вошёл в систему'.format(user_name, user_age)
# В фигурных скобках можно указать индексы либо имена переменных
# sys_message = 'Пользователь {0} в возрасте {1} лет вошёл в систему'.format(user_name, user_age)
# sys_message = 'Пользователь {name} в возрасте {age} лет вошёл в систему'.format(name=user_name, age=user_age)
sys_message = f'Пользователь {user_name} в возрасте {user_age} лет вошёл в систему'
print(sys_message)

if user_age >= 18:
    print("Доступ разрешён в ХХХ")
elif user_age >= 16:
    print("Доступ к боевикам")
else:
    print("Ограниченный доступ")

print('Отсчёт возраста')

temp_age = user_age
while temp_age > 0:
    if not temp_age & 1:
        temp_age -= 1
        continue
    print(temp_age)
    if temp_age == 15:
        break
    # temp_age = temp_age - 1
    temp_age -= 1
else:
    print("Сработал 'else' цикла")