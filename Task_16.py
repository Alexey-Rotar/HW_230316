# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

import random
n = input("Введите количество элементов в массиве: ")
numbersArray = list()
if n == "1":
    numbersArray.append(int(n))
else:    
    for i in range(int(n)):
        numbersArray.append(random.randint(1, int(int(n)/2)))
print(numbersArray)
x = input("Введите искомое число: ")
count = numbersArray.count(int(x))
print(f"Количество \"{x}\" в массиве: {count}")