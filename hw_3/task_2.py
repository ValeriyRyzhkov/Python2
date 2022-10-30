# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def pair_of_numbers(array):
    result = []
    for i in range(len(array)):
        if(i > len(array) - i - 1):
            break
        result.append(array[i] * array[len(array) - i - 1])
    return result

array_1 = [2, 3, 4, 5, 6]
array_2 = [2, 3, 5, 6]

print(f'Произведение пар чисел первого массива {array_1} = {pair_of_numbers(array_1)}')
print(f'Произведение пар чисел второго массива {array_2} = {pair_of_numbers(array_2)}')