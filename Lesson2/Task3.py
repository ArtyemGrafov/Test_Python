# Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами, выводится на экран, 
# затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!

import random

def arrayShuffle(arr):
    for i in range(len(arr)):
        j = random.randint(0, len(arr) - 1)
        arr[i], arr[j] = arr[j], arr[i]

array = [random.randint(0, 100) for i in range(10)]

print(array)

arrayShuffle(array)

print(array)