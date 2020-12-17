"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

var_template = {
    'name': ('Укажите Ваше имя:', str),
    'surname': ('Укажите Вашу фамилию:', str),
    'birthday': ('Ваш год рождения (необходимо указать число в формате XXXX)', int),
    'city': ('Город проживания:', str),
    'email': ('Электронная почта:', str),
    'telephone': ('Телефон:', int),
}

def user_worksheet(name, surname, birthday, city, email, telephone):

    user_book = []

    while True:
        user_name = input(f'{name[0]}\n>>>')
        try:
            user_name = name[1](user_name)
        except ValueError as e:
            print(f'{e}\nНеверно указаны данные.')
            continue
        user_name = user_name.title()
        break
    user_book.append(user_name)
    while True:
        user_surname = input(f'{surname[0]}\n>>>')
        try:
            user_surname = surname[1](user_surname)
        except ValueError as e:
            print(f'{e}\nНеверно указаны данные.')
            continue
        user_surname = user_surname.title()
        break
    user_book.append(user_surname)

    while True:
        user_birthday = input(f'{birthday[0]}\n>>>')
        try:
            user_birthday = birthday[1](user_birthday)
        except ValueError as e:
            print(f'{e}\nНеверно указаны данные.')
            continue
        if user_birthday < 1900 or user_birthday > 2020:
            print('Пожалуйста, проверьте ещё раз введённые данные.')
            continue
        break
    user_book.append(user_birthday)

    while True:
        user_city = input(f'{city[0]}\n>>>')
        try:
            user_city = city[1](user_city)
        except ValueError as e:
            print(f'{e}\nНеверно указаны данные.')
            continue
        user_city = user_city.title()
        break
    user_book.append(user_city)

    while True:
        user_email = input(f'{email[0]}\n>>>')
        try:
            user_email = email[1](user_email)
        except ValueError as e:
            print(f'{e}\nНеверно указаны данные.')
            continue
        break
    user_book.append(user_email)

    while True:
        user_telephone = input(f'{telephone[0]}\n>>>')
        try:
            user_telephone = telephone[1](user_telephone)
        except ValueError as e:
            print(f'{e}\nНеверно указаны данные.')
            continue
        break
    user_book.append(user_telephone)

    return user_book

print(user_worksheet(**var_template))