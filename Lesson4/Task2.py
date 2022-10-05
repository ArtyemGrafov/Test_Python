# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

def getList(len):
    return [random.randint(0, 10) for i in range(len)]

def excludeDuplicateElements(list):
    res = []
    for x in list:
        if x not in res: res.append(x)
    return res

try:
    n = int(input("Enter length: "))
    arr = getList(n)
    res = excludeDuplicateElements(arr)
    print(f"sourse = {arr}")  
    print(f"result = {res}")
except Exception:
    print("Enter INT")