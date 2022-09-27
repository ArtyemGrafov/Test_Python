# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# Количество предикатов генерируется случайным образом от 5 до 11, проверяем это утверждение 10 раз, 
# с помощью модуля time выводим на экран , сколько времени отработала программа.

import random
import time

timeStart = time.time()

def checkTruthfulness(x, y, z):    
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(x, y, z, " - ", not (x or y or z) == (not x and not y and not z))
                print("----------------")

def generateVariants(n):
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                checkTruthfulness(i, j, k)

p = random.randint(5, 12)

for i in range(10):
    generateVariants(p)

timeEnd = time.time()

print(f"Program execution time: {timeEnd - timeStart}")