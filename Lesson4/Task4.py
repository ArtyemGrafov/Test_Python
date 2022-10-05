#  Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

import random

def getMinMultiplier(n):
    multiplier = 2
    while multiplier <= n:
        if n%multiplier == 0: 
            return multiplier
        else:
            multiplier += 1

def getSimpleMultipliers(n):
    listN = []
    while n > 1:        
        multiplier = getMinMultiplier(n)
        listN.append(multiplier)
        n = n // multiplier
    return listN

def multMultipliers(divNumA, divNumB):
    num = 1
    for n in divNumA:
        num *= n
    tmp = [i for i in divNumB if i not in divNumA or divNumA.remove(i)]
    for div in tmp:
        num *= div
    return num

a = random.randint(1, 100)
b = random.randint(1, 100)

print(f"1st num = {a}, 2nd num = {b}")

if a == b:
    print(f"Smallest common multiple = {a}")
elif a == 1:
    print(f"Smallest common multiple = {b}")   
    print(f"Smallest common multiple = {a}")
else: 
    print(f"Smallest common multiple = {multMultipliers(getSimpleMultipliers(a), getSimpleMultipliers(b))}")
