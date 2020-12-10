user_range = input('Введите расстояние(в км), которое преодалевает спортсмен за один день:\n>>>')
distance = input('Укажите дистанцию, которую необходимо преодолеть спортсмену\n>>>')

if distance.isdigit() and user_range.isdigit():
    distance = int(distance)
    user_range = int(user_range)
else:
    print("Вы вели некорректные данные.")
    exit()

user_day = 1

while user_range < distance:
    user_range = user_range * 1.1
    user_day += 1
else:
    sys_message = f'На {user_day} день спортсмен преодолеет дистанцию - не менее {distance} км.'
    print(sys_message)
