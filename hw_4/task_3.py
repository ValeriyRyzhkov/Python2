# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

rand_list = []
n = int(input("Задайте количество чисел в списке: "))
for i in range(n):
	rand_list.append(random.randint(1,9))
print('Случайный список чисел:', rand_list)

new_list = [i for i in rand_list if rand_list.count(i) == 1]

print(f"Список неповторяющихся элементов списка из {n} элементов: = {new_list}")