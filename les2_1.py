"""
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333.
"""

print('#' * 40)
print('Вариант работы с числом)')
while True:
    user_num = input('Введите целое число\n>>>')
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print('Ошибка. Введено не число.')

count = 0
tmp = user_num

while tmp:
    # tmp = tmp // 10
    tmp //= 10
    count += 1

nn_div = 10 ** count + 1
nnn_div = (10 ** (count * 2)) + nn_div
result = user_num + (user_num * nn_div) + (user_num * nnn_div)

print(result)

print('#' * 40)
print('Вариант работы со строкой')

while True:
    user_num = input('Введите целое число\n>>>')
    if user_num.isdigit():
        break
    print('Ошибка. Введено не число.')

result = int(user_num) + int(user_num * 2) + int(user_num * 3)

print(result)

"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Длярешения используйте цикл while и арифметические операции
"""

print('#' * 40)
print('Вариант арифметический (работа с числом)')
while True:
    user_nun = input('Введите целое число\n>>>')
    if user_nun.isdigit():
        user_nun = int(user_nun)
        break
    else:
        print('Ошибка. Введено не число.')

result = 0
while user_nun and result != 9:
    tmp = user_nun % 10
    if tmp > result:
        result = tmp
    user_nun //= 10

print(result)

print('#' * 40)
print('Вариант работы со строкой')
while True:
    user_num = input('Введите целое число\n>>>')
    if user_num.isdigit():
        break
    else:
        print('Ошибка ввода, это не число.')

result = 9
while result:
    if str(result) in user_num:
        break
    result -= 1

print(result)

"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма 
(прибыль - выручка больше издержек, или убыток - издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы на одного сотрудника.
"""

while True:
    proceeds = input('Введите сумму выручки')
    if proceeds.isdigit():
        proceeds = int(proceeds)
        break
    print('Ошибка данных, введено не число.')

while True:
    cost = input('Введите сумму издержек')
    if cost.isdigit():
        cost = int(cost)
        break
    print('Ошибка данных, введено не число')

fin_result = proceeds - cost

if fin_result > 0:
    ratio = proceeds / cost
    print(f'ваша прибыль равна: {fin_result}, вы молодец\nсоотношение составляет {ratio}')
    while True:
        worker_count = input('Введите количество сотрудников')
        if worker_count.isdigit():
            worker_count = int(worker_count)
            break
        print('Ошибка данных, введено не число')
    profit_of_worker = fin_result / worker_count
    print(f'прибыль на одного сотрудника составляет: {profit_of_worker}')

elif not fin_result:
    print('Нет ни прибыли ни убытков, странный бизнес.')
else:
    print(f'Казна пустеет, милорд!\nВаши убытки составили: {fin_result}')


"""
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил 'a' километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее  'b' километров.
Программа должна принимать значения параметров 'a' и 'b' и выводить одно натуральное число - номер дня.
Например: 
    а = 2, b = 3.
Результат:
    1-й день: 2
    2-й день: 2,2
    3-й день: 2,42
    4-й день: 2,66
    5-й день: 2,93
    6-й день: 3,22
Ответ:
    На 6-й день спортсмен достиг результата - не менее 3 км.
"""

while True:
    user_a = input('Введите целое число результата в первый день\n')
    if user_a.isdigit():
        user_a = int(user_a)
        break
    else:
        print('Ошибка ввода, это не число.')

while True:
    user_b = input('Введите целое число - желаемый результат\n')
    if user_b.isdigit():
        user_b = int(user_b)
        break
    else:
        print('Ошибка ввода, это не число.')

day = 1
tmp = user_a
while tmp < user_b:
    tmp *= 1.1
    day += 1

print(day)
