'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
специальный символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
'''

def my_sum():
    user_var = input('Введите числа через пробел. После завершения нажмите клавишу Enter.\n>>>')
    len_list = len(user_var.split())
    idx = 0
    result_end = 0
    result_end2 = 0
    user_list = []
    while idx < len_list:

        try:
            if user_var.split()[0] == 'q':
                result_end2 = 0
                break
            elif user_var.split()[idx] == 'q':
                result_end = sum(user_list)
                break

            else:
                user_value = int(user_var.split()[idx])
        except ValueError as e:
            print(f'{e}\nНеверное значение данных.')
            break

        user_list.append(user_value)
        idx += 1
    result = sum(user_list)
    return result, result_end, result_end2


total = []

while True:
    result, result_end, result_end2 = my_sum()
    if result_end2:
        total.append(result_end2)
        print(f'Общий результат: {sum(total)}')
        break
    elif result_end:
        total.append(result_end)
        print(f'Общий результат: {sum(total)}')
        break

    else:
        total.append(result)
        print(f'Промежуточный итог: {sum(total)}')
