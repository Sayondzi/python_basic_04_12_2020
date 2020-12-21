'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''
from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


basic_list = (100, 1000)
print(reduce(my_func, [el for el in range(basic_list[0], basic_list[1] + 1) if el % 2 == 0]))
