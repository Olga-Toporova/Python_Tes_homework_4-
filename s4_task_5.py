'''
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов
'''

def poly_list (first, second):
    with open(first, "r", encoding = "utf-8") as file_1, \
        open(second, "r", encoding = "utf-8") as file_2:
        first_file = file_1.readlines()
        second_file = file_2.readlines()

        if len(first_file) == len(second_file):
            with open("for_task_5.txt", "a", encoding = "utf-8") as result:
                for i,k in enumerate(first_file):
                    result.write(f"{k[:-5]} + {second_file[i]}")
        else: 
            print("The contents of the files do not match!")
poly_list("poly.txt", "poly_2.txt")