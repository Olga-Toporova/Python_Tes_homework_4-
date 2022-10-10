'''
Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.
'''

def multiplier (n):
    result = []
    for i in range(2, n+1):            
        if n % i == 0: 
            while n % i ==0:
                n /= i
                result.append(i)
        else: 
            continue
    return result


N = int(input("Введите натуральное число N: "))
print(multiplier(N))