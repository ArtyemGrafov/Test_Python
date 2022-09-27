# print(sum(map(int, str(abs(float(input("Enter num: ")))).replace(".", ""))))


"""from math import factorial

[print(factorial(i + 1), end = " ") for i in range(int(input("Enter num: ")))]"""



"""import random

def arrayShuffle(arr):
    for i in range(len(arr)):
        j = random.randint(0, len(arr) - 1)
        arr[i], arr[j] = arr[j], arr[i]

array = [random.randint(0, 100) for i in range(10)]

print(*array)

arrayShuffle(array)

print(*array)"""

"""n = int(input("Enter n: "))
res = 0

coord = [[0 for j in range(n)] for i in range(2)]

for i in range(2):
    for j in range(n):
        coord[i][j] = int(input(f'Enter coord {j + 1} point {i + 1} : '))

if n == 1: print(abs(coord[0][0] - coord[1][0]))
else:
    for i in range(n):
        res += pow(coord[0][i] - coord[1][i], 2)
    print(res ** (0.5))"""

"""import random
import time

timeStart = time.time()

def checkTruthfulness(x, y, z):
    count = 0
    for x in range(2):
        for y in range(2):
            for z in range(2):
                c
                print(x, y, z, " - ", not (x or y or z) == (not x and not y and not z))
                print(count)

def generateVariants(n):
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                checkTruthfulness(i, j, k)

p = random.randint(5, 12)

for i in range(10):
    generateVariants(p)

timeEnd = time.time()

print(f"Program execution time: {timeEnd - timeStart}")"""