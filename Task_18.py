# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

import random
n = input("Введите количество элементов в массиве: ")
numbers = list()
for i in range(int(n)):
    numbers.append(random.randint(1, int(int(n)/2)))
print(numbers)

x = input("Введите проверяемое число: ")
numbers.append(int(x))
numbers = set(numbers)
numbers = list(numbers)

index = numbers.index(int(x))
if index == 0:
    index = index + 1
elif index == len(numbers) - 1 or numbers[index + 1] - int(x) == int(x) - numbers[index - 1] or numbers[index + 1] - int(x) > int(x) - numbers[index - 1]:
    index = index - 1
else: 
    index = index + 1
   
print(f"Ближайшее к {x} значение: {numbers[index]}")