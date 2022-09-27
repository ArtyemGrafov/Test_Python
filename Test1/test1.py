# print(sum(map(int, str(abs(float(input("Enter num: ")))).replace(".", ""))))


"""from math import factorial

[print(factorial(i + 1), end = " ") for i in range(int(input("Enter num: ")))]"""



import random

def arrayShuffle(arr):
    for i in range(len(arr)):
        j = random.randint(0, 9)
        arr[i], arr[j] = arr[j], arr[i]

array = [random.randint(0, 100) for i in range(10)]

print(*array)

arrayShuffle(array)

print(*array)