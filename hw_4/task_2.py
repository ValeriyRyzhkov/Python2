# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите натуральное число N: "))
numbers = []
a = 2
m = n 
while a * a <= n:
        if n % a == 0:
            numbers.append(a)
            n//=a
        else:
            a += 1
numbers.append(n) 
print(f'Cписок простых множителей числа {m} = {numbers}') 