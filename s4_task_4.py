'''
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
-  k=4 => 2*x^4 + 4*x^3 + 5x^2  - 3x + 3 = 0
'''

import random
from random import choice


def write_file(str):
    with open('for_task_4.txt', 'a') as file:
        file.write(f'{str} \n')

def create_str(list_in):
    new_list = list_in[::-1]
    write = ''
    length = len(new_list)
    if length == 1:
        write = 'x = 0'
    else:
        for i in range(length):
            if i != new_list[i] and new_list[i] == 0: write += f"{choice('+-')} "
            elif i != length - 1 and new_list[i] != 0 and i != length - 2:
                write += f'{new_list[i]}x^{length-i-1} '
                if new_list[i+1] != 0 and new_list[i] > 0: write += f"{choice('+-')} "
            elif i == length - 2 and new_list[i] != 0:
                write += f'{new_list[i]}x '
                if new_list[i+1] != 0 and new_list[i] > 0: write += f"{choice('+-')} "
            elif i == length - 1 and new_list[i] != 0: write += f'{new_list[i]} = 0 '
            elif i == length - 1 and new_list[i] == 0: write += ' = 0 '
    return write

k = int(input("Введите натуральную степень k = "))
koef = [random.randint(0,10) for i in range(k)]
write_file(create_str(koef))