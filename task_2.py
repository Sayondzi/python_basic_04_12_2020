user_name = input("Добрый день.\nПожалуйста, представьтесь.\n>>>")
user_time = input("Введите количество секунд для перевода в часы:\n>>>")

if user_time.isdigit():
    user_time = int(user_time)
else:
    print(user_name, ", ошибка ввода, введите число")
    exit()

time_oclock = int(user_time / 3600)
time_minute = int((user_time % 3600) / 60)
time_sec = user_time - time_oclock * 3600 - time_minute * 60

sys_message = f'Пользователь {user_name} ввёл {user_time} секунд.\nВ переводе это составит - {time_oclock}:{time_minute}:{time_sec}.'
print(sys_message)
