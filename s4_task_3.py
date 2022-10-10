'''
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
'''

def filter_unique_numbers(some_list):
    return [i for i in some_list if some_list.count(i)==1]

num_list = list(map(int, input("Введите значения через пробел: ").split()))
print(num_list)
print(filter_unique_numbers(num_list))