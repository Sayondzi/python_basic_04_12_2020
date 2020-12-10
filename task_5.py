user_name = input("Добрый день.\nПожалуйста, представьтесь.\n>>>")
proceeds = input("Укажите выручку вашей фирмы в тыс. руб. за отчётный период:\n>>>")
costs = input("Укажите величену издержек в тыс. руб. за тот же период:\n>>>")

if proceeds.isdigit() and costs.isdigit():
    proceeds = int(proceeds)
    costs = int(costs)
else:
    print(user_name, ", Вы вели некорректные данные.")
    exit()

profit = proceeds - costs

if profit < 0:
    print(user_name, ", Вам стоит задуматься о будущем!\nВозможно, имеет смысл сменить род деятельности.")
elif profit == 0:
    print("Хорошая новость,", user_name,", Вы не в убытке, но и прибыли нет.")
else:
    print(user_name, "поздравляю! Ваша фирма приносит доход!")
    rentability = profit / proceeds
    workers = int(input("Укажите количество сотрудников вашей фирмы:\n>>>"))
    workers_rentability = profit / workers
    sys_message = f'Рентабельность вашей фирмы сотавляет: {rentability}.\nПрибыль фирмы в расчёте на одного сотрудника составит: {workers_rentability} т.руб.'
    print(sys_message)
