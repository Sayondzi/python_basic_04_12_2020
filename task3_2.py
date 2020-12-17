"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

var_template = {
    'Name': ('Укажите Ваше имя:', str),
    'Surname': ('Укажите Вашу фамилию:', str),
    'Birthday': ('Ваш год рождения (необходимо указать число в формате XXXX)', int),
    'City': ('Город проживания:', str),
    'Email': ('Электронная почта:', str),
    'Telephone': ('Телефон:', int),
}
'''

def user_worksheet(var_template):

    user  = {}
    for key, value in var_template.items():
        while True:
            user_value = input(f'{value[0]}\n>>>')
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f'{e}\nНеверно указаны данные.')
                continue
            user[key] = user_value
            break
    return user

print('#'*40, '\n', user_worksheet(var_template))

'''

def user_worksheet(*user):

    user  = {}
    for key, value in var_template.items():
        while True:
            user_value = input(f'{value[0]}\n>>>')
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f'{e}\nНеверно указаны данные.')
                continue
            user[key] = user_value
            break
    return user
user_dict = user_worksheet(var_template)
print('#'*40, f'\n{user_dict}\n', '#'*40)
print(f"Имя: {user_dict.get('Name')}; Фамилия: {user_dict.get('Surname')}; Год рождения: {user_dict.get('Birthday')}; Город: {user_dict.get('City')}; Email: {user_dict.get('Email')}; Тел.: {user_dict.get('Telephone')}.", '\n', '#'*40)


